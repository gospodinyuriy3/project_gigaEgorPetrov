from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


# Добавляем тренера)
def main():
    db_session.global_init("db/gigachads.db")
    session = db_session.create_session()

    user1 = User()
    user1.nickname = "Эрнест Халимов"
    user1.age = 1000
    user1.weight = 500
    user1.height = 250
    user1.speciality = 'гуру'
    user1.email = "giga@chad.ru"
    user1.hashed_password = "qwerty"
    user1.set_password(user1.hashed_password)
    session.add(user1)

    user2 = User()
    user2.nickname = "Ryan Gosling"
    user2.age = 43
    user2.weight = 80
    user2.height = 190
    user2.speciality = 'driver'
    user2.email = "ne_umer@_v_konce.su"
    user2.hashed_password = "scorpion"
    user2.set_password(user2.hashed_password)
    session.add(user2)

    user3 = User()
    user3.nickname = "Patrick Pateman"
    user3.age = 30
    user3.weight = 80
    user3.height = 190
    user3.speciality = 'reach man'
    user3.email = "american@psycho.su"
    user3.hashed_password = "xoxoxo"
    user3.set_password(user3.hashed_password)
    session.add(user3)

    user4 = User()
    user4.nickname = "Кира Йошикаге"
    user4.age = 33
    user4.weight = 75
    user4.height = 180
    user4.speciality = 'главный злодей алмаза'
    user4.email = "killer@quenn.su"
    user4.hashed_password = "bite_the_dust"
    user4.set_password(user4.hashed_password)
    session.add(user4)

    user5 = User()
    user5.nickname = "Тайлер Дерден"
    user5.age = 35
    user5.weight = 80
    user5.height = 190
    user5.speciality = 'твоя работа это не ты сам'
    user5.email = "shiza@_u_menya_concretno"
    user5.hashed_password = "fight_club"
    user5.set_password(user5.hashed_password)
    session.add(user5)

    user6 = User()
    user6.nickname = "Гордей"
    user6.age = 16
    user6.weight = 65
    user6.height = 170
    user6.speciality = 'творец'
    user6.email = "popipo@228"
    user6.hashed_password = "12345"
    user6.set_password(user6.hashed_password)
    session.add(user6)

    session.commit()


if __name__ == '__main__':
    main()
