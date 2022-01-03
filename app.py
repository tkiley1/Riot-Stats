from flask import Flask
from flask_cors import CORS, cross_origin
import apigather

app = Flask(__name__)
CORS(app, support_credentials=True)

#Temporary home page
@app.route('/')
@cross_origin(supports_credentials=True)
def hello():
    return 'Team InVade.GG'

#Dynamic player info page
@app.route('/lookup/<player_name>')
def hello1(player_name):
    return apigather.return_player_stats_by_name(str(player_name))

#Test home page
@app.route('/home')
def generate_table():
    return apigather.return_home_page_stats()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
