import twitter
import indicoio
from indicoio import sentiment, political


indicoio.config.api_key = 
api = twitter.Api(consumer_key = ,
	consumer_secret = ,
	access_token_key = ,
	access_token_secret = )


def collect_tweets(search_term,count,location):
	results = api.GetSearch(term = search_term,
		count = count,
		geocode = location)
	tweets = []
	for tweet in results:
		text = tweet.text.encode('utf-8')
		tweets.append(text)
		#print text
	return tweets
		

def data_analysis(search_term,count,location):
	"""analyze data to find the average polarity; return average 
	polarity of data from a given source"""
	data = collect_tweets(search_term,count,location)
	polarity_compilation = [] #will find average of this list
	for entry in data: #run through each Tweet
		entry_analysis = sentiment(entry) #analyze each entry
		#print entry, entry_analysis
		polarity_compilation.append(entry_analysis) #add to list to average
	average_polarity = sum(polarity_compilation)/len(polarity_compilation)
	return search_term, average_polarity

search_term = 'Bern'
count = 200
lat_long_range1 = [40.712784,-74.005941,'300mi'] #NYC
lat_long_range2 = [32.318231,-86.902298,'300mi'] #Hicksville,AL

#print collect_tweets(search_term,count,lat_long_range)
print data_analysis(search_term,count,lat_long_range1)
print data_analysis(search_term,count,lat_long_range2)