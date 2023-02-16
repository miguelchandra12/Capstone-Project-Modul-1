listBuku = [
    {
        'ID_Buku': 'Buku_1',
        'Stok_Buku': 50,
        'Harga_Pinjam': 10000
    },
    {
        'ID_Buku': 'Buku_2',
        'Stok_Buku': 40,
        'Harga_Pinjam': 15000
    },
    {
        'ID_Buku': 'Buku_3',
        'Stok_Buku': 25,
        'Harga_Pinjam': 20000
    }
]

def menampilkanDataBuku() :
    while True:
        pilihanMenuPenampilan = input('''
            List Menu :
            1. Menampilkan Seluruh Data
            2. Menampilkan Data Tertentu
            3. Kembali Ke Menu Utama

            Masukkan angka Menu yang ingin dijalankan : ''')
    
        if pilihanMenuPenampilan == '1':
            if listBuku == []:
                print("Tidak ada data")
            for i, val in enumerate(listBuku):
                print(f"{i+1}. ID_Buku: {listBuku[i]['ID_Buku']}, Stok_Buku: {listBuku[i]['Stok_Buku']}, Harga_Pinjam: {listBuku[i]['Harga_Pinjam']}")
            continue


        elif pilihanMenuPenampilan == '2':
            found = False
            ID_Buku = input('Masukkan ID_Buku: ')
            for buku in listBuku:
                if buku['ID_Buku'] == ID_Buku:
                    print(f"ID_Buku : {buku['ID_Buku']}, Stok_Buku: {buku['Stok_Buku']}, Harga_Pinjam: {buku['Harga_Pinjam']}")
                    found = True 
                    break
                
            if found == False:
                print("Tidak ada buku dengan ID_Buku tersebut")
            continue
            
        elif pilihanMenuPenampilan == '3':
            break

        else:
            print("Pilihan yang anda masukkan salah")
        
def menciptakanDataBuku():
    while True:
        pilihanMenuPenciptaan = input('''
            List Menu :
            1. Menciptakan Data Baru
            2. Kembali Ke Menu Utama

            Masukkan angka Menu yang ingin dijalankan : ''')

        if pilihanMenuPenciptaan == '1':
            found = False
            ID_Buku = input('Masukkan ID_Buku: ')
            for buku in listBuku:
                if buku['ID_Buku'] == ID_Buku:
                    found = True
                    print("Buku dengan ID_Buku tersebut telah ada")
                    break
            
            if found == False:
                StokBuku = input('Masukkan Stok_Buku: ')
                HargaPinjam = input('Masukkan Harga_Pinjam: ')
                Konfirmasi = input("Apakah anda telah yakin dengan penciptaan data ini?(Yes/No)")
                if Konfirmasi == "Yes":
                    listBuku.append({'ID_Buku':ID_Buku, 'Stok_Buku':StokBuku, 'Harga_Pinjam':HargaPinjam})
                    print("Data telah sukses ditambahkan")
                elif Konfirmasi == "No":
                    continue
                else:
                    print("Pilihan yang anda masukkan salah")
            continue

        elif pilihanMenuPenciptaan == '2':
            break 
        
        else:
            print("Pilihan yang anda masukkan salah")

def mengupdateDataBuku():
    while True:
        pilihanMenuUpdate = input('''
            List Menu :
            1. Mengupdate Data
            2. Kembali Ke Menu Utama

            Masukkan angka Menu yang ingin dijalankan : ''')
        
        if pilihanMenuUpdate== '1':
            found = False
            ID_Buku = input('Masukkan ID_Buku: ')
            for buku in listBuku:
                if buku['ID_Buku'] == ID_Buku:
                    found = True
                    print(f"ID_Buku : {buku['ID_Buku']}, Stok_Buku: {buku['Stok_Buku']}, Harga_Pinjam: {buku['Harga_Pinjam']}")
                    Kolom_Update = input("Kolom mana yang mau diubah?(ID_Buku/Stok_Buku/Harga_Pinjam)")
                    if Kolom_Update == 'ID_Buku':
                        ID_Buku_Baru = input("Masukkan ID_Buku baru: ")
                        Konfirmasi = input("Apakah anda yakin ingin mengubah value ID_Buku?(Yes/No)")
                        if Konfirmasi == "Yes":
                            buku['ID_Buku'] = ID_Buku_Baru 
                            print("Data telah berhasil diubah")
                        elif Konfirmasi == "No":
                            continue 
                        else:
                            print("Pilihan yang anda masukkan salah")
                 
                    elif Kolom_Update == 'Stok_Buku':
                        Stok_Buku_Baru = input("Masukkan Stok_Buku baru: ")
                        Konfirmasi = input("Apakah anda yakin ingin mengubah value Stok_Buku?(Yes/No)")
                        if Konfirmasi == "Yes":
                            buku['Stok_Buku'] = Stok_Buku_Baru 
                            print("Data telah berhasil diubah")
                        elif Konfirmasi == "No":
                            continue 
                        else:
                            print("Pilihan yang anda masukkan salah")

                    if Kolom_Update == 'Harga_Pinjam':
                        Harga_Pinjam_Baru = input("Masukkan Harga_Pinjam baru: ")
                        Konfirmasi = input("Apakah anda yakin ingin mengubah value Harga_Pinjam?(Yes/No)")
                        if Konfirmasi == "Yes":
                            buku['Harga_Pinjam'] = Harga_Pinjam_Baru 
                            print("Data telah berhasil diubah")
                        elif Konfirmasi == "No":
                            continue 
                        else:
                            print("Pilihan yang anda masukkan salah")

            if found == False:
                print("Data ID_Buku tersebut tidak ada")
            continue

        elif pilihanMenuUpdate == '2':
            break

        else:
            print("Pilihan yang anda masukkan salah")

def menghapusDataBuku():
    while True:
        pilihanMenuUpdate = input('''
            List Menu :
            1. Menghapus Data
            2. Kembali Ke Menu Utama

            Masukkan angka Menu yang ingin dijalankan : ''')
        
        if pilihanMenuUpdate== '1':
            found = False
            ID_Buku = input('Masukkan ID_Buku: ')
            for i, val in enumerate(listBuku):
                if ID_Buku == listBuku[i]['ID_Buku']:
                    found = True
                    Konfirmasi = input("Apakah anda yakin ingin menghapus value ID_Buku?(Yes/No)")
                    if Konfirmasi == "Yes":
                        del listBuku[i]
                        print("Data telah berhasil dihapus")
                    elif Konfirmasi == "No":
                        continue 
                    else:
                        print("Pilihan yang anda masukkan salah")
            
            if found == False:
                print("Data ID_Buku tersebut tidak ada")
            continue

        elif pilihanMenuUpdate == '2':
            break

        else:
            print("Pilihan yang anda masukkan salah")

while True :
    pilihanMenu = input('''
        Selamat Datang di Perpustakaan

        List Menu :
        1. Read Data
        2. Create Data
        3. Update Data
        4. Delete Data
        5. Exit Program

        Masukkan angka Menu yang ingin dijalankan : ''')

    if(pilihanMenu == '1') :
        menampilkanDataBuku()

    elif(pilihanMenu == '2'):
        menciptakanDataBuku()

    elif(pilihanMenu == '3'):
        mengupdateDataBuku()
    
    elif(pilihanMenu == '4'):
        menghapusDataBuku()

    elif(pilihanMenu == '5') :
        break
    else:
        print("Pilihan yang anda masukkan salah")
    
