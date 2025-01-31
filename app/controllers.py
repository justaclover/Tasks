from abc import ABC, abstractmethod
from app import db
from werkzeug.utils import redirect
from flask import render_template_string


class Controller(ABC):
    def __init__(self, model):
        self.model = model


class TaskController(Controller):
    def store(self, name, description):
        task = self.model(name=name, description=description)

        try:
            db.session.add(task)
            db.session.commit()
        except Exception as e:
            return f"{e}"

    def destroy(self, id):
        task = db.session.query(self.model).filter_by(id=id).first()

        try:
            db.session.delete(task)
            db.session.commit()
            return redirect('/home')
        except Exception as e:
            return f"{e}"


class HomeController(Controller):
    def index(self, template_dir):
        return self.model.query.all()
        #return render_template_string(template_dir + '\home.html', tasks=tasks)