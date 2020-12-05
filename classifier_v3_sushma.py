import csv
import pandas as pd

from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
#from googletrans import Translator

translator = Translator()
training = 'O:\\10. Workspace\DI Jiras\DI-670  Improve sentiment scoring of rating comments and deliver insights\Sushma\\train2.csv'
comments = 'O:\\10. Workspace\DI Jiras\DI-670  Improve sentiment scoring of rating comments and deliver insights\Sushma\\csv comments.csv'
out_list = [] #list for sentiment score

with open(training, 'r', encoding="utf8") as f:
    text = list(csv.reader(f))

cl = NaiveBayesClassifier(text)

with open(comments, 'r', encoding="utf8") as f:
    data = f.readlines()

df = pd.read_csv(comments) #changed to data frame as this is what Alteryx uses

for index, row in df.iterrows():
    #if len(row['review_comment']) > 0: #removed as assume only rows with comments are fed in
    prob_dist = cl.prob_classify(TextBlob(row['review_comment'], classifier=cl))
    print(row['review_comment']+str((prob_dist.prob("pos"))))
    out_list.append(round(5 * (prob_dist.prob("pos")), 1))

df["sentiment_score"] = out_list

