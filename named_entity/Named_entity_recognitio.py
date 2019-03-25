import spacy
from spacy import displacy
nlp=spacy.load('en')
sent=input('Enter your sentence: ')
doc=nlp(sent)
for ent in doc.ents:
    print(ent.text,ent.label_)
displacy.render(doc,style='ent',jupyter=False)
doc1 = nlp('I am going to publish a journal on machine learning in security tommorrow')

for token in doc1:
    print("{0}/{1} <--{2}-- {3}/{4}".format(
        token.text, token.tag_, token.dep_, token.head.text, token.head.tag_))
