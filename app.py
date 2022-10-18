from flask import (render_template, redirect,
                   url_for, current_app, request)
from models import db, Pet, app


@app.route("/")
def index():
    pets = Pet.query.all()
    return render_template("index.html", pets=pets)


@app.route("/add-pet", methods=["GET", "POST"])
def add_pet():
    if request.form:
        new_pet = Pet(name=request.form["name"], age=request.form["age"],
                      breed=request.form["breed"], color=request.form["color"],
                      size=request.form["size"], weight=request.form["weight"],
                      url=request.form["url"], url_tag=request.form["alt"],
                      pet_type=request.form["pet"], gender=request.form["gender"],
                      spay=request.form["spay"], house_trained=request.form["housetrained"],
                      description=request.form["description"])
        db.session.add(new_pet)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("addpet.html")


@app.route("/pet")
def pet():
    return render_template("pet.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000, host="127.0.0.1")