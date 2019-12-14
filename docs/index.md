# Labeling YouTube Data

In order to train the model, we need labeled data. The goal is to have a ML model that can parse out a numerical score from the transcript of the video. Before the model can be created, though, we need to have exmaples for it to learn from. 

## Goal

Right now, there are 5 years of the IMDb top 50 movies. The application collects comments, transcripts, likes, etc. from YouTube for each of those movies, about 5 videos. This means for 250 movies there 5 video reviews for each of those movies, so 1250 peices of data that need to be labeled.

## The File

The csv file has four columns: "Title of video", "Title of Movie", "Body 1", and "Body 2"

I am not sure why, but some of the movies have their captions split into 2 columns. 

The main problem with the file is that the captions are collected automatically and so are not perfect by any means. The english is broken and hard to read. If you find that the captions are too broken, MARK IT WITH A -3,

## Parsing Scores

I think we should give a movie a score of 1-5. It is up to you to decide what number in 1-5 to give a movie from the reviewer's score. For example, if a reviewer says "best movie ever go an watch it" probably give it a 5. 

IF the video provided by the website is NOT a movie review (trailer or something idk) MARK IT WITH A -1

IF the video provided by the website is a movie review FOR A DIFFERENT MOVIE MARK IT WITH A -2 

## How to Label 

* Add in a column, call it "Score", and put the scores there.

## FAQ

Just contact me!
