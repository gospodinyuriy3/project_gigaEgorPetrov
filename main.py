from flask import Flask, render_template
from data import db_session
from data.users import User
from flask_login import LoginManager, login_user, logout_user
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
def root():
    user = 'Реальный гигачад'

    return render_template('base.html', title='Пристанищение гигчадов',
                           username=user)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)