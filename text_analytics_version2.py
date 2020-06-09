from textblob import TextBlob

def getStrSentiment(textStr):

	blob = TextBlob(textStr)
	print (blob.detect_language())
	# try: #if english error handle
		
	# 	texteng = textStr.translate(from_lang=textStr.detect_language(), to='en')
	# 	print (texteng)
	# 	return texteng.sentiment.polarity
	# except:
	# 	print ("Except")
	# 	return textStr.sentiment.polarity


str_to_test = "je suis" #0.07 old method - 0.089 new lrd100027

print (getStrSentiment(str_to_test))

from textblob import TextBlob
 
