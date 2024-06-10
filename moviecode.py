#PERFORM SENTIMENTAL ANALYSIS ON MOVIES.CSV FILE...THE title COLUMN IS USED FOR ANALYSIS
#IMPORTING LIBRARIES
import pandas as pd #TO READ EXCEL FILE

'''
STEP 1 
DATA EXTRACTION
'''
#READ THE CSV FILE
df=pd.read_csv(r"C:\Users\sejal\OneDrive\Documents\NOTES\python projects\movieanalysis\movies.csv")
df['keywords'] = df['keywords'].astype(str)

'''
STEP 2
DATA ANALYSIS
'''
#IMPORTING POSITIVE AND NEGATIVE WORDS
positive_words=set()  
negative_words=set()
with open(r"C:\Users\sejal\OneDrive\Documents\NOTES\python projects\movieanalysis\positive-words.txt") as f:
  for line in f:
    positive_words.add(line.strip())
with open(r"C:\Users\sejal\OneDrive\Documents\NOTES\python projects\movieanalysis\negative-words.txt") as f:
  for line in f:
    negative_words.add(line.strip())

#INITIALISING VARIABLES FOR SENTIMENTAL ANALYSIS
positive_score=[]
negative_score=[]
polarity_score=[]
subjectivity_score=[]

#PERFORMING SENTIMENTAL ANALYSIS
for i in range(len(df)):
    pos=0
    neg=0
    for word in df['title'][i].split():
        if word.lower() in positive_words:
            pos+=1
        if word.lower() in negative_words:
            neg+=1
    positive_score.append(pos)
    negative_score.append(neg)
    polarity_score.append((pos-neg)/(pos+neg+0.000001))
    subjectivity_score.append((pos+neg)/(len(df['title'][i].split())+0.000001))

    
'''
STEP 3
OUTPUT DATA STRUCTURE
'''
#CREATING A DATAFRAME WHICH INCLUDES ALL THE VARIABLES AND All INPUT VARIABLES IN THE INPUT FILE
data={'Index':df['index'],
      'Positive Score':positive_score,
      'Negative Score':negative_score,
      'Polarity Score':polarity_score,
      'Subjectivity Score':subjectivity_score}

#SAVING THE OUTPUT DATA TO A CSV FILE OR EXCEL
df=pd.DataFrame(data)
df.to_csv(r"C:\Users\sejal\OneDrive\Documents\NOTES\python projects\movieanalysis\output.csv",index=False)
print("success")