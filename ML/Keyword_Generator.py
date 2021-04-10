#!/usr/bin/env python
# coding: utf-8
import spacy
import re
from collections import Counter
from string import punctuation
from PyDictionary import PyDictionary
dictionary=PyDictionary()
nlp = spacy.load('en_core_web_md')

def get_vocab():
    with open('Sample Data/Keywords.txt') as f:
        l=(f.readlines())
    vocab = []
    for it in l:
        if(len(it)>2):
            vocab.append(it.strip()[1:-2])
    return vocab



def get_hotwords(text):
    vocab = get_vocab()
    result = []
    for it in text:
        if it in vocab:
            result.append(it)
    pos_tag = ['PROPN', 'NOUN'] # extract proper nouns and nouns
    doc = nlp(text.lower()) # 2
  
    for token in doc:
        
        # skip if puntuation or stop word
        if(token.text in nlp.Defaults.stop_words or token.text in punctuation):
            continue
        # 4
        if(token.pos_ in pos_tag):
            result.append(token.text)
        
                
    return list(set(result))

def get_entities():
    entities={}
    doc = nlp(data)
    for entity in doc.ents:
        if(entity.label_ not in entities.keys()):
            entities[entity.label_] = []
            entities[entity.label_].append(entity)
        else:
            entities[entity.label_].append(entity)
    return(entities)


# In[5]:


def highlight_data(data):
    for it in data.split():
        if(it.lower() in keywords):
            bolded_string = "\033[1m" + it + "\033[0m"
            print(bolded_string,end= ' ')
        else:
            print(it,end=' ')







if __name__ == '__main__':
    data ='''
    Normalization is a process to eliminate the flaws of a database with bad design. A poorly designed database is inconsistent and create issues while adding, deleting or updating information.

    The following makes Database Normalization a crucial step in database design process −

    Resolving the database anomalies
    The forms of Normalization i.e. 1NF, 2NF, 3NF, BCF, 4NF and 5NF remove all the Insert, Update and Delete anomalies.

    Insertion Anomaly occurs when you try to insert data in a record that does not exist.

    Deletion Anomaly is when a data is to be deleted and due to the poor deign of database, other record also deletes.

    Eliminate Redundancy of Data
    Storing same data item multiple times is known as Data Redundancy. A normalized table do not have the issue of redundancy of data.

    Data Dependency
    The data gets stored in the correct table and ensures normalization.

    Isolation of Data
    A good designed database states that the changes in one table or field do not affect other. This is achieved through Normalization.

    Data Consistency
    While updating if a record is left, it can led to inconsistent data, Normalization resolves it and ensures Data Consistency.

    '''
    vocab = get_vocab()
    print(data)
    keywords = get_hotwords(data)
    keywords
    highlight_data(data)

