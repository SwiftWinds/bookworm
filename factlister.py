import spacy
import en_core_web_md
import textacy.extract

def eventLister(text, subject):
    # Load the large English NLP model
    nlp = en_core_web_md.load()

    # Parse the document with spaCy
    doc = nlp(text)

    # Extract semi-structured statements
    statements = textacy.extract.semistructured_statements(doc, subject)

    # Return the results
    str = "Here are the things I know about " + subject + ":"

    for statement in statements:
        subject, verb, fact = statement
        str +=f"\n - {fact}"

    return str
