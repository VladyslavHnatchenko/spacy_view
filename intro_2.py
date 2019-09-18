import re
import spacy

from spacy.tokenizer import Tokenizer


custom_nlp = spacy.load("en_core_web_sm")

prefix_re = spacy.util.compile_prefix_regex(custom_nlp.Defaults.prefixes)
suffix_re = spacy.util.compile_prefix_regex(custom_nlp.Defaults.suffixes)
infix_re = re.compile(r'''[-~]''')

about_text = ("Gus Proto is a Python developer currently"
              " working for a London-based Fintech"
              " company. He is interested in learning"
              " Natural Language Processing.")


def customize_tokenizer(nlp):
    # Adds support to use '-' as the delimiter for tokenization
    return Tokenizer(nlp.vocab,
                     prefix_search=prefix_re.search,
                     suffix_search=suffix_re.search,
                     infix_finditer=infix_re.finditer,
                     token_match=None
                     )


custom_nlp.tokenizer = customize_tokenizer(custom_nlp)
customize_tokenizer_about_doc = custom_nlp(about_text)
print([token.text for token in customize_tokenizer_about_doc])
