import tweepy
import csv
import numpy as np
from textblob import TextBlob
from keras.models import Sequential
from keras.layers import Dense



#Step 1 - Insert your API keys
consumer_key= 'CONSUMER_KEY_HERE'
consumer_secret= 'CONSUMER_SECRET_HERE'
access_token='ACCESS_TOKEN_HERE'
access_token_secret='ACCESS_TOKEN_SECRET_HERE'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Step 2 - Search for your company name on Twitter
public_tweets = api.search('company_name')

#Step 3 - Define a threshold for each sentiment to classify each 
#as positive or negative. If the majority of tweets you've collected are positive
#then use your neural network to predict a future price
for tweet in public_tweets:    
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    



# Step 4 data collection
def get_data(filename,dates,prices):
	dates = []
	prices = []
	with open(filename, 'r') as csvfile:
		csvFileReader = csv.reader(csvfile)
		next(csvFileReader)	# skipping column names
		for row in csvFileReader:
			dates.append(int(row[0].split('-')[2]))
			prices.append(float(row[1])) # open value
	return dates, prices

#Step 5 reference your CSV file here
get_data('your_company_stock_data.csv')




#Step 6 In this function, build your neural network model using Keras, train it, then have it predict the price 
#on a given day. We'll later print the price out to terminal.
def predict_prices(dates, prices, x):

predicted_price = predict_price(dates, prices, 29)
print(predicted_price)

'''
TO DO:
Feel like we know what the algorithm is doing:

1) General flow:
1.1) Find tweets about your company: Step 1-3
1.2) Find stock data about the company (if sentiment positive): Step 4-5
1.3) Predict prices from neural network: Step 6

2) Subsections
Get ok with the implementations
Refactor their code
See what happens!



'''
