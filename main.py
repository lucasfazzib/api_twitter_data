from secrets import CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET

import tweepy

from fastapi import FastAPI

# WOEID of sp
woeid = 455827

def get_trends(woeid: int):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    # fetching the trends
    trends = api.get_place_trends(woeid)
 
    # printing the information
    print("The top trends for the location are :")
 
    #trends
    # for value in trends:
    #     for trend in value['trends']:
    #         print(trend['name'])

    #tweets
    for tweet in trends:
        print(tweet)

get_trends(woeid)

# app = FastAPI()

# @app.get("/trends")
# def get_trends_route():
#     return {"Hello": "World"}