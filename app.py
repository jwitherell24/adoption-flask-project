from flask import (render_template, 
                   url_for, current_app, request)
from models import db, Pet, app


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add-pet", methods=["GET", "POST"])
def add_pet():
    print(request.form)
    print(request.form["name"])
    return render_template("addpet.html")


@app.route("/pet")
def pet():
    return render_template("pet.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000, host="127.0.0.1")