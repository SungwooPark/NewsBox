import newspaper
from newspaper import Config, Article, Source
import indicoio
from indicoio import keywords, text_tags, sentiment
indicoio.config.api_key = '863dee4f6fe69b9f62bf9b5d1ede7dd3'

class newspaper_scraping(object):
	def __init__(self,paper_site):
		self.site = paper_site

	def paper(self,word,article_number):
		"""returns dictionary --> key_words_library[tag] = average polarity of that tag"""
		self.search_term = word.lower()
		self.number = article_number

		the_paper = newspaper.build(self.site, memoize_articles = False, fetch_images = False, keep_article_html = False)
		pol = dict()
		key_words = dict()
		tag_frequency = dict()
		key_words_library = []
		articles = dict()
		for i in range(self.number): #range(cnn.size()) when ready to categorize them all
			article = the_paper.articles[i]
			article.download()
			article.parse()
			article_text = article.text.encode('utf-8')
			articles[i] = article_text
			pol[i] = sentiment(article_text) #organizes dictionaries by article number
			key_words[i] = keywords(article_text)
		for i, tags in key_words.items():
			for tag, importance in tags.items():
				tag = tag.lower()
				if tag == self.search_term:
					key_words_library.append(articles[i])
		return key_words_library

#print cnn.size()
#CNN = newspaper_scraping('http://www.cnn.com/')
#print CNN.paper('social media')
