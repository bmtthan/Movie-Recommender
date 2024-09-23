# Movie-Recommender
## Overview 
The files contain data for all 45,000 movies listed in Full MovieLens. The dataset includes movies released on or before July 2017. Data points include cast, crew, script keywords, budget, revenue, poster, release date, language, production company, country, TMDB rating, and average rating.

The dataset also contains files with 26 million ratings from 270,000 users for all 45,000 movies. Ratings range from 1-5 and were collected from the official GroupLens website.

## Data

**movies_metadata.csv** : Main movie data file. Contains information about the 45,000 movies that appear in the full MovieLens dataset. Information includes posters, wallpapers, budgets, revenue, release dates, languages, countries, and production companies.

**keywords.csv** : Contains keywords about the plots of the movies in the MovieLens dataset. Represented as a serialized JSON object.

**credits.csv** : Contains information about the cast and crew for all movies. Represented as a serialized JSON object.

**rating_small.csv** : Subset of 100,000 ratings from 700 users on 9,000 movies.


## Building a Recommendation System
### Recommendation based on scaled weighted average and popularity score
![](images/3_1.png)
### Content Based Filtering
### Collaborative Filtering
