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
	results = api.GetSearch(term = search_term,count = count)
	tweets = []
	for tweet in results:
		if tweet.coordinates == None:
			pass
		else:
			tweets.append(tweet)
	return tweets #returns list of tweet objects if they have a geotag
		
def geo_processing(search_term,count):
	"""sorts tweets by location, returns dict[locations] = text"""
	data = collect_tweets(search_term,count)
	ne  = [] #not a viable way to do this if we have more detailed
	nw = [] #breakdown -- just for now
	s = []
	mw = []
	geo_dict = dict()
	if data == []:
		"No geotags in dataset"
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
	"""analyzes tweet text, returns dict[location] = polarity"""
	data = geo_processing(search_term,count)
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

search_term = '#NationalSiblingDay'
count = 100000

print data_analysis(search_term,count)
#print geo_processing(search_term,count)