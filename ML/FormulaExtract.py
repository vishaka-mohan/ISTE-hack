from chemdataextractor import Document
import re
from summarizer import Summarizer

def chemData(text):
  
  doc = Document(text)
  #abbreviations - list of tuples - first element of each tuple is the abbreviation , second uska full form and third element is CM if it is chemical mention else it is None
  abbreviations = doc.abbreviation_definitions 
  #chemical entity mention - just a list of chemistry terms in the text
  chemMentions = doc.cems
  l=[]
  for item in chemMentions:
        l.append(str(item))
  return list(set(l))

def GetFormula(text):
      generalPattern=r'([^\n]+=[^\n]+[^\s])'
      l =  re.findall(generalPattern, text)
      return l
    

def summary(text):
  model = Summarizer()
  result = model(text, min_length=60)
  full = ''.join(result)
  #return type is string
  return full

