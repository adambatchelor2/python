from textblob import TextBlob
# import re

def translateString(textStr):

	textStr = TextBlob(textStr)
	try: #if english error handle
		return textStr.translate(from_lang=textStr.detect_language(), to='en')
	except:
		return textStr


def getStrSentiment(textStr): 

    textStr = translateString(textStr) #clean string
    print(textStr)
    return textStr.sentiment.polarity # return sentiment 

str_to_test = "je suis un chat" #0.07 old method - 0.089 new lrd100027

print (translateString(str_to_test))
print (getStrSentiment(str_to_test))


