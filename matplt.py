import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sb
My_df=pd.read_csv("/home/ahmadreza/Downloads/100 Sales Records.csv")
plt.figure(figsize=(10,10),dpi=100)
plt.title("i need pussy")
plt.xlabel("how to fuck")
plt.ylabel("black guys are slaves")
a=np.linspace(1,10,10)
b=lambda a: [x**2 for x in a]
sb.boxplot(x='Item Type',y='Total Cost', data=My_df , hue="Item Type")
plt.show()

