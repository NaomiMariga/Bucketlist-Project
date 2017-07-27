""" importing modules and functions from flask
"""
from flask import Flask, render_template, request, session, make_response, redirect
import os #for cryptographic functions
from models.bucketlist import Bucketlist
from models.user import User
import uuid


app = Flask(__name__)

Users = {}
app.secret_key = os.urandom(20)
bucketlists_dict= {}





@app.route('/register/', methods=['GET','POST'])
def register():
    """ redirects to the user registration page
    """
    if request.method == 'GET':
        return render_template('register.html')

    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
    Users[email] = [username,  email, password]
    print (Users)
        
    if Users[email]:
        return (render_template('index.html'), "Account created successfully")
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
        #session[email] = request.form['email','password']
        email = request.form['email']
        password = request.form['password']
        print(email, password, "User entered data")

        try:
            valid_email = Users[email][1]
            valid_pass = Users[email][-1]

            if email == valid_email and password == valid_pass:
                session['email'] = email
                return redirect('/create_bucket/')
        except KeyError:
            error = "Login was not successful"
            return render_template("index.html", error=error)


@app.route('/create_bucket/', methods=['GET', 'POST'])
def bucketcreate_view():
    """   redirects to the bucketlist page
    """
    if request.method == 'GET': 
        return render_template('bucketcreate_view.html')
    if request.method == 'POST':
        bucket_name = request.form.get('name')     
        print(bucket_name, "bucketlist name test")
        bucketlist_id = str(uuid.uuid1())
        bucketlist_object = Bucketlist(bucketlist_id, bucket_name)

        if session['email'] in bucketlists_dict:
            bucketlists_dict[session['email']].append(bucketlist_object)
        else:
            bucketlists_dict[session['email']] = []
            bucketlists_dict[session['email']].append(bucketlist_object)
        print(bucketlists_dict[session['email']], "testing bucketlist")
  
        

        # name_exist = bucketlist[bucket_name]
        # print (name_exist)
        # if bucket_name != name_exist:
        #     bucketlist[bucket_name] = bucket_name    
        return render_template('bucketcreate_view.html', buckets = bucketlists_dict[session['email']])             
        # else:
        #     error = "name already exists"
        #     return error
    
@app.route('/edit_bucket/<bucketlist_id>', methods=['POST'])
def edit_bucket(bucketlist_id):
    if request.method == 'POST':
        name_given = request.form.get('Edit_name')
        print (name_given , "This is edited bucket name")
        for bucket in bucketlists_dict[session['email']]:
            if bucketlist_id == bucket.bucketlist_id:
                bucket.bucket_name = name_given
             
        return render_template('bucketcreate_view.html', buckets = bucketlists_dict[session['email']])
    # try:
                
    #     bucketlist[bucket] = [name_given]       
    #     return render_template('bucketcreate_view.html', buckets = bucketlist)             
    # except KeyError:
    #     error = "name already exists"
    #     return render_template('bucketcreate_view.html', error = error) 
        
@app.route('/delete_bucket/<bucketlist_id>', methods=['POST'])
def delete(bucketlist_id):
    for bucket in bucketlists_dict[session['email']]:
        if bucketlist_id == bucket.bucketlist_id:
           bucketlists_dict[session['email']].remove(bucket)
        return render_template(
    'bucketcreate_view.html', buckets = bucketlists_dict[session['email']]
    )

@app.route('/activities/', methods=['GET'])
def bucketlist_activities():
    """  redirects to the bucketlist  activities
    """
    if request.method == 'GET':
        return render_template('bucketlist_activities.html')




if __name__ == "__main__":
    app.run(host='127.0.0.1', port='80')
