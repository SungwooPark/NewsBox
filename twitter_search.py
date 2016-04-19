import twitter
import indicoio
from indicoio import sentiment, political
from config import indico_key,consumer_key,consumer_secret,access_token_key,access_token_secret

indicoio.config.api_key = indico_key
api = twitter.Api(consumer_key = consumer_key,
    consumer_secret = consumer_secret,
    access_token_key = access_token_key,
    access_token_secret = access_token_secret)

def geo_collect_tweets(search_term,latitude,longitude,radius):
    """search for tweets within certain radius of latitude and longitude with certain keyword in them.
        Returns the list of tweet texts
    """
    tweets = []
    results = api.GetSearch(term = search_term, count=100, result_type = 'recent', geocode=(latitude, longitude, radius))
    for tweet in results:
        tweets.append(tweet.text)
    return tweets 

def geo_data_analysis(search_term):
    """analyzes the sentiment of tweets and return the average value for each region 
        in dictionary form. Keys are 'NE' (northeast), 'S'(south), 'MW' (midwest),and  'W' (West)
    """
    map_pol = dict()

    #A list of tweet text from each region
    NE_text = geo_collect_tweets(search_term,42.781158,-71.398729,'250mi')
    S_text = geo_collect_tweets(search_term,33.000000,-84.000000,'500mi')
    MW_text = geo_collect_tweets(search_term,40.000000,-100.000000,'1000mi')
    W_text = geo_collect_tweets(search_term,35.000000,-120.000000,'250mi')
   
    #A list of sentiment values from each region 
    NE_sentiment_values = sentiment(NE_text)
    S_sentiment_values = sentiment(S_text)
    MW_sentiment_values = sentiment(MW_text)
    W_sentiment_values = sentiment(W_text)

    NE_avg = sum(NE_sentiment_values)/len(NE_sentiment_values)
    S_avg = sum(S_sentiment_values)/len(S_sentiment_values)
    MW_avg = sum(MW_sentiment_values)/len(MW_sentiment_values)
    W_avg = sum(W_sentiment_values)/len(W_sentiment_values)

    print 'NE_avg', NE_avg
    print 'S_avg',S_avg
    print 'MW_avg',MW_avg
    print 'W_avg',W_avg

search_term = '#mondaymotivation'
count = 100

geo_data_analysis('#bernie')
