# language: python
# imports: 
    - tweepy(twitter API interaction)
    - numpy(averaging data and array formation in dataframe)
    - pandas(dataframe and organization)
    - matplotlib(visualizing time series information based off of tweets in GUI)
    - textblob(text sentiment analysis)

# overview    
-this imports tweets from a specified user and intakes a specified number of their most recent tweets, removes special characters and processes the text through textblob. Textblob has a built in, pretrained, sentiment analysis model,and outputs a gauge of positive or negative polarity along with an objectiveness ranking. This information along with a number of the multiple data metrics that the tweet objects contain can be assimilated and analyzed using the outline set up on here. There are pre set pathways to output the pandas dataframe to a text file in the root directory and also a partial outline for a matplotlib GUI time series visualization.

-make sure you install all dependencies/requirements and execute with "python tweepy_streamer.py"
