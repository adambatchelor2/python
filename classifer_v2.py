#https://textblobreadthedocsio/en/dev/classifiershtml
train = [
     ('delicious and well stocked snack bar', 'pos'),
     ('this is an amazing place!', 'pos'),
     ('The food variety was excellent.', 'pos'),
     ('Good seating with plenty of places to sit and charge devices.Good food selection', 'pos'),
     ("Very very good, the ambiance is comfortable, the staff is very kind.", 'pos'),
     ('I do not like this restaurant', 'neg'),
     ('This is the worst PriorityPass lounge I have ever been to', 'neg'),
     ('lounge is never open','neg'),
     ('food is rubbish','neg'),
     ('waste of money','neg'),
     ("They have no facilities", 'neg'),
     ('Service was horrible', 'neg'),
     ('Food must be improved. Quality and selection was pathetic.', 'neg'),
     ('Was very disappointed to find that my Husband and I could not gain access', 'neg'),
     ('The lounge was quite filthy','neg'),
     ('the staff were rude, the lounge was dirty and the bathrooms were disgusting','neg'),
     ('Our stay here was great! Thank you very much!','pos'),
     ('Very nice lounge that was pretty comfortable, not too crowded, great refreshments and a wonderful staff.','pos'),
     ('Amazing customer service','pos'),
     ('Amazing experience!! The staff were so helpful and attentive to your needs. Highly recommend this lounge!','pos'),
     ('staff was very accommodating','pos')
 ]

from textblob.classifiers import NaiveBayesClassifier

cl = NaiveBayesClassifier(train)

testStr = 'Waste of money. Poor food and very very basic lounge.'

testOut = cl.classify(testStr)
testOut2 = cl.prob_classify(testStr)

print (testOut)
print ('Positive = ' + str(round(testOut2.prob("pos"), 2)))
print ('Negative = ' + str(round(testOut2.prob("neg"), 2)))