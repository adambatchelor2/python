
from textblob import TextBlob

# b = TextBlob("I havv goood speling!")

# print(b.correct())


# need iserror statement


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