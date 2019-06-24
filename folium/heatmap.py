from folium import plugins
#9814,2007-02-18 00:00:13,121.422800,31.225600, 24, 22,0
import folium
import os
import numpy as np
import pandas as pd
import os
dir = os.listdir(r".\shanghai-taxi-070218-example")
dir = [os.path.join(".\shanghai-taxi-070218-example", x) for x in dir]
def get_loc(path):
    taxi=pd.read_csv(path,sep=",",header=None)
    taxi.columns=["id","time","lat","lon","p","pp","dd"]
    taxi=taxi[["lon","lat"]]
    taxi=taxi.values
    return taxi
loc=[get_loc(path) for path in dir]
data=np.concatenate(loc,axis=0)
data=np.round(data,decimals=1)
map = {}
for d in data:
    d=str(d)
    if d in map.keys():
        map[d] = map[d] + 1
    else:
        map[d] = 1
print(len(map.keys()))
loc_count=list()
def parse_key(map):
    for key in map.keys():
        temp=list()
        temp_key=key.split(sep=" ")
        lon=float(temp_key[1])
        lat=float(temp_key[-1].split("]")[0])
        temp.append(lon)
        temp.append(lat)
        temp.append(map[key])
        loc_count.append(temp)
    return loc_count
loc_count=parse_key(map)
loc_count=np.array(loc_count)
print(np.mean(loc_count,axis=0))
import pandas as pd
import folium
from folium.plugins import HeatMap
map_osm = folium.Map(location=[31.14,121.5],zoom_start=5)    #绘制Map，开始缩放程度是5倍
HeatMap(loc_count).add_to(map_osm)  # 将热力图添加到前面建立的map里
file_path = r"./people.html"
map_osm.save(file_path)     # 保存为html文件
