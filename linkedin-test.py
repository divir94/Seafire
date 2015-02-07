import oauth2 as oauth
import httplib2
import time, os, simplejson

# Fill the keys and secrets you retrieved after registering your app
consumer_key         =   '75imqcm7hex0lp'
consumer_secret      =   '9nnWul0x0K0FTjiL'
user_token           =   '0994268e-25f3-41d8-87ad-426ae33a26b0'
user_secret          =   'f0c10d40-a189-4a2f-af69-e6fd564dd543'

# Use your API key and secret to instantiate consumer object
consumer = oauth.Consumer(consumer_key, consumer_secret)

# Use the consumer object to initialize the client object
client = oauth.Client(consumer)

# Use your developer token and secret to instantiate access token object
access_token = oauth.Token(
            key=user_token,
            secret=user_secret)

client = oauth.Client(consumer, access_token)

# Make call to LinkedIn to retrieve your own profile
resp,content = client.request("https://api.linkedin.com/v1/people/~/connections:(industry,positions)?format=json", "GET", "")

print content