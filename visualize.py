import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from database import engine

df = pd.read_sql_table("DTP", con=engine,)
msk = df.query("35 < longitude < 39 and 55 < latitude < 57")
gdf = gpd.GeoDataFrame(msk, geometry=gpd.points_from_xy(msk.longitude, msk.latitude))
ax = gdf.plot(markersize=1)
gjs = gpd.read_file("data/zel.geojson")
gjs.plot()
plt.show()
