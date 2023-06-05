import tweepy


def auth_twitter(api_key, api_secret_key, access_token, access_token_secret):
    # authorize the API Key
    print("Using twitter Auth function")
    authentication = tweepy.OAuthHandler(api_key, api_secret_key)
    # authorization to user's access token and access token secret
    authentication.set_access_token(access_token, access_token_secret)
    # call the api
    api = tweepy.API(authentication)
    return api
