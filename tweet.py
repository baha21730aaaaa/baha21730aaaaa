import tweepy

     # داتاکانی API Keys و Access Tokens
     API_KEY = 'API_KEY'
     API_SECRET_KEY = 'API_SECRET_KEY'
     ACCESS_TOKEN = 'ACCESS_TOKEN'
     ACCESS_TOKEN_SECRET = 'ACCESS_TOKEN_SECRET'

     # دەستپێکردنی API
     auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
     api = tweepy.API(auth)

     # ناردنی توڵێک
     tweet_text = "ئەمە توڵێکی تاقیکارییە بە بەکارهێنانی Twitter API و Python!"
     api.update_status(tweet_text)

     print("توڵێک بە سەرکەوتوویی نێردرا!")
