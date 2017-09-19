from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

# import config_example

app = Flask(__name__)
app_config = config.runtime_config("dev")

#app_coonfig = config.example.runtime_config("dev")

app.config.from_object(app_config)
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User ID: {}, NAME: {}, EMAIL: {}>'.format(
            self.id,
            self.username,
            self.email,
        )

db.drop_all()
db.create_all()
admin = User(username='admin', email='admin@example.com')
db.session.add(admin)
db.session.commit()
print(User.query.filter_by(username='admin').first())

@app.route('/')
def hello_world():
    return 'Hello world!'
