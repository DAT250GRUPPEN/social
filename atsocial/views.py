import datetime
from flask import render_template, Blueprint
from atsocial import app

pages = [{'id': 1, 'title': 'Home','figure_name':'fa fa-home'},\
        {'id': 2, 'title': 'Upload','figure_name':'fa fa-cloud-upload'},\
        {'id':3, 'title':'Friends', 'figure_name': 'fa fa-users'},\
        {'id':4, 'title': 'Myprofile','figure_name': 'fa fa-id-badge'}]

#ekstrapages = [{'id': 1, 'title':'Settings', 'figure_name':'fa fa-cogs'},\
#        {'id':2, 'title':'Help/FAQ', 'figure_name':'fa fa-question-circle-o'},\
#        {'id': 3, 'title':'Log Out', 'figure_name':'fa fa-lock'}]

userspages = [{'id': 1, 'title':'test_user_en', 'figure_name':'fa fa-cogs'},\
              {'id': 2, 'title':'test_user_to', 'figure_name':'fa fa-question-circle-o'},\
              {'id': 3, 'title':'teskt_user_tre', 'figure_name':'fa fa-lock'}]


views = Blueprint("views",__name__)

@app.route('/')  # Dette er localhost:5000
def login():
    return render_template('login.html') 

@app.route('/index')
def index():            # pages kunne ha hettet noe annet og att lik pages: side=pages
    return render_template('index.html', pages=pages) 

@app.route('/page/<int:page_id>')
def page(page_id):
    return render_template('page.html', page=pages[page_id - 1])
# Kan mend fordel dobbeltsjekkes med "flask routing exercise" - filmen.
# de ovenfor er til hovedmenyen

    
@app.route('/users/<int:userspages_id>') # Husk at id-en for input username i registreringen heter "username"
def username(userspages_id):
    return render_template('users.html', usernumber = userspages[userspages_id - 1])
    

