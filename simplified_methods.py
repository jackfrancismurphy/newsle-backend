import requests
import random

whole_article = requests.get(url = 'https://newsapi.org/v2/top-headlines?country=gb&apiKey=e1d14d936ae24aa5b9a99e8ab7bed6e9')

whole_article_json = whole_article.json()

headline = whole_article_json["articles"][0]["title"]

scrambled_string = ""

# below is the scrambler which needs fixing 

def wordmixer(word):
    new_word = ""
    charlst = list(word) 
    random.shuffle(charlst)
    new_word = ''.join(charlst)
    new_word += ' '
    for letter in word:
        if not letter.isalnum():
            new_word = word.replace(letter, " ")
    return new_word


def sentencescrambler(headline_argument):
    scrambled_sentence = ""
    #Line 29 creates both the headline and the scrambled sentence
    #without dashes and apostrophes in there  
    alnum_headline = misc_eradicator(headline_argument.split()) 
    for word in alnum_headline:
        scrambled_sentence += wordmixer(word)
    return scrambled_sentence, " ".join(alnum_headline)


def misc_eradicator(test_sentence):

    for i in range(len(test_sentence)):
        test_sentence[i] = test_sentence[i].replace("-", " ").replace("'", "")
    
    return test_sentence

scrambled_sentence = (sentencescrambler(headline))[0]
final_headline = (sentencescrambler(headline))[1]

print("\nThis is headline")
print(final_headline)

#why does the above still have dashes and such in it???

print("\nThis is scrambled sentence")
print(scrambled_sentence)

