from authentication import db
from authentication import login_manager
from flask_login import UserMixin
from authentication import flask_bcrypt


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=100), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60),nullable=False)

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = flask_bcrypt.generate_password_hash(plain_text_password).decode("utf-8")

    def check_password(self, attempted_password):
        if flask_bcrypt.check_password_hash(self.password_hash, attempted_password):
            return True

    def __str__(self):
        return self.username
