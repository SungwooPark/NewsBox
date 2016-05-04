import twitter
import indicoio
import sys
from indicoio import sentiment
from config import indico_key,consumer_key,consumer_secret,access_token_key,access_token_secret
import color_map

indicoio.config.api_key = indico_key
api = twitter.Api(consumer_key = consumer_key,
    consumer_secret = consumer_secret,
    access_token_key = access_token_key,
    access_token_secret = access_token_secret)

def geo_collect_tweets(search_term,latitude,longitude,radius):
    """search for tweets within certain radius of latitude and longitude with certain keyword in them.
        Returns the list of unique tweet texts
    """
    i = None
    tweets = []
    rep = 1
    for n in range(2): #can only search 100 tweets at a time, so run search multiple times
    	results = api.GetSearch(term = search_term, 
    		count = 100, 
    		result_type = 'recent', 
    		max_id = i, #start a search from the most recent tweet id, working backwards
    		geocode =(latitude, longitude, radius))
        for tweet in results:
            tweets.append(tweet.text)
        i = tweet.id - 1 #want it to start at the tweet after the last tweet
        rep += 1
    return list(set(tweets)) #set gets rid of repititve tweets, but need to return a list

def geo_data_analysis(search_term):
    """analyzes the sentiment of tweets and return the average value for each region 
    """
    map_pol = dict()

    #A list of tweet texts from each region
    NE_text = geo_collect_tweets(search_term,42.781158,-71.398729,'250mi')
    S_text = geo_collect_tweets(search_term,33.000000,-84.000000,'500mi')
    MW_text = geo_collect_tweets(search_term,40.000000,-100.000000,'1000mi')
    W_text = geo_collect_tweets(search_term,35.000000,-120.000000,'250mi')
   
    #A list of sentiment values for the tweets from each region 
    NE_sentiment_values = sentiment(NE_text)
    S_sentiment_values = sentiment(S_text)
    MW_sentiment_values = sentiment(MW_text)
    W_sentiment_values = sentiment(W_text)

    #find the average sentiment value for each region
    NE_avg = sum(NE_sentiment_values)/len(NE_sentiment_values)
    S_avg = sum(S_sentiment_values)/len(S_sentiment_values)
    MW_avg = sum(MW_sentiment_values)/len(MW_sentiment_values)
    W_avg = sum(W_sentiment_values)/len(W_sentiment_values)

    return [W_avg,S_avg,NE_avg,MW_avg]

average_sentiments = geo_data_analysis(str(sys.argv[1]))
color_map.map_states(average_sentiments[0],average_sentiments[1],average_sentiments[2],average_sentiments[3],str(sys.argv[1]))

def produce_map(search_term):
	average_sentiments = geo_data_analysis(search_term)
	color_map.map_states(average_sentiments[0],average_sentiments[1],average_sentiments[2],average_sentiments[3],search_term)
