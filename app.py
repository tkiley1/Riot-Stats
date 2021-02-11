from flask import Flask, render_template, flash, request, redirect, url_for
from flask_cors import CORS, cross_origin
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired
import os

DIFFICULTY = {'Tuesday': 1, 'Thursday': 2, 'Saturday': 3, 'Death by Beerio-Kart': 4}
headers = ['Track', 'Game', 'Test']
races = [[1,1,0],[2,4,1],[3,9,2],[4,16,3]]
app = Flask(__name__)
CORS(app, support_credentials=True)
Bootstrap(app)

class ReusableForm(FlaskForm):
    name = StringField('Name:', validators=[DataRequired()])
    choice_level = RadioField('Difficulty', choices=['Tuesday', 'Thursday', 'Saturday', 'Death by Beerio-Kart'])
    submit = SubmitField('Submit')


#class RadioForm(FlaskForm):

app.secret_key = os.urandom(12)
#Temporary home page
@app.route('/', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def hello():
    names = ReusableForm()
    message = ''
    if names.validate_on_submit():
        players = str(names.name.data).split(',')
        difficulty = DIFFICULTY[str(names.choice_level.data)]
        message = str(names.name.data) + " is bad at Mario Kart.\nYou have chosen the " + str(names.choice_level.data) + " difficulty."
    else:
        message = "Please enter a name."


    return render_template('index.html', form=names, message=message, races=races, headers=headers)

#Dynamic player info page
#@app.route('/<player_name>')
#def hello1(player_name):
#    return apigather.return_player_stats_by_name(str(player_name))

#Test home page
@app.route('/home')
def generate_table():
    return "Mario Time!"

if __name__ == '__main__':
    app.run(host= '0.0.0.0')
