import spacy
from spacy import displacy
from spacy_udpipe.language import load_from_path

nlp = load_from_path('ru-syntagrus', 'C:\\Users\\Oleg_Durandin\\Documents\\Research\\UDAuthorStyle\\UDModels\\russian-syntagrus-ud-2.4-190531.udpipe')


doc_example = nlp(" И каждый раз молодой человек, проходя мимо, чувствовал какое-то болезненное и трусливое ощущение, которого стыдился и от которого морщился.")
for token in doc_example:
    print(token.text, token.lemma_, token.pos_, token.dep_, token.tag_)