from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from atsocial import db,app
from werkzeug.security import generate_password_hash,check_password_hash#,check_password
from atsocial.models import User, Post
from atsocial.forms import RegistrationForm, LoginForm, UpdateUserForm
from atsocial.users.picture_handler import add_profile_pic

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
@views.route("/",methods=["GET","POST"])
def login():
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:

            login_user(user)
            flash("Log inn success!")

            next = request.args.get("next")

            if next == None or not next[0]=="/":
                next = url_for("views.login")

            return redirect(next)
    return render_template("login.html",form=form)


# THANKYOU for registering -siden
@app.route('/thank_you')  
def thank_you():
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template('thank_you.html', first=first,last=last)


#@views.route("/register",methods=["GET","POST"])
#def register():
    
    #form = RegistrationForm()
   # if form.validate_on_submit():
        #user = User(first_name=form.first_name.data,
                    #last_name=form.last_name.data,
                    #email=form.email.data,
                    #password=form.password.data)

       # db.session.add(user)
      #  db.session.commit()
     #   return redirect("views.register")
    #return render_template("register.html", form=form)




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