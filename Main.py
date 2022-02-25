nama_band  =    [
                'Payung Teduh',
                'Fourtwnty',
                'Dialog Din',
                'Armada',
                'Last Child'
                ]
lagu_band = [
    'Akad',
    'Zona nyaman',
    'Rumahku',
    'Harusnya Aku',
    'Pedih'
]

#enumerate / enumerasi index

for index,band in  enumerate(nama_band):
    print(index,' -> ',band)

print("\n")
#menggabungkan dua list / zip
for band, lagu in zip(nama_band, lagu_band):
    print(band,' judul lagu : ',lagu)

print("\n")
#set
hewanDarat = {'Kucing','Anjing','Monyet','Kuda','Burung'}
for animal in sorted(hewanDarat):
    print(animal)

hewanAir = {'Ikan', 'Paus','Lumba-lumba','Dugong'}

print("\n")
#dictionary
Animal_Profile = {
    "ID" : 11001,
    "Name" : "Tiger",
    "Size" : "Big",
    "Foot" : 4
}

for i,animalScoope in Animal_Profile.items():
    print(i,' - ',animalScoope)

#reversed
for i in reversed(range(1,10,1)):
    print(i)