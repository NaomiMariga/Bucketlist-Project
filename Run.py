from flask import Flask
from models.user import User
from models.bucketlist import Bucketlist
from models.activity import Activity 

app = Flask('bucketlist', template_folder="templates", static_folder="static")
login = User()


@app.route('/app/models/user')

app.run()
app.debug = True
app.run()