'''You need to submit one example project in PDF extraction and 
relevant text categorized and stored in CSV/text with appropriate tags/labels.'
the pdf used is sample.pdf 
'''
import PyPDF2
import nltk
import csv
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

#extracting text from pdf
def extract_text(page):
  text_content = ""
  text_objects=page.extract_text().splitlines()
  for line in text_objects:
    text_content+=line+" "
  return text_content.strip()

#creating a function for sentiment analysis
def sentiment_analysis(text):
  sentiment_analyzer=SentimentIntensityAnalyzer()
  sentiment_score=sentiment_analyzer.polarity_scores(text)['compound']
  return sentiment_score

#opening the pdf file and extracting the text
pdf_file=open(r'C:\Users\sejal\OneDrive\Documents\NOTES\python projects\movieanalysis\Untitled document.pdf', 'rb')
pdf_read=PyPDF2.PdfReader(pdf_file)
page=pdf_read.pages[0]
text=extract_text(page)


#performing sentiment analysis on the extracted text
if len(text)>0:
  sentiment_score=sentiment_analysis(text)
  if sentiment_score>=0.05:
    sentiment_label='Positive'
  elif sentiment_score<=-0.05:
    sentiment_label='Negative'
  else:
    sentiment_label='Neutral'
 

#creating a dictionary to store the extracted text, sentiment score and sentiment label
data={"Text":text, 
      "Sentiment Score":sentiment_score, 
      "Sentiment Label":sentiment_label
      }

#csv file to store
with open(r'C:\Users\sejal\OneDrive\Documents\NOTES\python projects\movieanalysis\sentiment_score.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(data.keys())
  writer.writerow(data.values())

file=r"C:\Users\sejal\OneDrive\Documents\NOTES\python projects\movieanalysis\sentiment_score.csv"
#closing the pdf file
pdf_file.close()

print("Text extracted from the PDF file: ", text)
print("Sentiment Score: ", sentiment_score)
print("Sentiment Label: ", sentiment_label)
print(f"Data stored in CSV file: {file}")
print("CSV file created successfully!")
