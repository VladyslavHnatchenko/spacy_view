"""Rule-Based Matching Using spaCy"""

import spacy
from spacy.matcher import Matcher

from stop_words_p import about_doc

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)


def extract_full_name(nlp_doc):
    pattern = [{"POS": "PROPN"}, {"POS": "PROPN"}]
    matcher.add("FULL_NAME", None, pattern)
    matches = matcher(nlp_doc)
    for match_id, start, end in matches:
        span = nlp_doc[start:end]
        return span.text


extract_full_name(about_doc)