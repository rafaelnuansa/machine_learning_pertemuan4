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


# df_nasabah[df_nasabah['csno'] == 6951313]
# df_nasabah1 = df_nasabah[df_nasabah['blcur'] >= 10000000000]
# df_nasabah1.head()
# df_nasabah[df_nasabah['blcur'] > 50000000000]
# blcur_max = df_nasabah['blcur'].max()
# blcur_max
# # isi data rekap customer jumlah balance dari nasabah
# df_rekap = df_nasabah.groupby(by='csno', as_index=False).agg({'blcur': 'sum'})
# df_rekap.columns = ['csno','balance']
# df_rekap.tail(10)
# # isi data rekap customer jumlah rekeningnya
# df_rekap_rek = df_nasabah.groupby(by='csno', as_index=False).agg({'acno': 'count'})
# df_rekap_rek.columns = ['csno','jumlah_rek']
# df_rekap_rek.head()
# no 2
# df_tugas = df_nasabah_awal[['acno', 'name', 'blcur', 'csno', 'open', 'brcod', 'loc', 'sts']]
# df_nasabah.head()
# no 3 
# df_tugas = pd.read_excel("nasabah_bandung_asli.xlsx")
# df_tugas.head(10)
# df_tugas[df_tugas['acno'] == 124001633]
# df_tugas[df_tugas['sts'] == 1]
# df_tugas[df_tugas['sts'] == 2]
# df_rekap2 = df_tugas.groupby(['brcod','loc','sts'],as_index=False).agg({'blcur': 'count'})
# df_rekap2.columns = ['Cabang','Lokasi', 'Status', 'Jml_Rekening']
# df_rekap2.tail(10)

# print('Rekap Data Nasabah Berdasarkan Cabang, Lokasi, serta Status. \n')
# print(df_rekap2)
# df_rekap2 = df_tugas.groupby(['brcod','loc','sts'],as_index=False).agg({'blcur': 'sum'})
# df_rekap2.columns = ['Cabang','Lokasi', 'Status', 'Total_Saldo']
# df_rekap2.tail(10)

# print('Rekap Data Nasabah Berdasarkan Cabang, Lokasi, serta Status. \n')
# print(df_rekap2)

# df_rekap = df_tugas.groupby(['brcod','loc'],as_index=False).agg({'blcur': 'count'})
# df_rekap.columns = ['Cabang','Lokasi', 'Jml_Rekening']
# df_rekap.tail(10)

# print('Rekap Data Nasabah Berdasarkan Cabang dan Lokasi. \n')
# print(df_rekap)
# df_rekap = df_tugas.groupby(['brcod','loc'],as_index=False).agg({'blcur': 'sum'})
# df_rekap.columns = ['Cabang','Lokasi', 'Total_Saldo']
# df_rekap.tail(10)

# print('Rekap Data Nasabah Berdasarkan Cabang dan Lokasi. \n')
# print(df_rekap)

#group by two columns and count occurrences
df_rekap = df_nasabah.groupby(['loc']).size().reset_index(name='Count')

#change.columns
df_rekap.columns = ['Lokasi', 'Jml Rekening']

print(df_rekap)