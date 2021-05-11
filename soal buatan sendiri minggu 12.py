# Aloysius Gonzaga Ardhian Krisna Aji
# 71180298

# Taher ingin membuat program menu yang bisa mencari nilai irisan, Selisih, dan komplomen 
# sebagai temannya bantulah taher untuk menyelesaikan permasalahannya di atas 

loop = True
while loop:
    print("Mencari nilai dari 2 himpunan")
    print("1. Selisih")
    print("2. Irisan")
    print("3. Komplomen")
    print("4. Exit")
    menu = int(input("masukan pilihan: "))
    if menu == 1:
        angka1 = input("masukan himpunan A: ")
        angka2 = input("masukan himpunan B: ")
        angka1 = set(angka1)
        angka2 = set(angka2)
        gabung = []
        gabung = sorted(angka1.difference(angka2))
        print(gabung)
    elif menu == 2:
        angka1 = input("masukan himpunan A: ")
        angka2 = input("masukan himpunan B: ")
        angka1 = set(angka1)
        angka2 = set(angka2)
        gabung = []
        gabung = sorted(angka1.intersection(angka2))
        print(gabung)
    elif menu == 3:
        angka1 = input("masukan himpunan A: ")
        angka2 = input("masukan himpunan B: ")
        angka1 = set(angka1)
        angka2 = set(angka2)
        gabung = []
        gabung = sorted(angka1.symmetric_difference(angka2))
        print(gabung)
    elif menu == 4:
        print("Terimakasih")
        loop = False
    else:
        print("pilihan tidak sesuai")
        loop = True