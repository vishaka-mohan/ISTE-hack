#!/usr/bin/env python
# coding: utf-8

#get_ipython().system('pip install wikipedia --quiet')
#get_ipython().system('pip install -U transformers==3.0.0 --quiet')
#get_ipython().system('python -m nltk.downloader punkt')
from ML.pipelines import pipeline
QGen = pipeline("question-generation")
MultiQGen= pipeline("multitask-qa-qg")
OnlyQ =  pipeline("e2e-qg")
import spacy
nlp = spacy.load('en_core_web_md')

def filter_length_answers(json_result):
    result = []
    for qa_pair in json_result:
        lenght_of_answer = len(qa_pair["answer"]) 
        if(lenght_of_answer> 50):
            continue
        result.append(qa_pair)
    return result


def ProcessQuestions(data):
    data.replace("\n", "")
    qs1 = QGen(data)
    result = json_result = filter_length_answers(qs1)
    return filter_length_answers(result)
   
  

def GetQuestionAnswer(json_result):
    json_result = ProcessQuestions(json_result)
    l=[]
    for idx, qa_pair in enumerate(json_result):
        l.append([qa_pair['question'],qa_pair['answer']])
    return l

def short_question_generation(data):
   
    questions = ProcessQuestions(data)
    #print(questions)
    short_answers=[]
    for item in questions:
        ans = item['answer']
        ans = nlp(ans)
        for entity in ans.ents:
          q_dict={}
          if(entity.label_=='PERSON'):
            question = "Who was "+str(entity)+" ?"
            answer = MultiQGen({
                "question": question,
                "context": data
            })
            #answer = str(entity) +" was the person "+item['question']
            q_dict['question']=question
            q_dict['answer']=answer
            short_answers.append(q_dict)

          elif entity.label_=='DATE':
            question = "What event occured in "+str(entity)+" ?"
            answer = MultiQGen({
                "question": question,
                "context": data
            })
            #answer =  str(entity) +" was the time period "+item['question']
            q_dict['question']=question
            q_dict['answer']=answer
            short_answers.append(q_dict)

          elif entity.label_=='ORG' or entity.label_=='GPE':
            question = "What event occured in "+str(entity)+" ?"
            answer = MultiQGen({
                "question": question,
                "context": data
            })
            #answer =  str(entity) +" was the time period "+item['question']
            q_dict['question']=question
            q_dict['answer']=answer
            short_answers.append(q_dict)
          
    return short_answers

if __name__ == '__main__':

    data='''The two characteristic features seen in carbon, that is, tetravalency and catenation, put
    together give rise to a large number of compounds. Many have the same non-carbon
    atom or group of atoms attached to different carbon chains. These compounds were
    initially extracted from natural substances and it was thought that these carbon
    compounds or organic compounds could only be formed within a living system. That is,
    it was postulated that a ‘vital force’ was necessary for their synthesis. Friedrich Wöhler
    disproved this in 1828 by preparing urea from ammonium cyanate. But carbon
    compounds, except for carbides, oxides of carbon, carbonate and hydrogencarbonate
    salts continue to be studied under organic chemistry'''


    data2='''
    The Indian independence movement was a series of historic events with the ultimate aim of ending the British rule in India. The movement spanned from 1857 to 1947.[1] The first nationalistic revolutionary movement for Indian independence emerged from Bengal.[2] It later took root in the newly formed Indian National Congress with prominent moderate leaders seeking only their fundamental right to appear for Indian Civil Service examinations in British India, as well as more rights (economical in nature) for the people of the soil. The early part of the 20th century saw a more radical approach towards political self-rule proposed by leaders such as the Lal Bal Pal triumvirate, Aurobindo Ghosh and V. O. Chidambaram Pillai.[3]
    The last stages of the self-rule struggle from the 1920s was characterized by Congress's adoption of Mahatma Gandhi's policy of non-violence and civil disobedience, and several other campaigns. Nationalists like Subhas Chandra Bose, Bhagat Singh, Bagha Jatin, Surya Sen preached armed revolution to achieve self-rule. Poets and writers such as Rabindranath Tagore, Subramania Bharati, Bankim Chandra Chattopadhyay and Kazi Nazrul Islam used literature, poetry, and speech as a tool for political awareness. Feminists like Sarojini Naidu, Pritilata Waddedar, Begum Rokeya promoted the emancipation of Indian women and their participation in national politics.[3] B. R. Ambedkar championed the cause of the disadvantaged sections of Indian society within the more significant self-rule movement.[4] The period of the World War II saw the peak of the campaigns by the Quit India Movement led by Congress and the Indian National Army movement led by Subhas Chandra Bose with the help of Japan
    '''


    data3 = '''
    A condition that occurs when two processes are each waiting for the other to complete before proceeding. The result is that both processes hang. Deadlocks occur most commonly in multitasking and client/server environments. Ideally, the programs that are deadlocked, or the operating system, should resolve the deadlock, but this doesn't always happen. A deadlock is also called a deadly embrace.

    The cause of deadlocks: Each process needing what another process has. This results from sharing resources such as memory, devices, links.

    In an operating system, a deadlock is a situation which occurs when a process or thread enters a waiting state because a resource requested by it is being held by another waiting process, which in turn is waiting for another resource. If a process is unable to change its state indefinitely because the resources requested by it are being used by another waiting process, then the system is said to be in a deadlock.
    '''
    questions = ProcessQuestions(data)
    GetQuestionAnswer(questions)
    short_answers = short_question_generation(data)
    GetQuestionAnswer(short_answers)
    short_answers = short_question_generation(data3)
    print(short_answers)
    OnlyQ(data)

