import twitter
import indicoio
from indicoio import sentiment, political
from config import indico_key,consumer_key,consumer_secret,access_token_key,access_token_secret

indicoio.config.api_key = indico_key
api = twitter.Api(consumer_key = consumer_key,
    consumer_secret = consumer_secret,
    access_token_key = access_token_key,
    access_token_secret = access_token_secret)

def collect_tweets(search_term,count):
    """searches tweets using search term, returns geotagged tweets"""
    i = None
    tweets = []
    rep = 1
    for n in range(100):
        results = api.GetSearch(term = search_term,
            count = 100,
            result_type = 'recent',
            max_id = i)
        for tweet in results:
            if tweet.coordinates == None:
                i = tweet.id - 1 #starts next loop after last tweet 
            else:
                print tweet.coordinates
                tweets.append(tweet)
                i = tweet.id - 1
        #print rep
        rep += 1
    for tweet in tweets:
        print "TWEET__________"
        print tweet.text
    return tweets #returns list of tweet objects if they have a geotag

def geo_collect_tweets(search_term,latitude,longitude,radius):
    """search for tweets within certain radius of latitude and longitude with certain keyword in them.
        Returns the list of tweet texts
    """
    tweets = []
    results = api.GetSearch(term = search_term, count=100, result_type = 'recent', geocode=(latitude, longitude, radius))
    for tweet in results:
        tweets.append(tweet.text)
    return tweets 
        
def geo_processing(search_term,count):
    """sorts tweets by location, returns dict[locations] = text"""
    data = collect_tweets(search_term,count)
    ne  = [] #not a viable way to do this if we have more detailed
    nw = [] #breakdown -- just for now
    s = []
    mw = []
    geo_dict = dict()
    if data == []:
        return "No geotags in this dataset"
    else:
        for tweet in data: #create dict --> key is coordinates, value is text
            geotag = tweet.coordinates
            coord = geotag['coordinates']
            print coord
            if int(coord[0]) in range(-130,-115) and int(coord[1]) in range(30,50):
                nw.append(tweet.text.encode('utf-8'))
            elif int(coord[0]) in range(-115,-85) and int(coord[1]) in range(37,50):    
                mw.append(tweet.text.encode('utf-8'))
            elif int(coord[0]) in range(-85,-65) and int(coord[1]) in range(37,47):
                ne.append(tweet.text.encode('utf-8'))
            elif int(coord[0]) in range(-115,-85) and int(coord[1]) in range(25,37):    
                s.append(tweet.text.encode('utf-8'))
        geo_dict['northwest'] = nw
        geo_dict['midwest'] = mw
        geo_dict['northeast'] = ne
        geo_dict['south'] = s
        return geo_dict

def data_analysis(search_term,count):
    """analyzes tweet text, returns dict[location] = average polarity"""
    data = geo_processing(search_term,count)
    if type(data) == str:
        return search_term, data
    map_pol = dict()
    for location, tweets in data.items(): #run through each dict item
        polarity_compilation = [] #will find average of this list
        if tweets == []:
            polarity_compilation.append(0)
        else:
            for tweet in tweets:
                entry_analysis = sentiment(tweet) #analyze each entry
                polarity_compilation.append(entry_analysis) #add to list to average
        map_pol[location] = sum(polarity_compilation)/len(polarity_compilation)
    return search_term, map_pol

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
    NE_sentiment_values = []
    for tweet in NE_text:
        NE_sentiment_values.append(sentiment(tweet))

    S_sentiment_values = []
    for tweet in S_text:
        S_sentiment_values.append(sentiment(tweet))

    MW_sentiment_values = []
    for tweet in MW_text:
        MW_sentiment_values.append(sentiment(tweet))

    W_sentiment_values = []
    for tweet in W_text:
        W_sentiment_values.append(sentiment(tweet))

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
