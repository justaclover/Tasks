from app import db, mysql, home_controller, template_dir, task_controller
from flask import render_template, redirect
from flask import send_from_directory, request
import os
from app import app


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico')
@app.route("/")
def index():
    return render_template('home.html', tasks=home_controller.index(template_dir))

@app.route("/task", methods=['POST'])
def store():
    name = request.form['name']
    description = request.form['description']

    task_controller.store(name, description)
    return redirect('/')

@app.route("/task/<id>/delete", methods=['GET'])
def destroy(id):
    task_controller.destroy(id)
    return redirect('/')