from flask import Flask, render_template, redirect
from data import db_session
from data.trainings import Training
from data.users import User
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField, StringField, BooleanField
from wtforms.validators import DataRequired


app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')


class TrainingsForm(FlaskForm):
    train = StringField('Training Title')
    trainer = StringField('Trainer ID')
    aboniment = StringField('Aboniment')
    chads = StringField('Chads')
    is_finished = BooleanField('Is training finished')
    submit = SubmitField('Submit')


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
def index():
    session = db_session.create_session()
    trainings = session.query(Training).all()
    users = session.query(User).all()
    names = {name.id: name.nickname for name in users}
    return render_template("index.html", trainings=trainings, names=names)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect('/')
        return render_template('login.html',
                               message='Неправильный логин или пароль',
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')


@app.route('/addtrain', methods=['GET', 'POST'])
@login_required
def addtrain():
    form = TrainingsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        trains = Training()
        trains.train = form.train.data
        trains.aboniment = form.aboniment.data
        trains.collaborators = form.chads.data
        trains.is_finished = form.is_finished.data
        trains.trainer = form.trainer.data
        current_user.terains.append(trains)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/')
    return render_template('training.html', title='Adding a Training', form=form)


def main():
    db_session.global_init("db/gigachads.db")
    app.run(host='127.0.0.1', port=8080)

main()
