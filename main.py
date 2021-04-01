from app import app, db
from app.models import User

@app.shell_contect_processor
def make_shell_context():
    return{"db": db, "User": User}