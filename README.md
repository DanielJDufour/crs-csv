# crs-csv
Python Code to Create a CSV of Coordinate Reference System Information, including EPSG Code, WKT, ESRI WKT, Proj String, Proj4js String, etc.

# why?
There are several different ways to get CRS information, but none seems to be both easily accessible and include ESRI WKT.

# approach
1) Run local instance of epsg.io using docker
2) Query gml.sqlite to get list of every CRS with EPSG code
3) Scrape info from the HTML page for each EPSG code instead of using API because the API doesn't include ESRI WKT
4) Save scraped information to a simple CSV
5) Upload CSV to S3

# nuances
- could consider using https://github.com/Esri/projection-engine-db-doc/tree/master/json instead of epsg.io for ESRI WKT because it should be more official

# support
Post an issue!
