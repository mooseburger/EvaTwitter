import tweepy
from config import Config

auth = tweepy.OAuthHandler(Config.API_KEY, Config.API_SECRET)
auth.set_access_token(Config.ACCESS_TOKEN, Config.ACCESS_TOKEN_SECRET)

Api = tweepy.API(auth)