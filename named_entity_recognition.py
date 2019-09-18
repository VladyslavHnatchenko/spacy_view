"""Named Entity Recognition."""

import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")
survey_text = "Out of 5 people surveyed, James Robert, Julie Fuller" \
              " and Benjamin Brooks like apple Kelly Cox and" \
              " Matthew Evans like oranges."


def replace_person_names(token):
    if token.ent_iob != 0 and token.ent_type_ == 'PERSON':
        return '[REDACTED]'
    return token.string


def redact_names(nlp_doc):
    for ent in nlp_doc.ents:
        ent.merge()
    tokens = map(replace_person_names, nlp_doc)
    return ''.join(tokens)


survey_doc = nlp(survey_text)
print(redact_names(survey_doc))

# ------------------------------------------------------------------- #
# piano_class_text = ("Great Piano Academy is situated"
#                     " in Mayfair or the city of London and has"
#                     " world-class piano instructors.")
# piano_class_doc = nlp(piano_class_text)
#
# for ent in piano_class_doc.ents:
#     print(ent.text, ent.start_char, ent.end_char,
#           ent.label_, spacy.explain(ent.label_))
#
# displacy.serve(piano_class_doc, style='ent')
