from flask import Flask
from flask_cors import CORS, cross_origin
import apigather

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/')
@cross_origin(supports_credentials=True)
def hello():
    return apigather.return_player_stats()

@app.route('/<player_name>')
def hello1(player_name):
    return apigather.return_player_stats_by_name(str(player_name))

if __name__ == '__main__':
    app.run()
