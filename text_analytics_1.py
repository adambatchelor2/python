from textblob import TextBlob
import re

def clean_tweet(tweet): 
        ''' 
        Utility function to clean tweet text by removing links, special characters 
        using simple regex statements. 
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split()) 

def get_tweet_sentiment(tweet): 
    # create TextBlob object of passed tweet text 
    analysis = TextBlob(clean_tweet(tweet)) 

    # return sentiment 
    return analysis.sentiment.polarity


# def get_tweet_subjectivity(tweet): 
#     # create TextBlob object of passed tweet text 
#     analysis = TextBlob(clean_tweet(tweet)) 

#     # return sentiment 
#     return analysis.sentiment

test_str = "the lounge was dirty"

print(get_tweet_sentiment(test_str))
