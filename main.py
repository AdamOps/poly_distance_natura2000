import geopandas as gpd
from shapely.geometry import Polygon
import os

# Source URL for geoJSON data
ckan_path = "https://ckan.dataplatform.nl/dataset/1574d290-1e08-42fc-8a7d-fadd0dcabb8f/resource/f6b5090d-ac9b-476c-b9b7-52a382937d2e/download/natura2000.json"

# Make a folder with relevant data.
os.makedirs("natura2000_polygons", exist_ok=True)
if os.path.isfile("natura2000_polygons/area_0.json"):
    poly_0 = gpd.read_file("natura2000_polygons/area_0.json")
    print("Found first polygon")
else:
    poly_0 = None
if os.path.isfile("natura2000_polygons/area_1.json"):
    poly_1 = gpd.read_file("natura2000_polygons/area_1.json")
    print("Found second polygon")
else:
    poly_1 = None

if poly_0 is None or poly_1 is None:
    print("At least one polygon file missing. Regenerating both from source dataset.")
    # Gotta reload the file anyway, so let's just make sure both exist.
    poly_0 = None
    poly_1 = None
    # There are LOADS of polygons in this file. Need to find a better one. Still, we can just grab the top two
    # as an example.
    natura_df = gpd.read_file(ckan_path)
    print("Loaded geojson file")

    for i, row in natura_df.iterrows():
        single_gdf = gpd.GeoDataFrame([row], crs=natura_df.crs)
        save_path = f"natura2000_polygons/area_{i}.json"
        if poly_0 is None:
            poly_0 = single_gdf
            single_gdf.to_file(save_path, driver="GeoJSON")
            continue
        poly_1 = single_gdf
        single_gdf.to_file(save_path, driver="GeoJSON")
        break

# Convert the coordinate system to something compatible with Shapely
# NB: If you use [(lat,lon)] style coordinates, shapely instead gives angles as the distance
poly_0 = poly_0.to_crs(epsg=3857)
poly_1 = poly_1.to_crs(epsg=3857)

# Convert the
poly_0 = Polygon([list(geom.exterior.coords) for geom in poly_0.geometry][0])
poly_1 = Polygon([list(geom.exterior.coords) for geom in poly_1.geometry][0])

# Minimum distance via Shapely
min_distance = poly_0.distance(poly_1)

# Output result
print(f"Minimum distance between polygons: {min_distance:.2f} meters")
