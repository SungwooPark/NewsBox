import indicoio
from indicoio import sentiment, political
from twitter_harvest import twitter_harvest
from newspaper_exp import newspaper_scraping
import matplotlib.pyplot as plt
import numpy as np

indicoio.config.api_key = '863dee4f6fe69b9f62bf9b5d1ede7dd3'

def data_analysis(source):
	"""analyze data to find the average polarity; return average 
	polarity of data from a given source"""
	data = source #search term and number
	if len(data) == 0: #in case keyword doesn't show up in source articles
		average_polarity = 0
		return average_polarity
	polarity_compilation = [] #will find average of this list
	for entry in data: #run through each piece of data
		entry_analysis = sentiment(entry) #analyze each entry
		#print entry, entry_analysis
		polarity_compilation.append(entry_analysis) #add to list to average
	average_polarity = sum(polarity_compilation)/len(polarity_compilation)
	return average_polarity

def plot_polarity(data,sources):
	"""This function plots the results of the data_analysis function in
	the form of a bar graph. The x-axis is the list items and the y-axis
	is the polarity of each list item."""
	sources_polarity = []
	for n in range(len(data)):
		polarity = data_analysis(data[n]) #find average polarity of each source
		sources_polarity.append(polarity) #add polarity to list
	objects = sources
	y_pos = np.arange(len(objects))
	plt.bar(y_pos,sources_polarity,align = 'center',alpha = .5)
	plt.xticks(y_pos,objects)
	plt.ylabel('Polarity')
	plt.title('Polarity of Data Sources towards ' + keyword)
	plt.show()

"""params"""
keyword = 'no'
number_of_tweets = 5
number_of_articles = 2

"""list of sources -- processed data put into data_analysis"""
Twitter = twitter_harvest(keyword,number_of_tweets)
CNN = newspaper_scraping('http://www.cnn.com/').paper(keyword,number_of_articles)
Fox = newspaper_scraping('http://www.foxnews.com/').paper(keyword,number_of_articles)


"""call function"""
plot_polarity([Twitter,CNN,Fox],['Twitter','CNN','Fox'])
