
from textblob import TextBlob

def translateString(textStr):

	try:
		return textStr.translate(from_lang=textStr.detect_language(), to='en')
	except:
		return textStr


def spellingCorrect(textStr):
	return textStr.correct()


def fixString(textStr):
	textStr = TextBlob(textStr)
	textStr = translateString(textStr)
	textStr = spellingCorrect(textStr)
	
	return textStr

b = "this lounge is diiirty and smelll"

print(fixString(b))