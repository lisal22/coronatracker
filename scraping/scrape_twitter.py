from twitterscraper import query_tweets
import json
import datetime
from abc import ABCMeta, abstractclassmethod

class ITwitterBuilder(metaclass = ABCMeta):
    "the builder interface"

@staticmethod
@abstractmethod
def build_username():
    pass

@staticmethod
@abstractmethod
def build_tweet_id():
    pass

@staticmethod
@abstractmethod
def build_hashtags():
    pass

@staticmethod
@abstractmethod
def build_links():
    pass

@staticmethod
@abstractmethod
def build_timestamp():
    pass

@staticmethod
@abstractmethod
def build_text():
    pass

class TwitterScrape(ITwitterBuilder):
    "concrete builder"

    def __init__(self):
        self.product = Product()
    
    def build_username(self, username):
        self.username = username
        return self

    def build_tweet_id(self, tweet_id):
        self.tweet_id = tweet_id
        return self

    def build_hashtags(self, hashtags):
        self.hashtags = hashtags
        return self

    def build_links(self, links):
        self.links = links
        return self

    def build_timestamp(self, timestamp):
        self.timestamp = timestamp
        return self

    def build_text(self, text):
        self.text = text
        return self

    def get_twitter_info(self):
        return self.product

class Product():
    "the products"

    def __init__(self):
        self.info = []

class Director:
    "the director"

    @staticmethod
    def construct():
        "constrct and return info"
        return Builder()\
            .build_username()\
            .build_tweet_id()\
            .build_hashtags()\
            .build_links()\
            .build_timestamp()\
            .build_text()\
            .get_twitter_info()

TwitterInfo = Director.construct()

if __name__ == '__main__':
    search_query = "WuhanVirus OR 2019nCoV OR Coronavirus OR WuhanCoronavirus OR coronaviruses OR coronavirusoutbreak OR coronavirus OR Covid-19 OR COVID-19 OR ChineseCoronavirus OR Coronaoutbreak"
    filename = "corona_twitter.json"
    #filename = "{}.json".format(username)

    tweets = query_tweets(query=search_query, begindate=datetime.date(2019, 12, 30), enddate=datetime.date(2020, 1, 27))
    print("Found: {} tweets".format(len(tweets)))

    j = []
    for t in tweets:
        t.timestamp = t.timestamp.isoformat()
        print("{} {} {} {} {}: {}".format(TwitterInfo.info))
        j.append(t.__dict__)

    with open(filename, "w") as f:
        f.write(json.dumps(j))
