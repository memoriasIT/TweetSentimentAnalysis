import json
import csv
import os
from urllib.parse import quote
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

# Tone list as possible results
tone_list = ["anger", "fear", "joy", "sadness", "analytical", "confident", "tentative"]

# I know this is not optimal I did listdir and pasted here for quick script
dates = ['2020-02-1.txt', '2020-02-2.txt', '2020-02-3.txt', '2020-02-4.txt', '2020-02-5.txt', '2020-02-6.txt', '2020-02-7.txt', '2020-02-8.txt', '2020-02-9.txt', '2020-02-10.txt', '2020-02-11.txt', '2020-02-12.txt', '2020-02-13.txt', '2020-02-14.txt', '2020-02-15.txt', '2020-02-16.txt', '2020-02-17.txt', '2020-02-18.txt', '2020-02-19.txt', '2020-02-20.txt', '2020-02-21.txt', '2020-02-22.txt', '2020-02-23.txt', '2020-02-24.txt', '2020-02-25.txt', '2020-02-26.txt', '2020-02-27.txt', '2020-02-28.txt', '2020-02-29.txt', '2020-03-1.txt' , '2020-03-2.txt', '2020-03-3.txt', '2020-03-4.txt', '2020-03-5.txt', '2020-03-6.txt', '2020-03-7.txt', '2020-03-8.txt', '2020-03-9.txt', '2020-03-10.txt', '2020-03-11.txt', '2020-03-12.txt', '2020-03-13.txt', '2020-03-14.txt', '2020-03-15.txt', '2020-03-16.txt', '2020-03-17.txt', '2020-03-18.txt', '2020-03-19.txt', '2020-03-20.txt', '2020-03-21.txt', '2020-03-22.txt', '2020-03-23.txt', '2020-03-24.txt', '2020-03-25.txt', '2020-03-26.txt', '2020-03-27.txt', '2020-03-28.txt', '2020-03-29.txt',  '2020-03-30.txt', '2020-03-31.txt']

# Save to out.csv
with open("out.csv", "a", newline="") as f:
    writer = csv.writer(f)

    for date in dates:
        print(date + "\n\n\n\n")
        # Load all tweets one by one in the file of saved tweets
        with open(date) as f:
            for line in f:
                try:
                    # Serialize to avoid invalid characters
                    tweetStringSerialized = quote(line)

                    # Make call to Watson API and convert to dictionary
                    WatsonOutput = os.popen("curl -X GET -u \"apikey:INSERT YOUR API KEY HERE\" \"https://YOURWATSONAPIURLHERE/v3/tone?version=2017-09-21&text=" + tweetStringSerialized +"\"").read()
                    OutputToJSON = json.loads(WatsonOutput)
        
                    # Create csv format - classify to place if not present put 0
                    tweet = []
                    for tone in tone_list:
                        found = False

                        # Linear search in tone list
                        for item in OutputToJSON['document_tone']['tones']:
                            # Tone was found, add tone score
                            if item['tone_id'] == tone:
                                found = True
                                tweet.append(item['score'])

                        # Tone was not found
                        if found == False:
                            tweet.append(0)

                    # Save to the csv
                    writer.writerow(map(lambda x: x, tweet))

                except Exception:
                    pass


