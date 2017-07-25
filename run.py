""" importing modules and functions from flask
"""
from flask import Flask, render_template, request, session, make_response

app = Flask(__name__)

Users = {}


@app.route('/register/', methods=['GET', 'POST'])
def register():
    """ redirects to the user registration page
    """
    if request.method == 'GET':
        return render_template('register.html')

    if request.method == 'POST':
        first_name = request.form.get('first_name')
        other_name = request.form.get('other_name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        username = request.form.get('username')
        password = request.form.get('password')
        
    Users[email] = [first_name, other_name, email, phone, username, password]
    print (Users)
        
    if Users[email]:
        return (render_template('register.html'), "Account created successfully")
    else:
        return "Problem was encountered creating account"

@app.route('/login/', methods=['GET', 'POST'])
def index():
    """ Redirects to the main/login page
    """
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        """
            user login authentication 
        """
        email = request.form.get('email')
        password = request.form.get('password')
        print(email, password)

        try:
            valid_email= Users[email]
            valid_pass = Users[email][-1]
            print(valid_email, valid_pass)
            if email == valid_email and password == valid_pass:
                session['user'] = valid_email
                return render_template('bucketcreate_view.html')
        except KeyError:
            error = "Login was not successful"
            return render_template("index.html", error=error)


@app.route('/', methods=['GET', 'POST'])
def bucketcreate_view():
    """   redirects to the bucketlist page
    """
    if request.method == 'POST': 
        return render_template('bucketcreate_view.html')


@app.route('/', methods=['GET'])
def bucketlist_activities():
    """  redirects to the bucketlist  activities
    """
    return render_template('bucketlist_activities.html')




if __name__ == "__main__":
    app.run(host='127.0.0.1', port ='80')

