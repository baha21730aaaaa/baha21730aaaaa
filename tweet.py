import tweepy

# داتاکانی API Keys و Access Tokens
API_KEY = 'API_KEY'  # لەجیاتی API_KEY، داتاکانی خۆت بنووسە
API_SECRET_KEY = 'API_SECRET_KEY'  # لەجیاتی API_SECRET_KEY، داتاکانی خۆت بنووسە
ACCESS_TOKEN = 'ACCESS_TOKEN'  # لەجیاتی ACCESS_TOKEN، داتاکانی خۆت بنووسە
ACCESS_TOKEN_SECRET = 'ACCESS_TOKEN_SECRET'  # لەجیاتی ACCESS_TOKEN_SECRET، داتاکانی خۆت بنووسە

# دەستپێکردنی API
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# ناردنی توڵێک
tweet_text = "ئەمە توڵێکی تاقیکارییە بە بەکارهێنانی Twitter API و Python! 🚀"
try:
    api.update_status(tweet_text)
    print("توڵێک بە سەرکەوتوویی نێردرا! ✅")
except tweepy.TweepError as e:
    print(f"هەڵە: {e} ❌")
