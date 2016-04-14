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

(Will add information about config file and api keys later)

##Runing Program
```
$ python twitter_search.py
``` 

##Copyright and license
Code released under the MIT license.
