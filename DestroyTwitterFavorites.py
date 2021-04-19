import twitter
from pprint import pprint
import sys



#Keys - Generate your own from developer twitter
consumer_key = CONSUMERKEY '''make sure keys are in single quotes '...'
consumer_secret = CONSUMERSECRET
access_token = ACCESSTOKEN
access_token_secret = ACCESSTOKENSECRET

#Access API
api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_token_secret)

# Get the statuses from the API
statuses = api.GetFavorites()

#Log one of te favourites in a txt file for posterity
with open('favorites.txt', 'a') as f:
    f.write(str(statuses[0]))
    f.write('\n\n')

#Some output to show progress
print(len(statuses),'favorites retrieved ')    
print('starting deletion at this status now \n\n')
pprint(statuses[0].created_at)
pprint(statuses[0].text)
print('\n... ...')
for status in statuses:
    api.DestroyFavorite(status)
print('Done!')
