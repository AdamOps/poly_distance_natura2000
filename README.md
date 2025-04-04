# Polygon distance calculator (Natura 2000)
This is an example script which uses shapely to calculate the distance between polygons in meters. The sample script does three things:
1. It fetches data on Natura 2000 regions, which is stored in a JSON file.
2. It picks out the top two polygons from the (rather large) complete JSON file and stores them in separate files.
3. It calculates the distance between these two polygons. If you re-run the script, it loads and parses the smaller GeoJSON files instead of always reloading the big one.

## Run Locally

Clone the project

```bash
  git clone https://github.com/AdamOps/poly_distance_natura2000.git
```

Install dependencies

```bash
  pip install requirements.txt
```

> [!IMPORTANT]
> Double check which CRS you are using in your geometry data. EPSG:3857 works well globally. For local precision, calculate the correct UTM zone.
> Calculating the distance with lat-lon data returns degrees, instead of meters.
