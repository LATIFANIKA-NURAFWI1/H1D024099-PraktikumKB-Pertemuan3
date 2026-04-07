import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# 1. Variabel Fuzzy
barang_terjual = ctrl.Antecedent(np.arange(0, 101, 1), 'Barang Terjual')
permintaan = ctrl.Antecedent(np.arange(0, 301, 1), 'Permintaan')
harga_peritem = ctrl.Antecedent(np.arange(0, 100001, 1), 'Harga per Item')
profit = ctrl.Antecedent(np.arange(0, 4000001, 1), 'Profit')
stok = ctrl.Consequent(np.arange(0, 1001, 1), 'Stok Makanan')

# 2. Himpunan Fuzzy
# Barang Terjual
barang_terjual['rendah'] = fuzz.trimf(barang_terjual.universe, [0, 0, 40])
barang_terjual['sedang'] = fuzz.trimf(barang_terjual.universe, [30, 50, 70])
barang_terjual['tinggi'] = fuzz.trimf(barang_terjual.universe, [60, 100, 100])

# Permintaan
permintaan['rendah'] = fuzz.trimf(permintaan.universe, [0, 0, 100])
permintaan['sedang'] = fuzz.trimf(permintaan.universe, [50, 150, 250])
permintaan['tinggi'] = fuzz.trimf(permintaan.universe, [200, 300, 300])

# Harga per Item 
harga_peritem['murah'] = fuzz.trimf(harga_peritem.universe, [0, 0, 40000])
harga_peritem['sedang'] = fuzz.trimf(harga_peritem.universe, [30000, 50000, 80000])
harga_peritem['mahal'] = fuzz.trimf(harga_peritem.universe, [60000, 100000, 100000])

# Profit 
profit['rendah'] = fuzz.trimf(profit.universe, [0, 0, 1000000])
profit['sedang'] = fuzz.trimf(profit.universe, [1000000, 2000000, 2500000])
profit['tinggi'] = fuzz.trapmf(profit.universe, [1500000, 2500000, 4000000, 4000000])

# Stok Makanan
stok['sedang'] = fuzz.trimf(stok.universe, [100, 500, 900])
stok['banyak'] = fuzz.trimf(stok.universe, [600, 1000, 1000])

# 3. Rules
rule1 = ctrl.Rule(barang_terjual['tinggi'] & permintaan['tinggi'] & harga_peritem['murah'] & profit['tinggi'], stok['banyak'])
rule2 = ctrl.Rule(barang_terjual['tinggi'] & permintaan['tinggi'] & harga_peritem['murah'] & profit['sedang'], stok['sedang'])
rule3 = ctrl.Rule(barang_terjual['tinggi'] & permintaan['sedang'] & harga_peritem['murah'] & profit['sedang'], stok['sedang'])
rule4 = ctrl.Rule(barang_terjual['sedang'] & permintaan['tinggi'] & harga_peritem['murah'] & profit['sedang'], stok['sedang'])
rule5 = ctrl.Rule(barang_terjual['sedang'] & permintaan['tinggi'] & harga_peritem['murah'] & profit['tinggi'], stok['banyak'])
rule6 = ctrl.Rule(barang_terjual['rendah'] & permintaan['rendah'] & harga_peritem['sedang'] & profit['sedang'], stok['sedang'])

# 4. Control System
stok_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6])
stok_makanan = ctrl.ControlSystemSimulation(stok_ctrl)

inputbrg = input("Masukkan Barang Terjual (0-100) (80): ") or 80
inputpermintaan = input("Masukkan Permintaan (0-300) (255): ") or 255
inputharga = input("Masukkan Harga Per Item (0-100000) (25000): ") or 25000
inputprofit = input("Masukkan Profit (0-4000000) (3500000): ") or 3500000

stok_makanan.input['Barang Terjual'] = int(inputbrg)
stok_makanan.input['Permintaan'] = int(inputpermintaan)
stok_makanan.input['Harga per Item'] = int(inputharga)
stok_makanan.input['Profit'] = int(inputprofit)

stok_makanan.compute()
hasil_stok = stok_makanan.output['Stok Makanan']
print(f"Persediaan Stok Makanan: {hasil_stok:.2f} unit")

stok.view(sim=stok_makanan)
plt.title("Pet Shop")
plt.show()





