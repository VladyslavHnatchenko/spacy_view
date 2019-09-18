import spacy
from spacy.matcher import Matcher


nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)
conference_org_text = ("There is a developer conference"
                       " happening on 21 July 2019 in London.It is titled "
                       " 'Applications of Natural Language Processing'."
                       " There is a helpline number available"
                       " at (123) 456-789")


def extract_phone_number(nlp_doc):
    pattern = [{'ORTH': '('}, {'SHAPE': 'ddd'},
               {'ORTH': ')'}, {'SHAPE': 'ddd'},
               {'ORTH': '-', 'OP': '?'},
               {'SHAPE': 'ddd'}]
    matcher.add('PHONE_NUMBER', None, pattern)
    matches = matcher(nlp_doc)
    for match_id, start, end in matches:
        span = nlp_doc[start:end]
        return print(span.text)


conference_org_doc = nlp(conference_org_text)
extract_phone_number(conference_org_doc)
