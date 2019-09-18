"""Lemmatization is the process of reducing inflected forms of a word
while still ensuring that the reduced form belongs to the language.
This reduced form or root word is called a lemma."""

import spacy

nlp = spacy.load("en_core_web_sm")

conference_help_text = ("Gus is helping organize a developer"
                        " conference on Applications of Natural Language"
                        " Processing. He keeps organizing local Python meet-ups"
                        " and several internal talks at his workplace.")
conference_help_doc = nlp(conference_help_text)

for token in conference_help_doc:
    print(token, token.lemma_)
