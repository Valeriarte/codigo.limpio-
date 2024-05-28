

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/view/nuevo-usuario")
def VistaNuevoUsuario():
   return render_template("crear-usuario.html")

@app.route('/crear-usuario', methods=['GET', 'POST'])
def VistaCrearUsuario():
    nombre = request.args["name"]
    edad = request.args["age"]
    nuevo_usuario = User(nombre,edad)
    usuario = controlador_usuarios.crear_usuario(nuevo_usuario)
    usuarios = controlador_usuarios.obtener_usuarios()
    
    #return render_template('create_user.html')

@app.route('/calcular-hipoteca', methods=['GET', 'POST'])
def calculate_mortgage():
    if request.method == 'POST':
        # Aquí agregarías la lógica para calcular la hipoteca
        return render_template('calculate_mortgage.html', result="Resultado del cálculo")
    return render_template('calculate_mortgage.html', result=None)

@app.route('/lista-usuarios')
def list_users():
    # Aquí agregarías el código para obtener la lista de usuarios de la base de datos
    return render_template('list_users.html', users=[])
