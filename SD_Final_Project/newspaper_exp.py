import newspaper
from newspaper import Config, Article, Source
import indicoio
from indicoio import keywords, sentiment
from os.path import exists
import sys
from pickle import dump, load
from string import punctuation, ascii_letters
import matplotlib.pyplot as plt

indicoio.config.api_key = '863dee4f6fe69b9f62bf9b5d1ede7dd3'

class newspaper_scraping(object):
	def __init__(self,paper_site):
		"""initializes paper"""
		self.site = paper_site

	def paper(self,word,article_number):
		"""returns dictionary --> key_words_library[tag] = articles with that tag"""
		self.search_term = word.lower()
		self.number = article_number
		the_paper = newspaper.build(self.site, memoize_articles = False, fetch_images = False, keep_article_html = False)
		self.size = the_paper.size()
		pol = dict()
		key_words = dict()
		tag_ave = dict()
		date = dict()
		tag_dict = dict()
		dates_list = []
		#key_words_library = []
		for i in range(self.number): #range(cnn.size()) to categorize them all
			article = the_paper.articles[i]
			article.download()
			article.parse()
			article_text = article.text.encode('utf-8')
			pol[i] = sentiment(article_text) #organizes dictionaries by article number
			key_words[i] = keywords(article_text)
			date[i] = article.url.strip(ascii_letters + punctuation)
			if len(date[i]) >= 7:
				date[i] = int((date[i])[6])
			else:
				date[i] == int(0)
		for i, tags in key_words.items():
			for tag, importance in tags.items():
				tag = tag.lower()
				if tag == self.search_term:
					dates_list.append((date[i],pol[i]))
		tag_dict[word] = dates_list
		return tag_dict

#print cnn.size()
CNN = newspaper_scraping('http://www.cnn.com/')
#print CNN.paper('social media',10)
#CNN_size = newspaper.build('http://www.cnn.com/',memoize_articles = False)
#print CNN_size.size()

def articles_dump(file_name,search_term):
	f = open(file_name,'r+')
	f.seek(0,0)  #start lookign at file from beginning
	tag_dict = load(f) #loads a list of single dictionary entries with tuples 
	dates = []
	pols = []
	for entry in tag_dict: #run through each dictionary in list
		for tag, dates_dict in entry.items(): #entry is a list of tuples
			if tag == search_term:
				for tuples in dates_dict: #run through list of tuples
					dates.append(tuples[0]) 
					pols.append(tuples[1])
				return dates, pols
	f.close()
	if dates == []:
		f = open(file_name,'w')
		dump(tag_dict + [CNN.paper(search_term,10)],f)
		f.close()
		#print 'Done! ' + file_name + ' has been added.'
		return articles_dump(file_name,search_term)
	else:
		return dates, pols

#print articles_dump('tag_polarities.txt','social media')
# f = open('tag_polarities.txt','w')
# dump([CNN.paper('women',20), CNN.paper('social media',20)],f)
# f.close()
points = articles_dump('tag_polarities.txt','social media')
print points
plt.plot(points[0],points[1],'ro')
plt.axis([0,12,-1,1])
plt.show()