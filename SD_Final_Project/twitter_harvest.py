from pattern.web import Twitter

def twitter_harvest(keyword,number_of_tweets):
	"""collect number_of_tweets from Twitter using the keyword"""
	t = Twitter() #shorten Twitter()
	i = None #where you start the first time you run the search
	tweets = [] #compile tweets in a list
	for tweet in t.search(keyword,start = i,count = number_of_tweets):
		text = tweet.text.encode("utf-8")
		tweets.append(text) #add tweet to list of tweets
		i = tweet.id #resets where you start so you don't repeat tweets
	return tweets

#print twitter_harvest('POTUS',3)