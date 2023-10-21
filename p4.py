import numpy as np
import pandas as pd
import time, warnings
import datetime as dt
from datetime import timedelta

df_nasabah_awal = pd.read_excel("nasabah_bandung_asli.xlsx")
df_nasabah_awal.head(10)

pd.options.display.float_format = "{:,.2f}".format

df_nasabah = df_nasabah_awal[['acno', 'name', 'blcur', 'csno', 'open', 'brcod', 'loc', 'sts']]
df_nasabah.head()

#group by two columns and count occurrences
df_rekap = df_nasabah.groupby(['loc']).size().reset_index(name='Count')

#change.columns
df_rekap.columns = ['Lokasi', 'Jml Rekening']

print(df_rekap)