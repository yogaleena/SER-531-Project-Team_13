import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
import time


class MyListener(StreamListener):

    def on_data(self, data):
        try:
            print(data)
            sFile = open('EventData.csv', 'a')
            sFile.write(data)
            sFile.write('\n')
            sFile.close()
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
            time.sleep(5)

    def on_error(self, status):
        print(status)
        return True


auth = tweepy.OAuthHandler("jSYOQvmz9lmZco947OWVVgdze",
                           "ri08DWJdyuInIPLAkwxj2Sc3T5RL5M1tjaFkRyQvD7hpLgA9Yb")
auth.set_access_token("1458707545774706695-hEyjIWrJcu855PknNJqmQQEsKkU34E",
                      "TREA0Bxx61KDIQvKD6R7amxWRJbhusholIRTN1Y0KF0in")

api = tweepy.API(auth)

eventList =["football", "health", "medical", "devils", "sundevil", "engineering", "opportunity", "job", "job-search"]

twitter_list = Stream(auth, MyListener())
twitter_list.filter(track=['events', 'event'])


for stweet in api.search(q="Python", lang="en", rpp=10, geocode="33.42552° N -111.94125° E"):
    print(f"{stweet.user.name}:{stweet.text}")

places_value = api.geo_search(query="USA", granularity="country")
place_value_id = places_value[0].id

tweets_list = api.search(q="place:%s" % place_value_id, limit=1000, lang="en")
for ntweet in tweets_list:
    print(f"{ntweet.text} : {ntweet.place.name}")