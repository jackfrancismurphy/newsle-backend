#python dependencies
import sys
import random

#third party dependencies
from flask import Flask 
from flask_restful import Resource, Api
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
    charlst.replace('‘', "'").replace('’', "'").replace('“',"\"").replace('”',"\"")   
    random.shuffle(charlst)
    new_word = ''.join(charlst)
    new_word += ' '
    return new_word


class Game_info(Resource):
    def get(self):

        JSON_object = requests.get('https://content.guardianapis.com/search?api-key=5ae53b78-a100-42ea-9d0c-262ed4d181bc')

        #Randomising headlines as this is now from one website;
        #A website which my friends commonly read.
        headline_list = [x["webTitle"] for x in JSON_object.json()['response']['results']]
    
        headline = headline_list[random.randint(0, len(headline_list))]

        scrambled_sentence = sentencescrambler(headline)

        data = {'scrambled_headline': scrambled_sentence, "headline": headline}
        return data, 200, {'Access-Control-Allow-Origin':'*'}
    
    pass

api.add_resource(Game_info,'/Game_info')
