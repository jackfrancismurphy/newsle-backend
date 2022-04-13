from flask import Flask 
from flask_restful import Resource, Api
import pandas as pd
import requests
#getting the headline

#Creating the API

app = Flask(__name__)
api = Api(app)

class Game_info(Resource):
    def get(self):
        whole_article = requests.get(url = 'https://newsapi.org/v2/top-headlines?country=gb&apiKey=e1d14d936ae24aa5b9a99e8ab7bed6e9')

        whole_article_json = whole_article.json()

        headline = whole_article_json["articles"][0]["title"]
        
        data = {'scrambled_headline': "Bggteis euseezq rof ipuclb otserc ypa in 02 eayrs BBC com", "headline": headline}
        return {'data': data}, 200
    
    pass

api.add_resource(Game_info,'/Game_info')

if __name__ == '__main__':
    app.run()