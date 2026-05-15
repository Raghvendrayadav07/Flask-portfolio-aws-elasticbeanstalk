import json
import os
from flask import Flask, render_template, request, redirect, url_for, session, flash

application = Flask(__name__)
application.secret_key = 'raghu-portfolio-2025-change-this'

PROJECTS_FILE = os.path.join(os.path.dirname(__file__), 'projects.json')
ADMIN_PASSWORD = 'raghu@aws2025'


def load_projects():
    with open(PROJECTS_FILE, 'r') as f:
        return json.load(f)


def save_projects(projects):
    with open(PROJECTS_FILE, 'w') as f:
        json.dump(projects, f, indent=2)


@application.route('/')
def index():
    projects = load_projects()
    return render_template('index.html', projects=projects)


@application.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST' and 'password' in request.form:
        if request.form['password'] == ADMIN_PASSWORD:
            session['admin'] = True
        else:
            flash('Wrong password.')
        return redirect(url_for('admin'))

    if not session.get('admin'):
        return render_template('login.html')

    projects = load_projects()
    return render_template('admin.html', projects=projects)


@application.route('/admin/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@application.route('/admin/add', methods=['POST'])
def add_project():
    if not session.get('admin'):
        return redirect(url_for('admin'))

    projects = load_projects()
    new_id = max((p['id'] for p in projects), default=0) + 1
    tags = [t.strip() for t in request.form.get('tags', '').split(',') if t.strip()]

    projects.insert(0, {
        'id': new_id,
        'title': request.form.get('title', ''),
        'short': request.form.get('short', ''),
        'description': request.form.get('description', ''),
        'tags': tags,
        'live_url': request.form.get('live_url', ''),
        'github_url': request.form.get('github_url', ''),
        'date': request.form.get('date', '')
    })
    save_projects(projects)
    flash('Project added successfully!')
    return redirect(url_for('admin'))


@application.route('/admin/delete/<int:project_id>', methods=['POST'])
def delete_project(project_id):
    if not session.get('admin'):
        return redirect(url_for('admin'))

    projects = load_projects()
    projects = [p for p in projects if p['id'] != project_id]
    save_projects(projects)
    flash('Project deleted.')
    return redirect(url_for('admin'))


if __name__ == '__main__':
    application.run(debug=False)
