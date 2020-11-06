import datetime
from flask import render_template
from atsocial import app

pages = [{'id': 1, 'title': 'Home','figure_name':'fa fa-home'},\
        {'id': 2, 'title': 'Upload','figure_name':'fa fa-cloud-upload'},\
        {'id':3, 'title':'Friends', 'figure_name': 'fa fa-users'},\
        {'id':4, 'title': 'Myprofile','figure_name': 'fa fa-id-badge'}]

ekstrapages = [{'id': 1, 'title':'Settings', 'figure_name':'fa fa-cogs'},\
        {'id':2, 'title':'Help/FAQ', 'figure_name':'fa fa-question-circle-o'},\
        {'id': 3, 'title':'Log Out', 'figure_name':'fa fa-lock'}]

# dictionary

@app.route('/')  # Dette er localhost:5000
def login():
    return render_template('login.html', pages=pages) 

@app.route('/index')
def index():
    return render_template('index.html', pages=pages) 



@app.route('/page/<int:page_id>')
def page(page_id):
    return render_template('page.html', page=pages[page_id - 1])



