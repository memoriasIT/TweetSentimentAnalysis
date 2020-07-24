from twitter_scraper import get_tweets

# Save tweets from february - for each day
day = 1
for x in range(29):
    date = "2020-02-" + str(day)
    print(date + ".txt")

    # Download tweets and save to file with date
    file = open(date +".txt", "w")
    for tweet in get_tweets('#china until:'+date, pages=1):
        try:
            file.write(tweet['text'].replace("\n", " ")+"\n")
        except Exception:
            pass
        
    file.close()    

    day = day +1

# Save tweets from march - for each day
day = 15
for x in range(31):
    date = "2020-03-" + str(day)
    print(date + ".txt")

    # Download tweets and save to file with date
    file = open(date +".txt", "w")
    for tweet in get_tweets('#china until:'+date, pages=1):
        try:
            file.write(tweet['text'].replace("\n", " ")+"\n")
        except Exception:
            pass

    file.close()    

    day = day +1