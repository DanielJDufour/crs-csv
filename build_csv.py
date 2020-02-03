from bs4 import BeautifulSoup
from csv import DictReader, DictWriter, QUOTE_ALL
from math import ceil
from os.path import isfile
from requests import get
from enums import crs_formats, skip_these

fieldnames = ['code'] + crs_formats
delimiter = "\t"

base_url = "http://127.0.0.1:8000"

results_per_page = 10

filename = "crs.csv"

start = 0

# get previous number of crs processed
if isfile(filename):
  print(filename + " already exists")
  with open(filename) as f:
    start = len(list(DictReader(f, delimiter=delimiter)))
    print("start:", start)
else:
  with open(filename, "w") as f:
    DictWriter(f, delimiter=delimiter, fieldnames=fieldnames, quoting=QUOTE_ALL).writeheader()
print("start:", start)

rows = []

crs_index = 0

def clean_text(text):
  return text.strip().replace("&#34;", '"').replace("&#39;","'").replace("&lt;","<").replace("&gt;",">")

for kind in ["CRS-GEOGCRS", "CRS-PROJCRS"]:
  kind_url = base_url + "/?format=json&q=kind:" + kind
  print("kind_url:", kind_url)
  response = get(kind_url)
  print("response:", response)
  data = response.json()
  print("data:", data)
  num_results = data['number_result']
  print("num_results:", num_results)
  num_pages = ceil(num_results / 10)
  print ("num_pages:", num_pages)

  for i in range(num_pages):
    if i % 10 == 0:
      print("on page " + str(i) + " of " + str(num_pages))
      if i != 0:
        break
    data = get(kind_url + "&page=" + str(i+1)).json()
    for crs in data['results']:
      crs_index += 1
      if crs_index >= start:
        code = int(crs['code'])
        print("code:", code)
        code_url = base_url + "/" + str(code)
        page_text = get(code_url).text
        soup = BeautifulSoup(page_text, features="lxml")
        #print("soup:", soup)
        if "fictitious" not in page_text and "s_proj4_text" in page_text and "s_xml" in page_text and "s_gml" in page_text:
          row = {
            'code': code,
            'esriwkt': clean_text(soup.find(id="s_esriwkt_text").text),
            'geoserver': clean_text(soup.find(id="s_geoserver_text").text),
            'gml': clean_text(soup.find(id="s_gml_text").text),
            'mapfile': clean_text(soup.find(id="s_mapfile_text").text),
            'mapnik': clean_text(soup.find(id="s_mapnik_text").text),
            'postgis': clean_text(soup.find(id="s_postgis_text").text),
            'prettywkt': clean_text(soup.find(id="s_html_text").text),
            'proj4': clean_text(soup.find(id="s_proj4_text").text),
            'proj4js': clean_text(soup.find(id="s_proj4js_text").text),
            'wkt': clean_text(soup.find(id="s_wkt_text").text),
            'xml': clean_text(soup.find(id="s_xml_text").text)
          }
          #print("row:", row)
          """
          for crs_format in crs_formats:
            if crs_format in ['esriwkt','geoserver','gml','js','mapfile','mapnik','postgis','prettywkt','proj4','proj4js','sql','wkt','xml']:
              continue

            crs_format_url = code_url + "." + crs_format
            try:
                row[crs_format] = get(crs_format_url).text.strip()
            except Exception as e:
              print("crs_format:", crs_format)
              print("crs_index:", crs_index)
              #print("exception getting " + crs_format_url)
              print(e)
              raise e
          """
          with open(filename, "a") as f:
            DictWriter(f, delimiter=delimiter, fieldnames=fieldnames, quoting=QUOTE_ALL).writerow(row)

print("finished")
