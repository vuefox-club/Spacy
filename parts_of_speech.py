import spacy
nlp=spacy.load('en')
sent=input('Enter your sentence: ')
doc=nlp(sent)
print("We are vuefox")
for token in doc:
    print(token.text,token.tag_)
