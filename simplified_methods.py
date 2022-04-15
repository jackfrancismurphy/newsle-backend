import requests
import random

whole_article = requests.get(url = 'https://newsapi.org/v2/top-headlines?country=gb&apiKey=e1d14d936ae24aa5b9a99e8ab7bed6e9')

whole_article_json = whole_article.json()

#real code

#headline = whole_article_json["articles"][0]["title"]

#for now code 

headline = "Boris Johnson says tens of thousands could be sent to Rwanda under relocation plan for asylum seekers – UK politics live - The Guardian"

scrambled_string = ""

# below is the scrambler which needs fixing 

def wordmixer(word):
    new_word = ""
    charlst = list(word) 
    random.shuffle(charlst)
    new_word = ''.join(charlst)
    return dash_eradicator(new_word)

def dash_eradicator(word):
    new_word = word
    new_word += ' '
    for letter in word:
        if not letter.isalnum():
            new_word = word.replace(letter, " ")
    return new_word


def sentencescrambler(headline_argument):
    scrambled_sentence = ""
    alnum_headline = ""
    for word in headline_argument.split():
        scrambled_sentence += wordmixer(word)
        alnum_headline += dash_eradicator(word)
    return scrambled_sentence, alnum_headline




""" def misc_eradicator(test_sentence):

    for i in range(len(test_sentence)):
        test_sentence[i] = test_sentence[i].replace("-", " ").replace("'", "")
    print(f"are there dashes and such in here? {test_sentence}")
    return test_sentence
 """
(scrambled_sentence, final_headline) = sentencescrambler(headline)

print("\nThis is headline")
print(final_headline)

#why does the above still have dashes and such in it???

print("\nThis is scrambled sentence")
print(scrambled_sentence)

player_guess = "says"

""" if player_guess in final_headline.split():
    guess_position = final_headline.split().index(player_guess)
    test_ssentence = scrambled_sentence.split()
    test_ssentence[guess_position] = player_guess
    print(test_ssentence)
    #scrambled_sentence[guess_position] = player_guess """

#print(scrambled_sentence)

def word_replacer(current_sentence, headline, player_guess):
    if player_guess in headline.split():
        guess_position = headline.split().index(player_guess)
        updated_position = current_sentence.split()
        updated_position[guess_position] = player_guess
        print(updated_position)
        return " ".join(updated_position)

#test 

scrambled_sentence = word_replacer(scrambled_sentence, headline, player_guess)

print(f"This is the scrambled sentence: {scrambled_sentence}")