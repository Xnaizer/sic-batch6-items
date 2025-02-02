input = [
    {'nama' : 'budi', 'gaji' : 1000000},
    {'nama' : 'andi', 'gaji' : 2000000},
    {'nama' : 'tono', 'gaji' : 3000000}
]

gajiTertinggi = max(input, key=lambda x: x['gaji'])
print(gajiTertinggi)

gajiTerendah = min(input, key=lambda x: x['gaji'])
print(gajiTerendah)

totalGajiKaryawan = sum(x['gaji'] for x in input)
print(f"Total gaji karyawan: {totalGajiKaryawan}") 