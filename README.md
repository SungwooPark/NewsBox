#NewsBox
@authors: *Sung Park* Olin College '19 , *Mary Keenan* Olin College '19

NewsBox is a python program that generates a graphical representation of varying positivity within Twitter toward certain topics in different regions US. NewsBox runs sentiment analysis of tweets with certain keyword in it and categorizes them by their geocode. It then calculates the average sentiment value of the region toward certain topic after processing a large number of relevant tweets from that region. As an output of the program, a map of the United States will be displayed with graphical representation of different sentiment value toward certain topic in different area.

##Getting Started
NewsBox uses python-twitter module to fetch tweets and [indico's](https://indico.io/) text analysis api to run a sentiment analysis. 

You can use pip to install python-twitter module.
```
$ pip install python-twitter
```

Then follow indico's [installation guide](https://indico.io/docs) to set up indico api on your machine.
 
Run following code to install indicoio PyPi Package.
```
$ pip install indicoio
```
You will have to get api keys for Twitter and Indico API. Create your own application in [Twitter Apps](https://apps.twitter.com/) page and get Twitter API key. You can follow indico's [installation guide](https://indico.io/docs) to get indico api key. Last step in setting up NewsBox is to create a configuration file. Create *config.py* with following code in it.
```
indico_key = '<Your Indico API Key>'
consumer_key = '<Your Twitter Consumer Key (API Key)>'
indico_secret = '<Your Twitter Consumer Secret (API Secret)>'
access_token_key = '<Your Twitter Access token>'
access_token_secret = '<Your Twitter Access token secret>'
```            

NewsBox is a webapp that uses Flask as a web framework. Run following code to install Flask.
```
$ sudo pip install Flask
```
(Optional)
It is recommended to run our program using virtualenv. If you would like to run NewsBox within virtualenv, install virtual env by running following script and then proceed to install all the dependencies.
```
$ sudo pip install virtualenv
```
or
```
$ sudo easy_install virtualenv
```
or
```
sudo apt-get install python-virtualenv
```
Then create virtualenv by running following script in a directory that you installed NewsBox.
```
$ virtualenv venv
```
Only thing you have to do after installing virtualenv is to activate the environment everytime you want to run the program.
```
$ . venv/bin/activate
```
##Runing Program
```
$ python hello.py
``` 
This will run our webapp in localhost:8000. Navigate to this localhost using webbrowser to use NewsBox.

##Copyright and license
[Python-twitter](https://github.com/bear/python-twitter), Twitter API wrapper for Python, for fetching tweets

[Indico API](https://indico.io/produc) for sentiment analysis

[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to process SVG file.

[Flask](http://flask.pocoo.org/) as a web framework.

