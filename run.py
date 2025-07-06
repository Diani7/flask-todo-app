from myapp import create_app, db
from myapp.models import Tarea

app = create_app()

with app.app_context():
    db.create_all()  # Crea las tablas si no existen

if __name__ == '__main__':
    app.run(debug=True)
