import unittest
from datetime import date
import sys
sys.path.append( "src" )
sys.path.append( "." )
from controller.app_controller import ControladorUsuarios, ControladorHipotecas

class ControladorHipotecasTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.controlador_usuarios = ControladorUsuarios()
        cls.controlador_hipotecas = ControladorHipotecas()

    def setUp(self):
        # Eliminar todos los registros de las tablas antes de cada prueba
        with self.controlador_usuarios.conexion.cursor() as cursor:
            cursor.execute("DELETE FROM hipotecas")
            cursor.execute("DELETE FROM usuarios")
            self.controlador_usuarios.conexion.commit()

    def tearDown(self):
        pass  # No es necesario realizar acciones adicionales después de cada prueba

    def test_crear_usuario(self):
        usuario = self.controlador_usuarios.crear_usuario("Matias Herrera", 68)
        usuarios = self.controlador_usuarios.obtener_usuarios()
        self.assertEqual(len(usuarios), 1)
        self.assertEqual(usuario.name, "Matias Herrera")
        self.assertEqual(usuario.age, 68)

    def test_crear_hipoteca(self):
        usuario = self.controlador_usuarios.crear_usuario("Juan José", 75)
        monto_total = 200000.0
        fecha_inicio = date(2023, 1, 1)
        cuota_mensual = 1000
        self.controlador_hipotecas.crear_hipoteca(usuario.id, monto_total, fecha_inicio, cuota_mensual)
        hipotecas = self.controlador_hipotecas.obtener_hipotecas(usuario.id)
        self.assertEqual(len(hipotecas), 1)
        self.assertEqual(hipotecas[0]["monto_total"], monto_total)
        self.assertEqual(hipotecas[0]["fecha_inicio"], fecha_inicio)
        self.assertEqual(hipotecas[0]["cuota_mensual"], cuota_mensual)

    def test_modificar_usuario(self):
        usuario = self.controlador_usuarios.crear_usuario("Matias Herrera", 68)
        nuevo_nombre = "Matias Herrera Vanegas"
        nueva_edad = 75
        self.controlador_usuarios.modificar_usuario(usuario.id, nuevo_nombre, nueva_edad)
        usuario_actualizado = self.controlador_usuarios.obtener_usuarios()[0]
        self.assertEqual(usuario_actualizado.name, nuevo_nombre)
        self.assertEqual(usuario_actualizado.age, nueva_edad)

    def test_eliminar_usuario(self):
        usuario = self.controlador_usuarios.crear_usuario("Matias Herrera", 68)
        self.controlador_usuarios.eliminar_usuario(usuario.id)
        usuarios = self.controlador_usuarios.obtener_usuarios()
        self.assertEqual(len(usuarios), 0)

    def test_obtener_usuarios(self):
        self.controlador_usuarios.crear_usuario("Matias Herrera", 68)
        self.controlador_usuarios.crear_usuario("Juan José", 75)
        usuarios = self.controlador_usuarios.obtener_usuarios()
        self.assertEqual(len(usuarios), 2)
        self.assertEqual(usuarios[0].name, "Matias Herrera")
        self.assertEqual(usuarios[1].name, "Juan José")

    def test_obtener_hipotecas(self):
        usuario = self.controlador_usuarios.crear_usuario("Matias Herrera", 68)
        monto_total = 2000000
        fecha_inicio = date(2023, 1, 1)
        cuota_mensual = 1000
        self.controlador_hipotecas.crear_hipoteca(usuario.id, monto_total, fecha_inicio, cuota_mensual)
        hipotecas = self.controlador_hipotecas.obtener_hipotecas(usuario.id)
        self.assertEqual(len(hipotecas), 1)
        self.assertEqual(hipotecas[0]["monto_total"], monto_total)
        self.assertEqual(hipotecas[0]["fecha_inicio"], fecha_inicio)
        self.assertEqual(hipotecas[0]["cuota_mensual"], cuota_mensual)

    def test_modificar_hipoteca(self):
        usuario = self.controlador_usuarios.crear_usuario("Diego Sanabria", 75)
        monto_total = 350000000
        fecha_inicio = date(2023, 1, 1)
        cuota_mensual = 2250000
        self.controlador_hipotecas.crear_hipoteca(usuario.id, monto_total, fecha_inicio, cuota_mensual)

        # Obtenemos la hipoteca creada
        hipotecas = self.controlador_hipotecas.obtener_hipotecas(usuario.id)
        hipoteca_id = hipotecas[0]["id"]

        # Modificamos la cuota mensual de la hipoteca
        nueva_cuota_mensual = 1200000
        self.controlador_hipotecas.modificar_hipoteca(hipoteca_id, nueva_cuota_mensual)

        # Obtenemos la hipoteca y verificamos que la cuota mensual se haya actualizado correctamente
        hipotecas = self.controlador_hipotecas.obtener_hipotecas(usuario.id)
        self.assertEqual(len(hipotecas), 1)
        self.assertEqual(hipotecas[0]["cuota_mensual"], nueva_cuota_mensual)

    def test_crear_usuario_con_datos_invalidos(self):
        with self.assertRaises(Exception) as cm:
            self.controlador_usuarios.crear_usuario("", 68)
        self.assertIn("Datos inválidos para crear usuario", str(cm.exception))

        with self.assertRaises(Exception) as cm:
            self.controlador_usuarios.crear_usuario("Matias Herrera", -1)
        self.assertIn("Datos inválidos para crear usuario", str(cm.exception))

    def test_crear_hipoteca_para_usuario_inexistente(self):
        usuario_id_inexistente = 9999
        monto_total = 200000000
        fecha_inicio = date(2023, 1, 1)
        cuota_mensual = 1000
        with self.assertRaises(Exception) as cm:
            self.controlador_hipotecas.crear_hipoteca(usuario_id_inexistente, monto_total, fecha_inicio, cuota_mensual)
        self.assertIn("El usuario no existe", str(cm.exception))

    def test_modificar_hipoteca_inexistente(self):
        hipoteca_id_inexistente = 9999
        nueva_cuota_mensual = 1000000
        with self.assertRaises(Exception) as cm:
            self.controlador_hipotecas.modificar_hipoteca(hipoteca_id_inexistente, nueva_cuota_mensual)
        self.assertIn("La hipoteca no existe", str(cm.exception))

    def test_eliminar_usuario_inexistente(self):
        usuario_id_inexistente = 9999
        with self.assertRaises(Exception) as cm:
            self.controlador_usuarios.eliminar_usuario(usuario_id_inexistente)
        self.assertIn("El usuario no existe", str(cm.exception))

if __name__ == '__main__':
    unittest.main(verbosity=2)
