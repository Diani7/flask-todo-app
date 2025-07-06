from myapp import db, create_app

app = create_app()

with app.app_context():
    #db.drop_all()  # Elimina todas las tablas, puedes descomentar esta linea si deseas reiniciar la base de datos, recuerda que esto te eliminara todo
    db.create_all()
    print("Base de datos creada o actualizada correctamente.")
