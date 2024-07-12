import pandas as pd

# Membaca data dari file
file_path = 'datas/data.csv'  # Ganti dengan path file Anda
data = pd.read_csv(file_path, delimiter=',')

# Menentukan kolom baru untuk output
output_columns = ['waktu', 'ws1', 'ws2', 'ws3', 'lat1', 'lat2', 'lat3', 'lon1', 'lon2', 'lon3']
output_data = []

# Mengelompokkan data berdasarkan waktu
grouped_data = data.groupby('waktu')

for waktu, group in grouped_data:
    ws = group['windspeed'].tolist()
    lat = group['lat'].tolist()
    lon = group['lon'].tolist()
    
    # Pastikan ada 3 data untuk setiap waktu
    while len(ws) < 3:
        ws.append(None)
        lat.append(None)
        lon.append(None)
    
    output_data.append([waktu, ws[0], ws[1], ws[2], lat[0], lat[1], lat[2], lon[0], lon[1], lon[2]])

# Membuat DataFrame baru dengan data yang telah diubah
output_df = pd.DataFrame(output_data, columns=output_columns)

# Menyimpan ke file baru
output_file_path = 'datas/output.csv'
output_df.to_csv(output_file_path, index=False)

print("Data telah disimpan ke", output_file_path)
