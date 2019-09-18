"""Preprocessing Functions."""

import spacy

from word_frequency_p import complete_doc

nlp = spacy.load("en_core_web_sm")


def is_token_allowed(token):
    """Only allow valid tokens which are not stop words and punctuation symbols."""
    if (not token or not token.string.strip() or
            token.is_stop or token.is_punct):
        return False
    return True


def pre_process_token(token):
    # Reduce token to its lowercase lemma from
    return token.lemma_.strip().lower()


complete_filtered_tokens = [pre_process_token(token)
                            for token in complete_doc if is_token_allowed(token)]
print(complete_filtered_tokens)
