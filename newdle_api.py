from flask import Flask 
from flask_restful import Resource, Api
import pandas as pd

app = Flask(__name__)
api = Api(app)

class Game_info(Resource):
    def get(self):
        data = {'scrambled_headline': "Bggteis euseezq rof ipuclb otserc ypa in 02 eayrs BBC com", "headline": "Biggest squeeze for public sector pay in 20 years BBC com"}
        return {'data': data}, 200
    
    pass

api.add_resource(Game_info,'/Game_info')

if __name__ == '__main__':
    app.run() 