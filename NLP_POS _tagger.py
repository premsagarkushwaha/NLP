#you should have installed nltk library in your PC/Laptop.(use "pip install nltk")
#you should have installed pandas library in your PC/Laptop.(use "pip install pandas")


# importing Library
import nltk
from nltk import word_tokenize
from nltk import StanfordTagger
import pandas as pd

#Defining function that accept a tokenized list of string and return a dataframe of word with description of pos tag.
def getdetail(li):
    
    
    pos_dict = {
    'CC': 'coordinating conjunction','CD': 'cardinal digit','DT': 'determiner',
    'EX': 'existential there (like: \"there is\" ... think of it like \"there exists\")',
    'FW': 'foreign word','IN':  'preposition/subordinating conjunction','JJ': 'adjective \'big\'',
    'JJR': 'adjective, comparative \'bigger\'','JJS': 'adjective, superlative \'biggest\'',
    'LS': 'list marker 1)','MD': 'modal could, will','NN': 'noun, singular \'desk\'',
    'NNS': 'noun plural \'desks\'','NNP': 'proper noun, singular \'Harrison\'',
    'NNPS': 'proper noun, plural \'Americans\'','PDT': 'predeterminer \'all the kids\'',
    'POS': 'possessive ending parent\'s','PRP': 'personal pronoun I, he, she',
    'PRP$': 'possessive pronoun my, his, hers','RB': 'adverb very, silently,',
    'RBR': 'adverb, comparative better','RBS': 'adverb, superlative best',
    'RP': 'particle give up','TO': 'to go \'to\' the store.','UH': 'interjection errrrrrrrm',
    'VB': 'verb, base form take','VBD': 'verb, past tense took',
    'VBG': 'verb, gerund/present participle taking','VBN': 'verb, past participle taken',
    'VBP': 'verb, sing. present, non-3d take','VBZ': 'verb, 3rd person sing. present takes',
    'WDT': 'wh-determiner which','WP': 'wh-pronoun who, what','WP$': 'possessive wh-pronoun whose',
    'WRB': 'wh-abverb where, when','QF' : 'quantifier, bahut, thoda, kam (Hindi)','VM' : 'main verb',
    'PSP' : 'postposition, common in indian langs','DEM' : 'demonstrative, common in indian langs'
    }
    
    # tagging POS with each word
    pos_tagged = nltk.pos_tag(li)
    
    word,pos=zip(*pos_tagged)
    detail = {'words':[],'POS':[],'description':[]}
    for i in range(len(word)):
        if pos[i] in pos_dict.keys():
            detail['words'].append(word[i])
            detail['POS'].append(pos[i])
            detail['description'].append(pos_dict[pos[i]])
        else :
            detail['words'].append(word[i])
            detail['POS'].append(pos[i])
            detail['description'].append('NA')
    return pd.DataFrame(detail)
  
  
  # tokenizing a string
  text_toks = nltk.word_tokenize("Just a small snippet of  my text.")
  
  # passing list to the function
  getdetail(text_toks)
