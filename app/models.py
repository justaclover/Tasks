from flask_sqlalchemy import SQLAlchemy
from app import db

class TaskModel(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f'<Task {self.name}>'


