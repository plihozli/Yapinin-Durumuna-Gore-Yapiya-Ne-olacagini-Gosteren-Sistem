import pandas as pd
import numpy as np
Z=0
veri = pd.read_csv("Kitap3.csv", sep=';',encoding='utf-8')
y = pd.DataFrame(veri,columns=["bolge","katsayi"])
print(y["katsayi"])
Z=y["katsayi"][1]+30
print(Z)