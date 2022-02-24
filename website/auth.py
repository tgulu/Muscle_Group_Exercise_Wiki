from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods =['GET', 'POST'])
def login():
    
    return render_template("login.html")

@auth.route('/logout')
def Logout():
    return "<p>Log Out</p>"  


@auth.route('/sign-up', methods =['GET', 'POST'])
def sign_up():
        if request.method == 'POST':
            
            email = request.form.get('email')
            firstname = request.form.get('firstname')
            lastname  = request.form.get('lastname')
            password1 = request.form.get('password1')
            password2 =request.form.get('password2')
            print(email)
            


            if len(email) < 4:
                flash('Email must be greater than 4 characters.', category='error')
            elif len(firstname) < 1:
                flash('First Name must be greater than 1 character.', category='error')
            elif len(lastname) < 1:
                flash('Last Name must be greater than 1 character.', category='error')
            elif password1 != password2:
                flash('Passwords don\'t match.', category='error')
            elif len(password1) < 7:
                flash('Password must be at least 7 characters.', category='error')
            else:
                flash('Account created!', category='success')
                
                
        return render_template("sign_up.html")


@auth.route('/upper-body')
def upper_body():
    return render_template("upper_body.html")