# crs-csv
Tab-Delimited CSV of Coordinate Reference System Information

# download link
https://s3.amazonaws.com/crs.csv/crs.csv.zip

# columns
| name | description | example |
| ---- | ----------- | ------- |
| code | EPSG Code | 3857 |
| esriwkt | ESRI's Version of Well-Known Text | [link](https://epsg.io/3857.esriwkt) |
| geoserver | GeoServer Configuration | [link](https://epsg.io/3857.geoserver) |
| gml | Geography Markup Language ([Wikipedia](https://en.wikipedia.org/wiki/Geography_Markup_Language)) | [link](https://epsg.io/3857.gml) |
| mapfile | Used in Configuring MapServer | [link](https://epsg.io/3857.mapfile) |
| mapnik | Used in Configuring Mapnik | [link](https://epsg.io/3857.mapnik) |
| postgis | Used in PostgreSQL/PostGIS | [link](https://epsg.io/3857.sql) |
| prettywkt | Well-Known Text with New Lines and Indentation | [link](https://epsg.io/3857.prettywkt) |
| proj4 | Very popular representation, used by GDAL | [link](https://epsg.io/3857.proj4) |
| proj4js | Used by [proj4js](http://proj4js.org/) for client-side conversion | [link](https://epsg.io/3857.js) |
| xml | Description forthcoming | [link](https://epsg.io/3857.xml) |
| wkt | Well-Known Text ([Wikipedia](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry)) | [link](https://epsg.io/3857.wkt) |

# why?
There are already several different ways to get information on coordinate reference systems, but none seems to be provide it both in an easy format and include ESRI WKT.

# approach
Scrape the information from a local instance of epsg.io

# Requirements
To install the Python3 Requirements type:
```bash
pip3 install -r requirements.txt
```

# Test
```bash
python3 -m unittest test.py
```

# Build CSV
```bash
python3 build_csv.py
```

# nuances
- ESRI has released https://github.com/Esri/projection-engine-db-doc/tree/master/json, which we may consider using in the future as the official ESRI WKT source


# support
Post an issue or email daniel.j.dufour@gmail.com
