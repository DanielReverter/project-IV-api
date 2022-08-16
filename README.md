# Project 4: API

By runing the main.py python file a API is created using flask. It gathers the data from 3 million tweets related to Tesla from 2018 to 2020. Some queries can be done through endpoints which will be explained in detail later. There is alse an endpoint that can be used to add more tweets to the database.

### Main Endpoint page for the API query: 
        http://127.0.0.1:5000/  

### 1 - Endpoint route for getting all dates:
The endpoint to get a list of all the dates on which there is some tweets in the database is the following:

        http://127.0.0.1:5000/dates 

### 2 - Endpoint route for all tweets in a particular date:
The following endpoint gets all tweets of a particular day:

        http://127.0.0.1:5000//date/<date>/

Note: < date > is the particular date, written in YYYY-MM-DD format


### 3 - Endpoint route for one translated tweet on a particular date:
Changing en (meaning english) to any other language (for example es for spanish), through this endpoint you can get a random tweet from a particular day translated to any language. The query will still show the original language.

        http://127.0.0.1:5000/translate/<date>?language='en'

### 4 - Endpoint route for posting a new entry through API:
To post a new tweet use the POST section of the "Get and POST in API.ipynb" file, changing the date, tweet and language to the actual details of the tweet to post.

        http://127.0.0.1:5000/newtweet/

### 5 - Endpoint route for deleting all tweets in a particular date:
To delete all tweets from a day use the second block of code in the POST section of the "Get and POST in API.ipynb" file, changing the date to the wanted date to delete.

        http://127.0.0.1:5000/deleteday/