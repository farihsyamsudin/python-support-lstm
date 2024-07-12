import numpy as np
import folium
from scipy.spatial import Delaunay
import pandas as pd

# Koordinat tiga titik pesisir
coords = np.array([
    [-5.918889, 105.9853],
    [-5.869293, 105.755],
    [-6.014822, 105.951525]
])

# Fungsi untuk menghasilkan titik-titik acak dalam segitiga
def random_points_in_triangle(triangle, num_points):
    r1 = np.random.rand(num_points)
    r2 = np.random.rand(num_points)
    r1_sqrt = np.sqrt(r1)
    points = (1 - r1_sqrt).reshape(-1, 1) * triangle[0] + (r1_sqrt * (1 - r2)).reshape(-1, 1) * triangle[1] + (r1_sqrt * r2).reshape(-1, 1) * triangle[2]
    return points

# Melakukan triangulasi Delaunay
tri = Delaunay(coords)

# Menghasilkan titik-titik acak di dalam triangulasi
num_points = 50
points = []
for simplex in tri.simplices:
    triangle = coords[simplex]
    points.extend(random_points_in_triangle(triangle, num_points // len(tri.simplices)))

# Mengonversi hasil ke array numpy
points = np.array(points)

# Membuat peta folium
m = folium.Map(location=[np.mean(coords[:, 0]), np.mean(coords[:, 1])], zoom_start=10)

# Menambahkan titik-titik interpolasi ke peta
for point in points:
    folium.Marker(location=[point[0], point[1]]).add_to(m)

# Menambahkan titik-titik pesisir utama ke peta
for coord in coords:
    folium.Marker(location=[coord[0], coord[1]], icon=folium.Icon(color='red')).add_to(m)

# Menyimpan peta ke file HTML
m.save('random_points_in_triangle_map.html')

# Menyimpan titik-titik ke file CSV
df = pd.DataFrame(points, columns=['lat', 'lon'])
df.to_csv('random_points.csv', index=False)

m