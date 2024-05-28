import sys
import os
sys.path.append( "src" )
sys.path.append( "." )

import datetime
from src.model.calculator import Calculator
from src.controller.app_controller import ControladorUsuarios, ControladorHipotecas

def format_number_with_dots(number):
    """Formatea el número agregando puntos para facilitar la lectura"""
    return "{:,.2f}".format(number)

def get_int_input(prompt):
    """Obtiene un valor entero válido del usuario"""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Error: Ingrese un número entero válido.")

def get_float_input(prompt):
    """Obtiene un valor flotante válido del usuario"""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Error: Ingrese un número válido.")

def main():
    controlador_usuarios = ControladorUsuarios()
    controlador_hipotecas = ControladorHipotecas()

    while True:
        print("\nMenú principal:")
        print("1. Registrar nuevo usuario")
        print("2. Modificar usuario existente")
        print("3. Eliminar usuario")
        print("4. Listar usuarios")
        print("5. Calcular hipoteca inversa")
        print("6. Salir")

        opcion = get_int_input("Ingrese una opción: ")

        if opcion == 1:
            # Registrar nuevo usuario
            nombre = input("Ingrese el nombre: ")
            edad = get_int_input("Ingrese la edad: ")
            try:
                usuario = controlador_usuarios.crear_usuario(nombre, edad)
                print("Usuario registrado correctamente.")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == 2:
            # Modificar usuario existente
            usuarios = controlador_usuarios.obtener_usuarios()
            if not usuarios:
                print("No hay usuarios registrados.")
            else:
                print("Usuarios registrados:")
                for usuario in usuarios:
                    print(f"ID: {usuario.id}, Nombre: {usuario.name}, Edad: {usuario.age}")

                id_usuario = get_int_input("Ingrese el ID del usuario a modificar: ")
                usuario_modificar = next((u for u in usuarios if u.id == id_usuario), None)

                if usuario_modificar:
                    nombre = input(f"Ingrese el nuevo nombre (actual: {usuario_modificar.name}): ") or usuario_modificar.name
                    edad = get_int_input(f"Ingrese la nueva edad (actual: {usuario_modificar.age}): ") or usuario_modificar.age

                    try:
                        controlador_usuarios.modificar_usuario(usuario_modificar.id, nombre, edad)
                        print("Usuario modificado correctamente.")
                    except Exception as e:
                        print(f"Error: {e}")
                else:
                    print("No se encontró el usuario.")

        elif opcion == 3:
            # Eliminar usuario
            usuarios = controlador_usuarios.obtener_usuarios()
            if not usuarios:
                print("No hay usuarios registrados.")
            else:
                print("Usuarios registrados:")
                for usuario in usuarios:
                    print(f"ID: {usuario.id}, Nombre: {usuario.name}, Edad: {usuario.age}")

                id_usuario = get_int_input("Ingrese el ID del usuario a eliminar: ")
                try:
                    controlador_usuarios.eliminar_usuario(id_usuario)
                    print("Usuario eliminado correctamente.")
                except Exception as e:
                    print(f"Error: {e}")

        elif opcion == 4:
            # Listar usuarios
            usuarios = controlador_usuarios.obtener_usuarios()
            if not usuarios:
                print("No hay usuarios registrados.")
            else:
                print("Usuarios registrados:")
                for usuario in usuarios:
                    print(f"ID: {usuario.id}, Nombre: {usuario.name}, Edad: {usuario.age}")

        elif opcion == 5:
            # Calcular hipoteca inversa
            usuarios = controlador_usuarios.obtener_usuarios()
            if not usuarios:
                print("No hay usuarios registrados. Registre un usuario primero.")
            else:
                print("Usuarios registrados:")
                for usuario in usuarios:
                    print(f"ID: {usuario.id}, Nombre: {usuario.name}, Edad: {usuario.age}")

                id_usuario = get_int_input("Ingrese el ID del usuario: ")
                usuario = next((u for u in usuarios if u.id == id_usuario), None)

                if usuario:
                    monto_total = get_float_input("Ingrese el monto total de la hipoteca: ")
                    esperanza_vida = get_int_input("Ingrese la esperanza de vida esperada: ")
                    periodo_pago = get_int_input("Ingrese el período de tiempo para las tarifas (en años): ")
                    porcentaje_propiedad = get_float_input("Ingrese el porcentaje de valor de la propiedad: ")
                    mortgage_type = int(input("Ingrese el tipo de hipoteca (1 para hipoteca vitalicia, 2 para hipoteca parcial, 3 para hipoteca total): "))

                    try:
                        calculadora = Calculator(monto_total, usuario.age, esperanza_vida, periodo_pago, porcentaje_propiedad, mortgage_type)
                        cuota_mensual = calculadora.calculate_monthly_fee()
                        print(f"La cuota mensual de la hipoteca inversa es: {format_number_with_dots(cuota_mensual)}")

                        # Agregar nueva hipoteca
                        controlador_hipotecas.crear_hipoteca(usuario.id, monto_total, datetime.date.today(), cuota_mensual)
                        print("Hipoteca registrada correctamente.")
                    except Exception as e:
                        print(f"Error: {e}")
                else:
                    print("No se encontró el usuario.")

        elif opcion == 6:
            # Salir
            break

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()