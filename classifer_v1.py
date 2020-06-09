#https://textblobreadthedocsio/en/dev/classifiershtml
train = [
     ('I love this sandwich', 'pos'),
     ('this is an amazing place!', 'pos'),
     ('I feel very good about these beers', 'pos'),
     ('this is my best work', 'pos'),
     ("what an awesome view", 'pos'),
     ('I do not like this restaurant', 'neg'),
     ('I am tired of this stuff', 'neg'),
     ('lounge is never open','neg'),
     ('food is rubbish','neg'),
     ("I can't deal with this", 'neg'),
     ('he is my sworn enemy!', 'neg'),
     ('my boss is horrible', 'neg')
 ]
test = [
     ('the beer was good', 'pos'),
     ('I do not enjoy my job', 'neg'),
     ("I ain't feeling dandy today", 'neg'),
     ("I feel amazing!", 'pos'),
     ('Gary is a friend of mine', 'pos'),
     ("I can't believe I'm doing this", 'neg')
 ]


from textblob.classifiers import NaiveBayesClassifier

cl = NaiveBayesClassifier(train)

testStr = 'drinks are rubbish'

testOut = cl.classify(testStr)
testOut2 = cl.prob_classify(testStr)

print (testOut)
print (round(testOut2.prob("pos"), 2))