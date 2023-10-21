import numpy as np
import pandas as pd
import time, warnings
import datetime as dt
from datetime import timedelta
import seaborn as sns 
import matplotlib.pyplot as plt

df_nasabah_awal = pd.read_excel("nasabah_bandung_asli.xlsx")
df_nasabah_awal.head(10)

df_nasabah = df_nasabah_awal[['acno', 'name', 'blcur', 'csno', 'open', 'brcod', 'loc', 'sts']]
df_nasabah.head()

#group by two columns and count occurrences
df_rekap = df_nasabah.groupby(['loc']).size().reset_index(name='Count')

#change.columns
df_rekap.columns = ['Lokasi', 'Jml Rekening']

# sns.lineplot(data=df_rekap, x='Lokasi', y='Jml Rekening')  #lineplot 
# sns.barplot(data=df_rekap, x='Lokasi', y='Jml Rekening') #scatter
sns.scatterplot(data=df_rekap, x='Lokasi', y='Jml Rekening')
plt.xlabel('Lokasi')
plt.ylabel('Jumlah Rekening')
plt.title('Grafik Jumlah Rekening Per Lokasi');
plt.savefig('grafik_rekap_lokasi.png')
plt.show()

# print(df_rekap)