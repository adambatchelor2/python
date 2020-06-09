from textblob import TextBlob

def getStrSentiment(textStr):

	blob = TextBlob(textStr)
	return blob.sentiment.polarity


str_to_test = "The lounge was clean, the staff polite and very professional (nicely dressed) and the space provided was comfortable, relaxing and it felt inviting" #0.07 old method - 0.089 new lrd100027

print (getStrSentiment(str_to_test))

 
