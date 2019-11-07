from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener #class from streaming module that allows stream listener
from tweepy import OAuthHandler #class that authenticates 
from tweepy import Stream #Streaming class
import dotenv
dotenv.load_dotenv()
import os

##TWITTER AUTH CLASS
class TwitterAuthenticator():

    def authenticate_twitter_app(self):
        auth = OAuthHandler(os.getenv('CONSUMER_KEY'), os.getenv('CONSUMER_SECRET'))
        auth.set_access_token(os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_SECRET'))
        return auth

class TwitterStreamer():

    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()    

    #class for streaming and processing live tweets
    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        #this handles auth/connection to stream api
        listener = TwitterListener(fetched_tweets_filename)
        auth = self.twitter_authenticator.authenticate_twitter_app()

        stream = Stream(auth,listener)

        stream.filter(track=hash_tag_list)

class TwitterListener(StreamListener): ## basic class that prints recieved tweets 

        def __init__(self, fetched_tweets_filename):
            self.fetched_tweets_filename = fetched_tweets_filename

        def on_data(self, data):        ##inhereted from StreamListener, overridden here
            try:
                print(data)
                with open(self.fetched_tweets_filename, 'a') as tf:
                    tf.write(data)
                return True
            except BaseException as e:
                print("Error on_data: %s" % str(e))
            return True

        def on_error(self, status):     #also inhereted from StreamListener, error handler
            print(status)


if __name__ == '__main__':

    hash_tag_list = ['donald trump', 'hillary clinton', 'barack obama', 'bernie sanders']
    fetched_tweets_filename = 'tweets.json'
    
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)
    
    
    

    
    
    
    
    
    
    
    
    


