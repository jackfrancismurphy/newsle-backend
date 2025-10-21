import newsle_api

# Scramble a word 100 times and make sure it's never the original word
def test_word_mixer_not_original():
    word = "headline"
    for _ in range(100):
        scrambled_word = newsle_api.wordmixer("headline")
        assert word + ' ' != scrambled_word

# Scramble a sentance 100 times and make sure it's never the original word
def test_sentencescrambler_not_original():
    sentance = "This is a news headline"
    for _  in range(100):
        scrambled_sentance = newsle_api.sentencescrambler(sentance)
        assert sentance != scrambled_sentance
