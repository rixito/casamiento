import logging
import os
import time,json
from datetime import date, datetime, timezone
from flask import jsonify, render_template, request,url_for, redirect, Response, abort
from flask_login import login_user, login_required, current_user, logout_user
from juntos import app


logger = logging.getLogger(__name__)

DEFAULT_INTERVAL = app.config['CHARTS_DEFAULT_INTERVAL']
DAYS_INTERVAL = app.config['DAYS_INTERVALTYPE_THRESHOLD']
MINUTES_INTERVAL = app.config['MINUTES_INTERVALTYPE_THRESHOLD']

@app.context_processor
def pass_common_template_info():
    return dict(info={'current_year':  date.today().year})


# =======================================================
# Esas 2 funciones son para que el css no quede cacheado en el browser
# http://flask.pocoo.org/snippets/40/
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)
# =======================================================


@app.route("/", methods=['GET'])
@app.route('/index/', methods=['GET'])
def get_resources():
    return render_template('index.html')


# @app.route('/login/', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         user_id = security.get_user_hash(username, password)
#         user = security.load_user(user_id)
#         if user:
#             login_user(user)
#             next_url = request.args.get("next") if request.args.get("next") else '/'
#             return redirect(next_url)
#         else:
#             errors = 'Invalid Credentials'
#             return render_template('login.html', errors=errors)
#     else:
#         return render_template('login.html')
#
#
# @app.route("/logout")
# @login_required
# def logout():
#     logout_user()
#     return redirect('/')


