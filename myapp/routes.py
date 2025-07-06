from flask import Blueprint, render_template, request, redirect, url_for
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
    return redirect(url_for('main.index'))

@main.route('/completar/<int:tarea_id>', methods=['POST'])
def completar(tarea_id):
    tarea = Tarea.query.get_or_404(tarea_id)
    tarea.completada = not tarea.completada
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/eliminar/<int:tarea_id>', methods=['POST'])
def eliminar(tarea_id):
    tarea = Tarea.query.get_or_404(tarea_id)
    db.session.delete(tarea)
    db.session.commit()
    return redirect(url_for('main.index'))
