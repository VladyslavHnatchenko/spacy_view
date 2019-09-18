"""Stop words are the most common words in a language. In the
English language, some examples of stop words are the, are, but, and they. """

import spacy

nlp = spacy.load("en_core_web_sm")


spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
# print(len(spacy_stopwords))

# for stop_word in list(spacy_stopwords)[:10]:
#     print(stop_word)

about_text = ("Gus Proto is a Python developer currently"
              " working for a London-based Fintech"
              " company. He is interested in learning"
              " Natural Language Processing.")
about_doc = nlp(about_text)
about_no_stop_word_doc = [token for token in about_doc if not token.is_stop]
print(about_no_stop_word_doc)

# for token in about_doc:
#     if not token.is_stop:
#         print(token)
