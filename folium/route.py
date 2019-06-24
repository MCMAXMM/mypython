from folium import plugins
#9814,2007-02-18 00:00:13,121.422800,31.225600, 24, 22,0
import folium
import os
import numpy as np
import pandas as pd
import os
#color
cnames = [
'aliceblue',
'antiquewhite',
'aqua',
'aquamarine',
'azure',
'beige',
'bisque',
'black',
'blanchedalmond',
'blue',
'blueviolet',
'brown'
,'burlywood'
,'cadetblue'
,'chartreuse'
,'chocolate'
,'coral'
,'cornflowerblue'
,'cornsilk'
,'crimson'
,'cyan'
,'darkgreen'
,'darkkhaki'
,'darkmagenta'
,'darkolivegreen'
,'darkorange'
,'darkorchid'
,'darkred'
,'darksalmon'
,'firebrick'
,'floralwhite'
,'forestgreen'
,'fuchsia'
,'gainsboro'
,'ghostwhite'
,'gold'
,'goldenrod'
,'gray'
,'green'
,'greenyellow'
,'honeydew'
,'hotpink'
,'indianred'
,'indigo'
,'ivory']
dir = os.listdir(r".\shanghai-taxi-070218-example")
dir = [os.path.join(".\shanghai-taxi-070218-example", x) for x in dir]
def get_loc(path):
    taxi=pd.read_csv(path,sep=",",header=None)
    taxi.columns=["id","time","lat","lon","p","pp","dd"]
    taxi=taxi[["lon","lat"]]
    taxi=taxi.values
    return taxi
count=0
for path in dir:
    count+=1
    loc_line=get_loc(path)
    mean=np.mean(loc_line,axis=0)
    break
m = folium.Map(mean, zoom_start=20)  #中心区域的确定
for i,path, in enumerate(dir):
    loc_line = get_loc(path)
    route = folium.PolyLine( loc_line,
        weight=3,
        color=cnames[i],
     opacity=0.8
    ).add_to(m)
#color='orange',
m.save(os.path.join(r'.', 'Heatmap1.html'))  #
