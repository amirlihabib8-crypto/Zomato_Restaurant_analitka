import pandas as pd

# Verilənlər bazasının yüklənməsi
df = pd.read_csv("Zomato Restaurant Dataset.csv")

# 1. Dataset haqqında ümumi məlumat
print("=== ÜMUMİ MƏLUMAT ===")
print(df.info())
print("\n" + "="*50 + "\n")

# 2. Şəhərlər üzrə ən bahalı orta qiymət (İlk 5)
print("=== ŞƏHƏRLƏR ÜZRƏ ƏN BAHALI RESTORANLAR ===")
print(df.groupby("City")["Average Cost for two"].mean().sort_values(ascending=False).head())
print("\n" + "="*50 + "\n")

# 3. Mətbəx növlərinə görə ən yüksək reytinqlər (İlk 5)
print("=== MƏTBƏX NÖVLƏRİNƏ GÖRƏ ƏN YÜKSƏK REYTİNQLƏR ===")
print(df.groupby("Cuisines")["Aggregate rating"].mean().sort_values(ascending=False).head())