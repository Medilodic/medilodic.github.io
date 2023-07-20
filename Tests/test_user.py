from flask_login import login_user, current_user, logout_user

from flaskblog import db, bcrypt
from flaskblog.models import User


def test_register(client, app):
    response = client.get("/register")
    assert b"<title>Flask Blog - Register</title>" in response.data

    hashed_password = bcrypt.generate_password_hash('password').decode('utf-8')
    user = User(username='testUser', email='test@test.com', password=hashed_password)

    with app.app_context():
        db.drop_all()
        db.create_all()

        db.session.add(user)
        db.session.commit()

        assert User.query.count() == 1
        assert User.query.first().email == 'test@test.com'


def test_login(client, app):
    response = client.get("/login")
    assert b"<title>Flask Blog - Login</title>" in response.data

    hash_correct_pass = bcrypt.generate_password_hash('password').decode('utf-8')
    correct_pass = 'password'
    incorrect_pass = bcrypt.generate_password_hash('notpassword').decode('utf-8')

    with app.app_context():
        user = User.query.filter_by(email='test@test.com').first()

        if user and bcrypt.check_password_hash(hash_correct_pass, correct_pass):
            login_user(user, remember=False)
        assert current_user == user

        logout_user()

        if user and bcrypt.check_password_hash(hash_correct_pass, incorrect_pass):
            login_user(user, remember=False)
        assert current_user != user
