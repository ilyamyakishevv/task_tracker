from tasktrackerapp import db, create_app

app = create_app()

with app.app_context(): 
<<<<<<< HEAD
    db.create_all()
=======
    db.create_all()
>>>>>>> a23f2ae09310f68ed3f07685ac9ff3418b4fffaf
