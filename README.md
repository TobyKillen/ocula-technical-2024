# Ocula Technical 2024

## What I did
* Created 2 endpoints
* Added a workflow in Github
* Unit Tests (PyTest)
  
## What I wish I done
* Cleaned up file types by splitting the network calls from the database calls into different services.
* Added more complex unit tests to test http func etc. 
* Built out the entire database client and talked to a SQL Lite Database.

* Properly Implement Date on the endpoint. I was confused by the open weather api's docs. 

## Further Improvements
* Implement a check to see if the (City / Date) Pair have been requested before so that we're not using our third-party API call costs. 
* Add a pre commit hook into the repo to execute pytests before being pushed to the remote
* Built out the docker file for it to be deployed using kubernetes or alternative solution
* Implemented Routing / Routes into the repo for readability etc. If I was planning to add additional endpoints.
* Added a logging client for logging information around the endpoints etc. 


## Environment Variables
```bash
WEATHER_API_URL = 'http://api.openweathermap.org/data/2.5/forecast/daily?q='
WEATHER_API_ONE_CALL_URL = 'https://api.openweathermap.org/data/3.0/onecall?'
WEATHER_API_KEY = '<YOUR API KEY>'
GEO_LOCATION_API_URL = 'http://api.openweathermap.org/geo/1.0/direct?q='
````
