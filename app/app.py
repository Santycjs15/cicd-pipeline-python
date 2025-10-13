"""Aplicación principal Flask que expone una calculadora web sencilla."""

from flask import Flask, render_template, request
from .calculadora import sumar, restar, multiplicar, dividir
import os


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """Vista principal de la aplicación.

    Maneja los formularios de operaciones aritméticas
    y renderiza la plantilla HTML.
    """

    resultado = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operacion = request.form["operacion"]

            if operacion == "sumar":
                resultado = sumar(num1, num2)
            elif operacion == "restar":
                resultado = restar(num1, num2)
            elif operacion == "multiplicar":
                resultado = multiplicar(num1, num2)
            elif operacion == "dividir":
                resultado = dividir(num1, num2)
            else:
                resultado = "Operación no válida"
        except ValueError:
            resultado = "Error: Introduce números válidos"
        except ZeroDivisionError:
            resultado = "Error: No se puede dividir por cero"

    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":
    # Ejecuta la aplicación Flask en modo desarrollo.
    # Nota: Nunca habilites debug=True en producción. Usa un WSGI server
    # como gunicorn/uwsgi para despliegues y controla el modo debug mediante
    # la variable de entorno FLASK_DEBUG (por defecto está desactivado).
    debug_env = os.environ.get("FLASK_DEBUG", "0")
    debug = str(debug_env).lower() in ("1", "true", "yes")
    port = int(os.environ.get("PORT", "5000"))
    app.run(debug=debug, port=port, host="0.0.0.0")
