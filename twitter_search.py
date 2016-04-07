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
	results = api.GetSearch(term = search_term,
		count = count)
	tweets = []
	for tweet in results:
		text = tweet.text.encode('utf-8')
		tweets.append(text)
	return tweets
		

def data_analysis(search_term,count):
	"""analyze data to find the average polarity; return average 
	polarity of data from a given source"""
	data = collect_tweets(search_term,count,)
	polarity_compilation = [] #will find average of this list
	for entry in data: #run through each Tweet
		entry_analysis = sentiment(entry) #analyze each entry
		#print entry, entry_analysis
		polarity_compilation.append(entry_analysis) #add to list to average
	average_polarity = sum(polarity_compilation)/len(polarity_compilation)
	return search_term, average_polarity

search_term = 'Bern'
count = 10

print data_analysis(search_term,count)