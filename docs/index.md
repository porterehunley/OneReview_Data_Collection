# Labeling YouTube Data

In order to train the model, we need labeled data. The goal is to have a ML model that can parse out a numerical score from the transcript of the video. Before the model can be created, though, we need to have exmaples for it to learn from. 

## Goal

Right now, there are 5 years of the IMDb top 50 movies. The application collects comments, transcripts, likes, etc. from YouTube for each of those movies, about 5 videos. This means for 250 movies there 5 video reviews for each of those movies, so 1250 peices of data that need to be labeled.

## Labeling App  

[Website](http://3.210.43.88/) (http://3.210.43.88/) Username: porter Password: porter 

Upon login you should see a webpage with 'Data Control Center' at the header. There is a box of movie titles to the left of the screen that contains the top 50 movies for the year at the top. The movies are highlighted as either green(collected) or Red(not collected). 

On the right side of the screen there should be a myriad of buttons and two text boxes. DONT TOUCH "START DATA COLLECTION" as that might crash the website because it's completely broken. On that note, this website is very fragile and is literally hosted on my old desktop in my parents house so please dont try and break it.

## Parsing Scores

I think we should give a movie a score of 1-5. It is up to you to decide what number in 1-5 to give a movie from the reviewer's score. For example, if a reviewer says "best movie ever go an watch it" probably give it a 5. 

IF the video provided by the website is NOT a movie review (trailer or something idk) mark it with -1

IF the video provided by the website is a movie review FOR A DIFFERENT MOVIE mark it with a -1 

## How to Label

* Select on a movie on the left hand side.
* If movie is red click 'Add Entry'. Should pop up as green after a few seconds OR give an error. IF it gives an error, THATS OK. Continue to the next step anyways.
* Click 'View Video Components'. This should prompt 5 new text boxes and the video titles above them. These correspond to youutbe videos
* Find the videos on youtube. Make sure the titles match exactly.
* Skip to the 'scoring' part and parse out the score acording to the above guidelines.
* Type in the score into the text box for that video 
* Click 'Submit Scores'

NOTE if there are labels for all the movies for that year, type in a year from 2014-2018 in the text box marked 'set year' and hit the 'Get Year' button. All the entries should update.

