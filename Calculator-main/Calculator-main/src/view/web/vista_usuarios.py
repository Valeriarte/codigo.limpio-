from flask import Flask, Blueprint, render_template, request, redirect, url_for

blueprint = Blueprint( "vista_usuarios", __name__, "templates" )

import sys
sys.path.append("src")
sys.path.append(".")
from model.user import Usuario
import controller.app_controller as app_controller

controlador_usuarios = app_controller.ControladorUsuarios()
controlador_hipotecas = app_controller.ControladorHipotecas()

app = Flask(__name__)


@blueprint.route("/")
def Home():
   return render_template("index.html")

@blueprint.route( "/nuevo-usuario")
def VistaNuevoUsuario():
   return render_template("nuevo-usuario.html")

@blueprint.route("/crear-usuario", methods=['POST'])
def crear_usuario_view():
    nombre = request.form.get("nombre")
    edad = request.form.get("edad")
    if edad:
        edad = int(edad)  
    try:
        usuario = controlador_usuarios.crear_usuario(nombre, edad)
        return render_template("usuario.html", user=usuario, mensaje="Usuario insertado exitosamente!")
    except ValueError as e:
        return render_template("excepcion.html", mensaje_error=str(e))
    except Exception as e:
        return render_template("excepcion.html", mensaje_error=f"Usuario Duplicado: {str(e)}")


@blueprint.route("/lista-usuarios")
def lista_usuarios():
    try:
        usuarios = controlador_usuarios.obtener_usuarios()
        return render_template("lista-usuarios.html", usuarios=usuarios)
    except Exception as e:
        return render_template("excepcion.html", mensaje_error=f"Error al obtener usuarios: {str(e)}")

   


