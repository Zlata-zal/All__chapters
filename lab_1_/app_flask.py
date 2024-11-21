from flask import Flask, request, jsonify
from models import session, Hero

app = Flask(__name__)

@app.route("/heroes", methods=["GET"])
def get_heroes():
    heroes = session.query(Hero).all()
    return jsonify([{"id": hero.id, "name": hero.name, "power": hero.power, "rank": hero.rank} for hero in heroes])

@app.route("/heroes", methods=["POST"])
def add_hero():
    data = request.json
    new_hero = Hero(name=data["name"], power=data["power"], rank=data["rank"])
    session.add(new_hero)
    session.commit()
    return jsonify({"id": new_hero.id, "name": new_hero.name, "power": new_hero.power, "rank": new_hero.rank}), 201

@app.route("/heroes/<int:hero_id>", methods=["PUT"])
def update_hero(hero_id):
    data = request.json
    hero = session.query(Hero).filter(Hero.id == hero_id).first()
    if hero:
        if "name" in data:
            hero.name = data["name"]
        if "power" in data:
            hero.power = data["power"]
        if "rank" in data:
            hero.rank = data["rank"]
        session.commit()
        return jsonify({"id": hero.id, "name": hero.name, "power": hero.power, "rank": hero.rank})
    return jsonify({"error": "Hero not found"}), 404


@app.route("/heroes/<int:hero_id>", methods=["DELETE"])
def delete_hero(hero_id):
    hero = session.query(Hero).filter(Hero.id == hero_id).first()
    if hero:
        session.delete(hero)
        session.commit()
        return jsonify({"message": "Hero deleted"})
    return jsonify({"error": "Hero not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
