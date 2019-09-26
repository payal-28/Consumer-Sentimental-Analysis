# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 19:06:00 2019

@author: Payal Arora
"""

import pandas as pd
import matplotlib.pyplot as plt
import tweepy
from textblob import TextBlob

def percentage(part,whole):
    return 100*float(part)/float(whole)

#Sample keys
api_key1="GCYhYXmb0MoGNvNx17DvvgGhv"
api_secret1="aNGHiuKj4SsyhhyTlh8BlNZYD29bas6P1Ykw9bU6txUGp000o1"
access_token1="752547855957692416-yHtgq8FC4KbiwdnYzSzrRAaKhsyfx11"
access_token_secret1="xNT9mxJQpgik7cpcGLgq2mrHFpb39xa7qLN3zU5EU5VPe"

#establishing connection
auth=tweepy.OAuthHandler(input("Enter API key:"),input("Enter API secret:"))
auth.set_access_token(input("Enter Access Token:"),input("Enter Access Token Secret:"))
api=tweepy.API(auth)


#extracting tweets
num_of_tweets=int(input("Enter the number of tweets to be extracted:"))
tweets=tweepy.Cursor(api.search,input("Enter the shopping site of which tweets are to be extracted:"),since=input("Enter the date since when the tweets are to be extracted from last 7 days:"),until=input("Enter the date till when the tweets are to be extracted from last 7 days:"),lang="en").items(num_of_tweets)


#run this code for printing tweets
"""
temp=[]
tweets_print=[tweet.text for tweet in tweets]
for j in tweets_print:
    temp.append(j)
    
print(temp)  
"""
#Performing sentimental analysis  
positive=0
negative=0
neutral=0
polarity=0

for tweet in tweets:
    analysis=TextBlob(tweet.text)
    polarity+=analysis.sentiment.polarity
    
    if (analysis.sentiment.polarity==0):
        neutral=neutral+1
    elif (analysis.sentiment.polarity>0.00):
        positive=positive+1
    elif (analysis.sentiment.polarity<0.00):
        negative=negative+1

#Converting into percentage        
positive=percentage(positive,num_of_tweets)
negative=percentage(negative,num_of_tweets)
neutral=percentage(neutral,num_of_tweets)
        
positive=format(positive,'.2f')
negative=format(negative,'.2f')
neutral=format(neutral,'.2f')

print("Positive percentage:",positive)
print("Negative percentage:",negative)
print("Neutral percentage:",neutral)

#checking Polarity
if polarity ==0:
    print("Neutral")
elif polarity>0.00:
    print("Positive")
elif polarity<0.00:
    print("Negative")
print("Polarity is:",polarity)

#plotting pie chart       
labels=['Positive','Negative','Neutral']
values=[positive,negative,neutral]
colors=["green","yellow","red"]
patches,texts,autotexts=plt.pie(values,colors=colors,startangle=90,autopct='%.2f%%')
plt.legend(patches,labels,loc="best")
plt.title("Sentimental analysis")
plt.axis("equal")
plt.tight_layout()
plt.show()


"""
Performing sentimental analysis of Amazon, Flipkart and Myntra
"""
"""
amazon sentiment analysis
"""
amzn_positive=0
amzn_negative=0
amzn_neutral=0
amzn_polarity=0

for tweet in tweets:
    analysis=TextBlob(tweet.text)
    amzn_polarity+=analysis.sentiment.polarity
    
    if (analysis.sentiment.polarity==0):
        amzn_neutral=amzn_neutral+1
    elif (analysis.sentiment.polarity>0.00):
        amzn_positive=amzn_positive+1
    elif (analysis.sentiment.polarity<0.00):
        amzn_negative=amzn_negative+1
        
amzn_positive=percentage(amzn_positive,num_of_tweets)
amzn_negative=percentage(amzn_negative,num_of_tweets)
amzn_neutral=percentage(amzn_neutral,num_of_tweets)
        
amzn_positive=format(amzn_positive,'.2f')
amzn_negative=format(amzn_negative,'.2f')
amzn_neutral=format(amzn_neutral,'.2f')

print("Amazon Positive Pecentage:",amzn_positive)
print("Amazon Negative Percentage:",amzn_negative)
print("Amazon Neutral Percentage:",amzn_neutral)

if amzn_polarity ==0:
    print("Polarity is Neutral")
elif amzn_polarity>0.00:
    print("Polarity is Positive")
elif amzn_polarity<0.00:
    print("Polarity is Negative")

print("Amazon Polarity is:",amzn_polarity)

#plotting
labels=['Positive','Negative','Neutral']
values=[amzn_positive,amzn_negative,amzn_neutral]
colors=["green","yellow","red"]
patches,texts,autotexts=plt.pie(values,colors=colors,startangle=90,autopct='%.2f%%')
plt.legend(patches,labels,loc="best")
plt.title("Amazon Sentimental Analysis")
plt.axis("equal")
plt.tight_layout()
plt.show()


"""
flipkart sentiment analysis
"""

flip_positive=0
flip_negative=0
flip_neutral=0
flip_polarity=0

for tweet in tweets:
    analysis=TextBlob(tweet.text)
    flip_polarity+=analysis.sentiment.polarity
    
    if (analysis.sentiment.polarity==0):
        flip_neutral=flip_neutral+1
    elif (analysis.sentiment.polarity>0.00):
        flip_positive=flip_positive+1
    elif (analysis.sentiment.polarity<0.00):
        flip_negative=flip_negative+1
        
flip_positive=percentage(flip_positive,num_of_tweets)
flip_negative=percentage(flip_negative,num_of_tweets)
flip_neutral=percentage(flip_neutral,num_of_tweets)
        
flip_positive=format(flip_positive,'.2f')
flip_negative=format(flip_negative,'.2f')
flip_neutral=format(flip_neutral,'.2f')

print("Flipkart Positive Percentage:",flip_positive)
print("Flipkart Negative Percentage:",flip_negative)
print("Flipkart Neutral Percentage:",flip_neutral)

if flip_polarity ==0:
    print("Polarity is Neutral")
elif flip_polarity>0.00:
    print("Polarity is Positive")
elif flip_polarity<0.00:
    print("Polarity is Negative")
    
print("Flipkart Polarity is:",flip_polarity)    

#plotting
labels=['Positive','Negative','Neutral']
values=[flip_positive,flip_negative,flip_neutral]
colors=["green","yellow","red"]
patches,texts,autotexts=plt.pie(values,colors=colors,startangle=90,autopct='%.2f%%')
plt.legend(patches,labels,loc="best")
plt.title("Flipkart Sentimental Analysis")
plt.axis("equal")
plt.tight_layout()
plt.show()

"""
myntra sentiment analysis
"""

myn_positive=0
myn_negative=0
myn_neutral=0
myn_polarity=0

for tweet in tweets:
    analysis=TextBlob(tweet.text)
    myn_polarity+=analysis.sentiment.polarity
    
    if (analysis.sentiment.polarity==0):
        myn_neutral=myn_neutral+1
    elif (analysis.sentiment.polarity>0.00):
        myn_positive=myn_positive+1
    elif (analysis.sentiment.polarity<0.00):
        myn_negative=myn_negative+1
        
myn_positive=percentage(myn_positive,1000)
myn_negative=percentage(myn_negative,1000)
myn_neutral=percentage(myn_neutral,1000)
        
myn_positive=format(myn_positive,'.2f')
myn_negative=format(myn_negative,'.2f')
myn_neutral=format(myn_neutral,'.2f')

print("Myntra Positive Percentage:",myn_positive)
print("Myntra Negative Percentage:",myn_negative)
print("Myntra Neutral Percentage:",myn_neutral)

if myn_polarity ==0:
    print("Polarity is Neutral")
elif myn_polarity>0.00:
    print("Polarity is Positive")
elif myn_polarity<0.00:
    print("Polarity is Negative")

print("Myntra Polarity is:",myn_polarity)

#plotting
labels=['Positive','Negative','Neutral']
values=[myn_positive,myn_negative,myn_neutral]
colors=["green","yellow","red"]
patches,texts,autotexts=plt.pie(values,colors=colors,startangle=90,autopct='%.2f%%')
plt.legend(patches,labels,loc="best")
plt.title("Myntra Sentimental Analysis")
plt.axis("equal")
plt.tight_layout()
plt.show()

"""
comparative analysis of three sites
"""
#Enter the positive,negative and neutral values of the three sites in place of Values for comparison

a,b,c=[eval(x) for x in input("Enter values for comparison:").split(',')]
combined=["Amazon","Flipkart","Myntra"]
values=[a,b,c]
colors=["grey","blue","orange"]
patches,texts,autotexts=plt.pie(values,colors=colors,startangle=90,autopct='%.2f%%')
plt.legend(patches,combined,loc="best")
plt.title("Combined Analysis of Amazon, Flipkart, Myntra ")
plt.axis("equal")
plt.tight_layout()
plt.show()





