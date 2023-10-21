import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_terbang = pd.read_csv("penerbangan1.csv", names=['tanggal', 'flight', 'asal', 'tujuan', 'penumpang', 'durasi'])
df_terbang.head()

perhari = df_terbang.groupby('tanggal').sum()
perhari.head()

print("Data Perhari")
print(perhari)
perharitujuan = df_terbang.groupby(['tanggal', 'tujuan']).sum()
perhari.head()

print("Data Perhari Tujuan")
print(perharitujuan)

vipot1 = df_terbang.pivot_table(columns=['tujuan'], values=['penumpang'], index=['tanggal'])
vipot2 = df_terbang.pivot_table(columns=['tujuan'], values=['penumpang'], index=['tanggal'], fill_value=0)
vipot3 = df_terbang.pivot_table(columns=['tujuan'], values=['penumpang'], index=['tanggal'], fill_value=0, aggfunc='count')

print("Vipot")
print(vipot1)
print(vipot2)
print(vipot3)

# Grafik dari vipot1
# sns.lineplot(data=vipot1, dashes=False)
# plt.title('Line Plot dari vipot1')
# plt.xlabel('Tanggal')
# plt.ylabel('Jumlah Penumpang')
# plt.show()

