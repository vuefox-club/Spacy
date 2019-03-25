import spacy
nlp=spacy.load('en')
sent=input('Enter your sentence: ')
doc=nlp(sent)
for sent in doc.sents:
    print(sent)
