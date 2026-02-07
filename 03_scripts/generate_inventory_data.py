import pandas as pd
import numpy as np

np.random.seed(42)

dates = pd.date_range(start="2024-01-01", end="2024-06-30")
products = ["Pertalite", "Pertamax", "Solar"]
warehouses = ["Depot Lampung", "Depot Palembang"]

data = []

for date in dates:
    for wh in warehouses:
        for prod in products:
            stok_awal = np.random.randint(5000, 15000)
            stok_masuk = np.random.randint(1000, 5000)
            stok_keluar = np.random.randint(2000, 6000)
            lead_time = np.random.randint(1, 5)

            data.append([
                date, wh, prod,
                stok_awal, stok_masuk, stok_keluar,
                lead_time
            ])

df = pd.DataFrame(data, columns=[
    "Tanggal", "Gudang", "Produk",
    "Stok_Awal", "Stok_Masuk", "Stok_Keluar",
    "Lead_Time_Hari"
])

df.to_csv("../02_data/raw/inventory_raw.csv", index=False)

print("Inventory data generated successfully.")
