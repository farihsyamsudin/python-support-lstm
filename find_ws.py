import pandas as pd
import numpy as np
from scipy.interpolate import LinearNDInterpolator

# Baca data kecepatan angin
data_angin = pd.read_csv('datas/output_clean.csv')

# Baca data koordinat baru
data_koordinat_baru = pd.read_csv('random_points_fix.csv')

# Ekstrak waktu, kecepatan angin dan koordinat
waktu = data_angin['waktu']
kecepatan_angin = data_angin[['ws1', 'ws2', 'ws3']].values
lat = data_angin[['lat1', 'lat2', 'lat3']].values
lon = data_angin[['lon1', 'lon2', 'lon3']].values

# Siapkan array untuk hasil interpolasi
kecepatan_angin_interpolasi = []

# Interpolasi untuk setiap timestamp
for i in range(len(waktu)):
    # Titik asli dengan sedikit jitter
    titik_asli = np.array([lat[i], lon[i]]).T + np.random.normal(0, 1e-5, (3, 2))
    # Kecepatan angin asli
    kecepatan_asli = kecepatan_angin[i]
    
    # Koordinat baru
    koordinat_baru = data_koordinat_baru[['lat', 'lon']].values
    
    # Interpolasi menggunakan LinearNDInterpolator
    interpolator = LinearNDInterpolator(titik_asli, kecepatan_asli)
    interpolasi = interpolator(koordinat_baru)
    
    # Simpan hasil interpolasi
    kecepatan_angin_interpolasi.append(interpolasi)

# Ubah hasil interpolasi menjadi DataFrame
hasil_interpolasi = pd.DataFrame(kecepatan_angin_interpolasi, columns=[f'point_{i}' for i in range(len(data_koordinat_baru))])

# Tambahkan kolom waktu
hasil_interpolasi.insert(0, 'waktu', waktu)

# Simpan hasil interpolasi ke file CSV
hasil_interpolasi.to_csv('hasil_interpolasi.csv', index=False)