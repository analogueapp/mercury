Data Enrichment Service

We are creating a service for grabbing relevant data from any webpage. Optimization is a major part of this project. Our current appraoch
includes a Flask app that accepts url and returns Open graph tags. This is only valid for sites following the Open Graph protocol.

API is live at: http://enrich-data.herokuapp.com/

How to use: http://enrich-data.herokuapp.com/get?= [add your url here] 

Sample Youtube Video: http://enrich-data.herokuapp.com/get?url=https://www.youtube.com/watch?v=dzqpfu5izjE

Note: First request can take a bit longer as the server sleeps after 30mins of inactivity.
