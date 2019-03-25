import spacy

nlp = spacy.load('en')  # make sure to use larger model!
sent=input('Enter your sentence: ')
tokens = nlp(sent)

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
