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
@views.route('/thank_you')  
def thank_you():
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template('thank_you.html', first=first,last=last)


@views.route("/register",methods=["GET","POST"])
def register():
    
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)                   

        db.session.add(user)
        db.session.commit()
        return redirect("views.login")
    return render_template("register.html", form=form)




#@app.route('/page/<int:page_id>') # Hovedmenyen
#def page(page_id):
#        return render_template('page.html', page=pages[page_id -1])
# Kan mend fordel dobbeltsjekkes med "flask routing exercise" - filmen.




# HOVED MENY - SIDER:
# 
# 
    
# HOME -siden
@views.route('/index')
#@login_required
def index():          
    return render_template('index.html') #pages=pages

# MYPROFILE -siden
#@views.route('/myprofile')  
#def myprofile():
 #   return render_template('myprofile.html') 

# UPLOAD -siden
@views.route('/upload') 
def upload():
    return render_template('upload.html') 

# MYFRIENDS -siden
@views.route('/myfriends')  
def myfriends():
    return render_template('myfriends.html') 


#@views.route('/users/<int:userspages_id>') # Husk at id-en for input username i registreringen heter "username"
#def username(userspages_id):
   # return render_template('users.html', usernumber = userspages[userspages_id - 1])

@views.route("/<username>")
def user_posts(username):
    page = request.args.get("page",1,type=int)
    user =  User.query.filter_by(username=username).first_or_404()
    post = Post.query.filter_by(author=user).order_by(Post.date.desc().pageinate(page=page,per_page=4))
    return render_template("myprofile.html")


    
@views.route("/myprofile",methods=["GET","POST"])
@login_required
def myprofile():
    form = UpdateUserForm()
    if form.validate_on_submit():

        if form.picture.data:
            username = current_user.username
            pic = add_profile_pic(form.picture.data,username)
            current_user.profile_image = pic
        
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()

        return redirect("views.myprofile")

    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email

    profile_image = url_for("static",filename="profile_pics/"+current_user.profile_image)
    return render_template("myprofile.html",profile_image=profile_image,form=form)







# Dropdown meny:

@views.route('/settings')  # SETTINGS
def settings():
    return render_template('settings.html') 

@views.route('/faq')  # FAQ
def faq():
    return render_template('index.html') 


@views.route('/logout')  # LOGOUT
def logout():
    logout_user()
    return redirect("views.login")


# Footer: group 27
@views.route('/group27')  # GROUP
def group27():
    return render_template('group27.html') 