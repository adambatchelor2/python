# Import libraries
import csv
import pandas as pd

from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier

from googletrans import Translator
translator = Translator()
from pathlib import Path

# CSV files
data_folder = Path("C:/Users/adam.batchelor/Desktop/")
file_to_open = data_folder / "train5.csv"

comments = 'O:\\10. Workspace\DI Jiras\DI-670  Improve sentiment scoring of rating comments and deliver insights\Sushma\\csv comments_280720.csv'

# list for sentiment score
out_list = []
# list for translated comment
#trans_list = []

# Reading from training files
with open(file_to_open, 'r', encoding="utf8") as f:
    text = list(csv.reader(f))

cl = NaiveBayesClassifier(text)

# reading comments - insert new every run
df = pd.read_csv(comments)

# writing output to csv - with sentiment,score and translation
for index, row in df.iterrows():
    translation = translator.translate(row['review_comment'], dest="en")
    line = translation.text
    prob_dist = cl.prob_classify(TextBlob(line, classifier=cl))
    # print(line + str((prob_dist.prob("pos"))) + '\n')
   # trans_list.append(line) #purpose of this?

    out_list.append(round(5 * (prob_dist.prob("pos")), 1))

df["sentiment_score"]= out_list

print(df)
    #writer.writerow({'comment': row['review_comment'], 'translation': line, 'sentiment': cl.classify(line),
    #                'score': round(5 * (prob_dist.prob("pos")), 1)})

# cl.show_informative_features(5)
# print(cl.accuracy(text))

