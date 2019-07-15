import numpy as np
import pandas as pd
route=np.load("route_embedding.npy")
b=pd.DataFrame(route)
with open("route.tsv","w") as write_tsv:
    write_tsv.write(b.to_csv(sep="\t",index=False,header=False))
