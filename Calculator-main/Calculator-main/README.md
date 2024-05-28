# Calculadora de hipoteca inversa.

El proyecto consiste en desarrollar una aplicación en Python
que permita calcular la cuota mensual que un banco le pagaría 
a una persona que ha adquirido una hipoteca inversa.

## Integrantes del grupo:
- Diego Sanabria Gómez.
- Andrés Julián Murillo.

## Estructura del proyecto:
- src: Contiene la lógica de negocio (model), las interfaces gráficas (view) y el controlador (controller).
- tests: Contiene las pruebas unitarias del aplicativo.
- sql: Contiene los scripts sql para crear las tablas necesarias para el correcto funcionamiento del controlador.

## Dependencias: 
Asegurese de tener instalado Python en su unidad. Si no lo tiene instalado, puede visitar el siguiente link y descargar el ejecutable: [Python](https://www.python.org/).

La lista de dependencias las encontrará listadas en el archivo 'requirements.txt'. Para descargarlas solo ubiquese en el directorio raíz de la carpeta clonada y ejecute el siguiente comando: `pip install -r requirements.txt`, esto instalará las dependencias necesarias para el funcionamiento del proyecto.

## ¿Cómo se usa?
Para hacer uso del aplicativo asegurese de tener instalado las dependencias necesarias. Una vez tenga las dependencias necesarias prosiga con las instrucciones:

1. Clone el repositorio en su unidad y abra la consola de comandos. Ejecute el siguiente comando: `set PYTHONPATH=[ruta de la carpeta raiz clonada]`. Ignore los corchetes, por ejemplo, en mi caso el comando quedaría de la siguiente manera: `set PYTHONPATH=C:\Users\dsana\Workspace\Calculator`. Cabe recalcar que debe ser ejecutado en una terminal cmd (consola de comandos) y no en una powershell.
2. Ubiquese en la raiz de la carpeta clonada. Use el comando `cd [ruta de la carpeta]`.
3. Si desea correr las pruebas unitarias del modelo del aplicativo:
    - Ubiquese en la carpeta 'tests' de la ruta clonada.
    - Ejecute el siguiente comando: `python tests.py`.
4. Si desea ejecutar las pruebas del controlador:
    - Ubiquese en la carpeta 'tests' de la ruta clonada.
    - Ejecute el siguiente comando: `python controller_tests.py`
5. Si desea ejecutar la interfaz por consola:
    - Ubiquese en la siguiente ruta 'src/view/console'.
    - Ejecute el siguiente comando: `python controller_console.py`
6. Si desea ejecutar la interfaz gráfica de usuario (gui):
    - Ubiquese en la siguiente ruta: 'src/view/interface'.
    - Ejecute el siguiente comando: `python interface.py`.



