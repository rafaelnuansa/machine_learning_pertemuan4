import pandas as pd 

df_mk = pd.read_csv("matkul.csv")
df_mk.head()

df_dos = pd.read_csv("dosen.csv")
df_dos.head()

df_join = df_mk.merge(df_dos, left_on='kddosen', right_on='kddosen')
df_join.head()


print(df_join)
