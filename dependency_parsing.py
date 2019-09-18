"""Dependency Parsing Using spaCy."""

import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

piano_text = "Gus is learning piano"
piano_doc = nlp(piano_text)

for token in piano_doc:
    print(token.text, token.tag_, token.head.text, token.dep_)

displacy.serve(piano_doc, style='dep')
