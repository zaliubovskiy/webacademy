# Task 6 =================================================================================

# ТЗ: Даны входные данные (номера страховых полисов клиентов двух больних (списки):
# Alchemilla Hospital и Brookhaven Hospital).
# Нужно выяснить:
# 1. Сколько клиентов посещают обе больницы
# 2. Сколько клиентов посещают только больницу Alchemilla Hospital
# 3. Сколько клиентов (уникальных страховых полисов) находится в базах данных всех больниц
# Input data: al_hospital = [123, 4325, 3567, 234, 54647, 5663]
# Input data: bh_hospital = [688, 5653, 123, 56778, 234, 4677, 8787]
# # To solve with and without sets

# Developer notes: Решить не применяя set ! :)
# ========================================================================================

al_hospital = [123, 4325, 3567, 234, 54647, 5663]
bh_hospital = [688, 5653, 123, 56778, 234, 4677, 8787]

both_hospitals = 0  # Hom many clients visit both hospitals
only_al_hospital = 0  # How many clients only in Alchemilla Hospital
only_bh_hospital = 0  # How many client only in Brookhaven Hospital

for a in al_hospital:
    for b in bh_hospital:
        if a == b:
            both_hospitals += 1
        else:
            continue

print(f"{both_hospitals} clients visit both hospitals")

for a in al_hospital:
    if a not in bh_hospital:
        only_al_hospital += 1
    else:
        continue

print(f"{only_al_hospital} clients visit only 'Alchemilla' hospital")

for b in bh_hospital:
    if b not in al_hospital:
        only_bh_hospital += 1
    else:
        continue

print(f"{only_al_hospital + both_hospitals + only_bh_hospital} unique visitors of both hospitals")
