#python dependencies
import sys
import random

#third party dependencies
from flask import Flask 
from flask_restful import Resource, Api
import pandas as pd
import requests

#getting the headline

#Creating the API and defining functions

app = Flask(__name__)
api = Api(app)

def sentencescrambler(headline_argument):
    scrambled_sentence = ""
    for word in headline_argument.split():
        scrambled_sentence += wordmixer(word)
    return scrambled_sentence 

def wordmixer(word):
    charlst = list(word) 
    random.shuffle(charlst)
    new_word = ''.join(charlst)
    new_word += ' '
    return new_word


class Game_info(Resource):
    def get(self):

        whole_article = requests.get(url = 'https://newsapi.org/v2/top-headlines?country=gb&apiKey=e1d14d936ae24aa5b9a99e8ab7bed6e9')

        whole_article_json = whole_article.json()

        if len(sys.argv) > 1:
             headline = sys.argv[1]
        
        else:
            headline = whole_article_json["articles"][0]["title"]
        
       

        scrambled_sentence = sentencescrambler(headline)

        print(headline)
        print(scrambled_sentence)

        data = {'scrambled_headline': scrambled_sentence, "headline": headline}
        return data, 200, {'Access-Control-Allow-Origin': 'http://localhost:8000'}
    

    pass

api.add_resource(Game_info,'/Game_info')

if __name__ == '__main__':
    app.run()
