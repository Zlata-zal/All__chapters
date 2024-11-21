from models import session, Hero

def create_hero(name, power, rank):
    new_hero = Hero(name=name, power=power, rank=rank)
    session.add(new_hero)
    session.commit()
    return new_hero

def read_heroes():
    return session.query(Hero).all()

def update_hero(hero_id, name=None, power=None, rank=None):
    hero = session.query(Hero).filter(Hero.id == hero_id).first()
    if hero:
        if name:
            hero.name = name
        if power:
            hero.power = power
        if rank:
            hero.rank = rank
        session.commit()
        return hero
    return None

def delete_hero(hero_id):
    hero = session.query(Hero).filter(Hero.id == hero_id).first()
    if hero:
        session.delete(hero)
        session.commit()
        return True
    return False


if __name__ == "__main__":

    hero = create_hero("Black Panther", "Super Strength", 1)
    print(f"Создан герой: {hero}")


    heroes = read_heroes()
    print(f"Все герои: {heroes}")


    updated_hero = update_hero(hero_id=1, power="Enhanced Agility")
    print(f"Обновлён герой: {updated_hero}")


    if delete_hero(hero_id=1):
        print("Герой удалён.")
    else:
        print("Герой не найден.")

