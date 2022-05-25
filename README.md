# Weather app with flask and angular
 - Python version: 3.7 (3.10 cause CORS problem with flask-cors)
 - Angular 13.3.9
## Todos:
 - Separate endpoints to different files
 - Use typed objects when weather api server sends response
 - Now angular http requests header get jwt token locally
    it would be better to create an interceptor to make it more unified
 - Forecast data stored as a json and now a lot of unnecessary data stored in this file
    reduce stored data would be nicer
 - Store user credentials in database
 - Implement registration form (It is visible on frontend but there is no backend endpoint for)