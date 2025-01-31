from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import os
import pymysql
from flask_sqlalchemy import SQLAlchemy


template_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
template_dir = os.path.join(template_dir, 'Tasks')
template_dir = os.path.join(template_dir, 'app')
template_dir = os.path.join(template_dir, 'templates')

app = Flask(__name__, template_folder='templates')

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'tasks'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/tasks'


db = pymysql.connections.Connection(
    host='localhost',
    user='root',
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS tasks")
cursor.close()
db.close()


mysql = MySQL(app)
db = SQLAlchemy(app)

from app.controllers import HomeController, TaskController
from app.models import TaskModel

home_controller = HomeController(models.TaskModel)
task_controller = TaskController(models.TaskModel)
from app import routes

