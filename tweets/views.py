from django.shortcuts import render
from django.http import HttpResponse
from TwitterSearch import *

def index(request):
	try:
		tso = TwitterSearchOrder() # create a TwitterSearchOrder object
		tso.setKeywords(['basketball']) # let's define all words we would like to have a look for
		tso.setLanguage('en') # we want to see English tweets only
		tso.setCount(7) # please dear Mr Twitter, only give us 7 results per page
		tso.setIncludeEntities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
		ts = TwitterSearch(
			consumer_key = 'rv01lKOzYhKSDdoNv5PQ',
			consumer_secret = '2OmHBCuQPYyXWtec2yI1NDykzaDvz4f9oTpVay8QDoI',
			access_token = '47210904-9aMkHRVrv4kHmEb3WG7Tph3L7JRpjLT2Q0hX3J9uw',
			access_token_secret = 'TzdKpq2EDdhPZZF2Z8tMxbvqlFnowySmUvCNvJONqgbh0'
		)


		for tweet in ts.searchTweetsIterable(tso): # this is where the fun actually starts :)
			# return HttpResponse( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
			return HttpResponse('%s' % (tweet['entities']['hashtags']))

	except TwitterSearchException as e: # take care of all those ugly errors if there are some
		return HttpResponse(e)
