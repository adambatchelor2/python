from textblob import TextBlob

def getStrSentiment(textStr):

	blob = TextBlob(textStr)
	return blob.sentiment.polarity


str_to_test = "Does not offer free alcohol. Crowded place."

print (getStrSentiment(str_to_test))

 
