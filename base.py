import math

# # Alochida uzatkichlar uchun kuchlanishlarni hisoblash funktsiyasi
# def calculate_field_strength(power, gain, frequency, delta, distance):
#     # E = (30 * P * G)^0.5 * (f(Δ) * K / R)
#     E = math.sqrt(30 * power * gain) * (frequency * 1.41 / distance)  # K = 1.41
#     return E

# # Berilgan ma'lumotlar
# P_tasvir = 60  # Tasvir uchun quvvat, kVt
# P_ovoz = 18  # Ovoz uchun quvvat, kVt
# G = 21
# N = 327  # m
# K = 1.41
# f_delta = 1  # Normallashtirilgan ko'paytiruvchi (taxminan 1 deb qabul qilamiz)

# # Telemarkaz masofalari (rl)
# rl_values = [60, 140, 290, 440, 550]

# # Alochida uzatkichlar uchun kuchlanishlar
# E_values_tasvir = []
# E_values_ovoz = []

# # Uzatkichlar uchun kuchlanishlarni hisoblash
# for rl in rl_values:
#     R = math.sqrt(rl ** 2 + N ** 2)
#     E_tasvir = calculate_field_strength(P_tasvir, G, f_delta, K, R)
#     E_ovoz = calculate_field_strength(P_ovoz, G, f_delta, K, R)
#     E_values_tasvir.append(E_tasvir)
#     E_values_ovoz.append(E_ovoz)

# # Maydon kuchlanishini hisoblash
# EYMK_tasvir = math.sqrt(sum([E ** 2 for E in E_values_tasvir]))
# EYMK_ovoz = math.sqrt(sum([E ** 2 for E in E_values_ovoz]))

# # Natijalarni chiqarish
# print("Tasvir uchun EYMK:", EYMK_tasvir)
# print("Ovoz uchun EYMK:", EYMK_ovoz)


# print(math.sqrt(550*550+327*327))

# import numpy as np

# # Berilgan ma'lumotlar
# P = 60000  # Vt
# G = 21
# K = 1.41
# N = 327  # m
# f_delta = 1  # Normallashtirilgan ko'paytiruvchi (taxminan 1 deb qabul qilamiz)

# # Masofa qiymatlari
# rl = np.array([60, 140, 290, 440, 550])

# # Masofani hisoblash
# R = np.sqrt(rl**2 + N**2)

# # Maydon kuchlanishini hisoblash
# E = np.sqrt(30 * P * G) * (f_delta * K / R)

# print(E)
