from flask import Blueprint, render_template, request, redirect
from .models import Tarea
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    tareas = Tarea.query.all()
    return render_template('index.html', tasks=tareas)

@main.route('/agregar', methods=['POST'])
def agregar():
    contenido = request.form['contenido']
    nueva = Tarea(contenido=contenido)
    db.session.add(nueva)
    db.session.commit()
    return redirect('/')
