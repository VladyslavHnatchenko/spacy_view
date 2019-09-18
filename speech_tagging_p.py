"""Part of speech or POS is a grammatical role that explains how
a particular word is used in a sentence. """

import spacy
from spacy import displacy
from stop_words_p import about_doc


nlp = spacy.load("en_core_web_sm")

about_interest_text = ("He is interested in learning"
                       " Natural Language Processing.")

about_interest_doc = nlp(about_interest_text)
displacy.serve(about_interest_doc, style='dep')

# ------------------------------------------------------------------- #
# nouns = []
# adjectives = []
# for token in about_doc:
#     if token.pos_ == 'NOUN':
#         nouns.append(token)
#     if token.pos_ == 'ADJ':
#         adjectives.append(token)

# print(nouns, "\n")
# print(adjectives, "\n")

# for token in about_doc:
#     print(token, token.tag_, token.pos, spacy.explain(token.tag_))
