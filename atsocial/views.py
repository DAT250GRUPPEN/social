import datetime
from flask import Flask, render_template, Blueprint, request
from atsocial import app


################################################################################################
# Disse under er til testing...
pages = [{'id': 1, 'title': 'Upload','figure_name':'fa fa-cloud-upload'},\
        {'id':2, 'title':'Friends', 'figure_name': 'fa fa-users'},\
        {'id':3, 'title': 'Myprofile','figure_name': 'fa fa-id-badge'}]
# Disse under er til testing...
userspages = [{'id': 1, 'name':'test_user_en', 'password':'1234'},\
              {'id': 2, 'name':'test_user_to', 'password':'3456'},\
              {'id': 3, 'name':'teskt_user_tre', 'password':'6789'}]
# Disse under er til testing...
mainuser = [{'id': 1, 'first':'ola', 'last':'nordmann', 'email':'olanordmann@olanordmann','password':'1234'}]
################################################################################################

views = Blueprint("views",__name__)






# LOGIN -siden
@app.route('/')  # Dette er localhost:5000 
def login():
    return render_template('login.html') 


# THANKYOU for registering -siden
@app.route('/thank_you')  
def thank_you():
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template('thank_you.html', first=first,last=last)




#@app.route('/page/<int:page_id>') # Hovedmenyen
#def page(page_id):
#        return render_template('page.html', page=pages[page_id -1])
# Kan mend fordel dobbeltsjekkes med "flask routing exercise" - filmen.




# HOVED MENY - SIDER:
# 
# 
    
# HOME -siden
@app.route('/index')
def index():          
    return render_template('index.html', pages=pages) 

# MYPROFILE -siden
@app.route('/myprofile')  
def myprofile():
    return render_template('myprofile.html') 

# UPLOAD -siden
@app.route('/upload') 
def uploads():
    return render_template('upload.html') 

# MYFRIENDS -siden
@app.route('/myfriends')  
def myfriends():
    return render_template('myfriends.html') 


@app.route('/users/<int:userspages_id>') # Husk at id-en for input username i registreringen heter "username"
def username(userspages_id):
    return render_template('users.html', usernumber = userspages[userspages_id - 1])


    
    





# Dropdown meny:

@app.route('/settings')  # SETTINGS
def settings():
    return render_template('settings.html') 

@app.route('/faq')  # FAQ
def faq():
    return render_template('index.html') 


@app.route('/logout')  # LOGOUT
def logout():
    return render_template('login.html') 


# Footer: group 27
@app.route('/group27')  # GROUP
def group27():
    return render_template('group27.html') 