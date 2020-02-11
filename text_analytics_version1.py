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


#str_to_test = "ce salon est sale" #example

#old range 0 to 1 and new range -1 to 1
#str_to_test = "The free airport Wifi was faster than the lounge's" #0.96 old method - 0.4 new lrd100012
#str_to_test = "Too cramped" #0.04 old method - 0.0 new lrd100016
#str_to_test = "Too small. Food options lacking. Only drinks behind unstaffed bar. Disappointed" #0.04 old method - -0.14 new lrd100021
#str_to_test = "This lounge needs improvements, since it is not up to the standards clients would expect from a JFK lounge." #0.5 old method - 0.0 new lrd100022
#str_to_test = "Food is extremely limited & not at all appetising, stale sandwiches, 2 types of pastries thats pretty much it & very poor. Staff on the front desk was miserable without even a Hello on entering, although did smile & was trying to be nice when asking us to fill a questionnaire in on our experience. Not really worth the reduced fee when using the pass so definitely not worth the full entry fee." #0.07 old method - 0.0007 new lrd100027
str_to_test = "Best lounge I have used in the UK, this lounge is the reason I keep the Priority Pass." #0.86 old method - 0.0 new lrd100012

print('Sentence: '+str(fixString(str_to_test))+'    Sentiment: '+str(getStrSentiment(str_to_test)))

