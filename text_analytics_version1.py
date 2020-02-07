from textblob import TextBlob
# import re

def translateString(textStr):

	try: #if english error handle
		return textStr.translate(from_lang=textStr.detect_language(), to='en')
	except:
		return textStr


def strCorrect(textStr):

	textStr = textStr.correct() #attempts to correct spelling
	# need to add text cleansing
	return textStr 

def fixString(textStr):

	textStr = TextBlob(textStr) #create text blob
	textStr = translateString(textStr) #call translate function
	textStr = strCorrect(textStr) #call text cleanse
	return textStr

def getStrSentiment(textStr): 

    textStr = fixString(textStr) #clean string
    return textStr.sentiment.polarity # return sentiment 


# str_to_test = "ce salon est sale"
str_to_test = "i wish i was anywhere else in the world - stinks, service is awful"
# str_to_test = "wow this is really nice i love it"

print('Sentence: '+str(fixString(str_to_test))+'    Sentiment: '+str(getStrSentiment(str_to_test)))

