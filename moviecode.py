#PERFORM SENTIMental ANALYSIS ON MOVIES.CSV FILE
#IMPORTING LIBRARIES
import pandas as pd #TO READ EXCEL FILE

'''
STEP 1 
DATA EXTRACTION
'''

#READ THE CSV FILE
df=pd.read_csv(r"C:\Users\sejal\Downloads\movies.csv")


'''
STEP 2
DATA ANALYSIS
'''
#IMPORTING LIBRARIES
import nltk #TO PERFORM NLP OPERATIONS
from nltk.corpus import stopwords #TO REMOVE STOPWORDS

#PERFORMING SENTIMENTAL ANALYSIS
#Cleaning using Stop Words Lists
stop_words=set(stopwords.words('english'))

#Creating a dictionary of Positive and Negative words
positive_words=set()  
negative_words=set()
with open(r"C:\Users\sejal\Downloads\positive-words.txt") as f:
  for line in f:
    positive_words.add(line.strip())
with open(r"C:\Users\sejal\Downloads\negative-words.txt") as f:
  for line in f:
    negative_words.add(line.strip())

#INITIALISING VARIABLES FOR SENTIMENTAL ANALYSIS
positive_score=[]
negative_score=[]
polarity_score=[]
subjectivity_score=[]

#NUMBER OF SYLLABLES IN A WORD
def count_syllables(word):
  word=word.lower()
  if word.endswith(('es','ed')):
    return 0
  vowels='aeiou'
  count=0
  prev_char=None
  for char in word:
    if char in vowels and prev_char not in vowels:
      count+=1
    prev_char=char
  return count


#CALCULATING SENTIMENTAL ANALYSIS
for i in range(len(df)):
  

    #INITIALISING VARIABLES
    positive_word_count=0
    negative_word_count=0
    polarity=0
    subjectivity=0
    word_count=0
    syllable_count=0
    
    #TOKENIZING THE TEXT
'''
STEP 3
OUTPUT DATA STRUCTURE
'''
#CREATING A DATAFRAME WHICH INCLUDES ALL THE VARIABLES AND All INPUT VARIABLES IN THE INPUT FILE
data={'URL_ID':df['URL_ID'],
      'Positive Score':positive_score,
      'Negative Score':negative_score,
      'Polarity Score':polarity_score,
      'Subjectivity Score':subjectivity_score,
}

#SAVING THE OUTPUT DATA TO A CSV FILE OR EXCEL
df=pd.DataFrame(data)
df.to_csv(r'output.csv',index=False)







