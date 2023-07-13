from snscrape.modules.twitter import TwitterTweetScraperMode, TwitterTweetScraper

tweet_id= '1676980499410202624'
def getFullConversation(tweet_id):
    conv = []
    while True:
        try:
            tweet = list(TwitterTweetScraper(tweet_id).get_items())[0]
            print("here")
            print(tweet)
            break
        except Exception:
            print('borked')
            pass
getFullConversation('1676980499410202624')
print('')