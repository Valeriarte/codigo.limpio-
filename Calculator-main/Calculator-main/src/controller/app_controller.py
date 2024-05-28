import psycopg2
import sys
sys.path.append("src")
sys.path.append( "." )
from psycopg2 import sql
from psycopg2.extras import RealDictCursor
from model.user import Usuario
import secret_config

class ControladorUsuarios:
    def __init__(self):
        self.conexion = psycopg2.connect(database=secret_config.PGDATABASE, user=secret_config.PGUSER,
                                         password=secret_config.PGPASSWORD, host=secret_config.PGHOST)
        self._crear_tabla_usuarios()

    def _crear_tabla_usuarios(self):
        """
        Crea la tabla de usuarios si no existe.
        """
        with self.conexion.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    age INT NOT NULL,
                    UNIQUE(name, age)
                )
            """)
            self.conexion.commit()

    def crear_usuario(self, nombre, edad):
        """
        Crea un nuevo usuario en la base de datos.

        Args:
            nombre (str): El nombre del usuario.
            edad (int): La edad del usuario.

        Returns:
            Usuario: El objeto Usuario creado.

        Raises:
            Exception: Si ocurre algún error al crear el usuario.
        """
        if not nombre or edad < 0:
            raise Exception("Datos inválidos para crear usuario")

        usuario = Usuario(nombre, edad)
        with self.conexion.cursor() as cursor:
            try:
                cursor.execute("""INSERT INTO usuarios (name, age)
                                  VALUES (%s, %s) RETURNING id""",
                               (usuario.name, usuario.age))
                usuario_id = cursor.fetchone()[0]
                usuario.id = usuario_id
                self.conexion.commit()
            except psycopg2.IntegrityError as e:
                self.conexion.rollback()
                if 'unique constraint' in str(e):
                    raise Exception(f"Usuario con el nombre '{nombre}' y edad '{edad}' ya existe.")
                else:
                    raise Exception(f"Error al crear usuario: {e}")
        return usuario

    def obtener_usuarios(self) -> list[Usuario]:
        """
        Obtiene todos los usuarios de la base de datos.

        Returns:
            list[Usuario]: Una lista de objetos Usuario.
        """
        usuarios = []
        with self.conexion.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("""SELECT id, name, age FROM usuarios""")
            for fila in cursor.fetchall():
                usuario = Usuario(fila['name'], fila['age'])
                usuario.id = fila['id']
                usuarios.append(usuario)
        return usuarios

    def eliminar_usuario(self, usuario_id: int) -> None:
        """
        Elimina un usuario y sus hipotecas asociadas de la base de datos.

        Args:
            usuario_id (int): El ID del usuario a eliminar.

        Raises:
            Exception: Si ocurre algún error al eliminar el usuario.
        """
        with self.conexion.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM usuarios WHERE id = %s", (usuario_id,))
            if cursor.fetchone()[0] == 0:
                raise Exception("El usuario no existe")
            try:
                with self.conexion:
                    cursor.execute("DELETE FROM hipotecas WHERE usuario_id = %s", (usuario_id,))
                    cursor.execute("DELETE FROM usuarios WHERE id = %s", (usuario_id,))
                    self.conexion.commit()
            except psycopg2.Error as e:
                self.conexion.rollback()
                raise Exception(f"Error al eliminar usuario: {e}")

    def modificar_usuario(self, usuario_id: int, nombre: str, edad: int) -> None:
        """
        Modifica los datos de un usuario existente.

        Args:
            usuario_id (int): El ID del usuario a modificar.
            nombre (str): El nuevo nombre del usuario.
            edad (int): La nueva edad del usuario.

        Raises:
            Exception: Si ocurre algún error al modificar el usuario.
        """
        with self.conexion.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM usuarios WHERE id = %s", (usuario_id,))
            if cursor.fetchone()[0] == 0:
                raise Exception("El usuario no existe")

            try:
                with self.conexion:
                    cursor.execute("""UPDATE usuarios SET name = %s, age = %s WHERE id = %s""",
                                   (nombre, edad, usuario_id))
                    self.conexion.commit()
            except psycopg2.Error as e:
                self.conexion.rollback()
                raise Exception(f"Error al modificar usuario: {e}")

class ControladorHipotecas:
    def __init__(self):
        self.conexion = psycopg2.connect(database=secret_config.PGDATABASE, user=secret_config.PGUSER,
                                         password=secret_config.PGPASSWORD, host=secret_config.PGHOST)
        self._crear_tabla_hipotecas()

    def _crear_tabla_hipotecas(self):
        """
        Crea la tabla de hipotecas si no existe.
        """
        with self.conexion.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS hipotecas (
                    id SERIAL PRIMARY KEY,
                    usuario_id INT REFERENCES usuarios(id) ON DELETE CASCADE,
                    monto_total FLOAT NOT NULL,
                    fecha_inicio DATE NOT NULL,
                    cuota_mensual FLOAT NOT NULL
                )
            """)
            self.conexion.commit()

    def crear_hipoteca(self, usuario_id: int, monto_total: float, fecha_inicio: str, cuota_mensual: float) -> None:
        """
        Crea una nueva hipoteca para un usuario en la base de datos.

        Args:
            usuario_id (int): El ID del usuario.
            monto_total (float): El monto total de la hipoteca.
            fecha_inicio (str): La fecha de inicio de la hipoteca.
            cuota_mensual (float): La cuota mensual de la hipoteca.

        Raises:
            Exception: Si ocurre algún error al crear la hipoteca.
        """
        with self.conexion.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM usuarios WHERE id = %s", (usuario_id,))
            if cursor.fetchone()[0] == 0:
                raise Exception("El usuario no existe")

            try:
                with self.conexion:
                    cursor.execute("""INSERT INTO hipotecas (usuario_id, monto_total, fecha_inicio, cuota_mensual)
                                      VALUES (%s, %s, %s, %s)""",
                                   (usuario_id, monto_total, fecha_inicio, cuota_mensual))
                    self.conexion.commit()
            except psycopg2.IntegrityError as e:
                self.conexion.rollback()
                raise Exception(f"Error al crear hipoteca: {e}")

    def obtener_hipotecas(self, usuario_id: int) -> list[dict]:
        """
        Obtiene todas las hipotecas de un usuario.

        Args:
            usuario_id (int): El ID del usuario.

        Returns:
            list[dict]: Una lista de diccionarios, donde cada diccionario representa una hipoteca.
        """
        hipotecas = []
        with self.conexion.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("""SELECT id, monto_total, fecha_inicio, cuota_mensual
                              FROM hipotecas
                              WHERE usuario_id = %s""", (usuario_id,))
            hipotecas = cursor.fetchall()
        return hipotecas
    
    def modificar_hipoteca(self, hipoteca_id: int, nueva_cuota_mensual: float) -> None:
        """
        Modifica una hipoteca existente.

        Args:
            hipoteca_id (int): El ID de la hipoteca a modificar.
            nueva_cuota_mensual (float): La nueva cuota mensual de la hipoteca.

        Raises:
            Exception: Si ocurre algún error al modificar la hipoteca.
        """
        with self.conexion.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM hipotecas WHERE id = %s", (hipoteca_id,))
            if cursor.fetchone()[0] == 0:
                raise Exception("La hipoteca no existe")

            try:
                with self.conexion:
                    cursor.execute("""UPDATE hipotecas SET cuota_mensual = %s WHERE id = %s""",
                                   (nueva_cuota_mensual, hipoteca_id))
                    self.conexion.commit()
            except psycopg2.Error as e:
                self.conexion.rollback()
                raise Exception(f"Error al modificar hipoteca: {e}")
