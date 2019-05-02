import nltk
import string
pre=''
sum1=0
pos=[]
#from win32com.client import Dispatch
counter = 1
croppedResponse = ' '
#speak = Dispatch("SAPI.SpVoice")
path='chat.txt'
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
from sentence_corps_1 import training_data
corpus_words = {}
class_words = {}
classes = list(set([a['class'] for a in training_data]))
for c in classes:
    class_words[c] = []
for data in training_data:
    for word in nltk.word_tokenize(data['sentence']):
        if word not in ["?", "'s"]:
            stemmed_word = stemmer.stem(word.lower())
            if stemmed_word not in corpus_words:
                corpus_words[stemmed_word] = 1
            else:
                corpus_words[stemmed_word] += 1
            class_words[data['class']].extend([stemmed_word])


def calculate_class_score(sentence, class_name, show_details=True):
    score = 0
    for word in nltk.word_tokenize(sentence):
        if stemmer.stem(word.lower()) in class_words[class_name]:
            score += (1 / corpus_words[stemmer.stem(word.lower())])
    return score 
def classify(sentence):
    high_class = None
    high_score = 0
    for c in class_words.keys():
        score = calculate_class_score(sentence, c, show_details=False)
        if score > high_score:
            high_class = c
            high_score = score

    return high_class, high_score
lines = [line.rstrip('\n') for line in open('lyrics.txt')]
n=len(lines)
for i in range(n):    
    sentence=lines[i]
    if(pre!=sentence):
        answer,prob=classify(sentence)
        #print(sentence)
        #print(prob)
        #print(answer)
        #speak.Speak(answer)
        if(answer!="positive"):
            sum1=sum1+1
            pos.append(lines[i])
 

print("positive sentences are: ",sum1)
print("total sentences are: ",len(lines))
fh=open('filter.txt','w')
for i in range(len(pos)):
    fh.write(pos[i])
    fh.write(' \n')
fh.close()
          
