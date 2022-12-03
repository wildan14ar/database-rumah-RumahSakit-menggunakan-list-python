pasien1={'nama': 'Luthfi', 'Nomor rekam(id pasien)': 1, 'alamat': 'dino', 'penyakit': 'anemia', 'nomor ruang': 1, 'BPJS' : 'kelas I', 'tanggak masuk': '11-2-3', 'tanggal keluar': '12-4-64'}
pasien2={'nama': 'Noval', 'Nomor rekam(id pasien)': 2, 'alamat': 'jepara', 'penyakit': 'Amnesia', 'nomor ruang': 2, 'BPJS': 'kelas I', 'tanggak masuk': '11-4-2012', 'tanggal keluar': '14-5-2015'}
list_pasien = [pasien1,pasien2]


def linkstart():
    print( "#### RS. GAMELAB INDONESIA #### \n1.Tampilkan Pasien \n2.Tambah Pasien \n3.Ubah Data Pasien \n4.Hapus Pasien \n5.Keluar \n##############################")
    pilihan = int(input("masukkan nomor pilihanmu:"))

    if pilihan == 1:
        print("Tampilkan Pasien")
        if __name__ == '__main__':
            daftar_pasien()
    elif pilihan == 2:
        print("Tamabahkan Pasien")
        if __name__ == '__main__':
            addpasien()
    elif pilihan == 3:
        print("Ubah Data Pasien")
        if __name__ == '__main__':
            ubah_data()
    elif pilihan == 4:
        print("Hapus data Pasien")
        if __name__ == '__main__':
            hapus_data()
    elif pilihan == 5:
        print("Keluar")
    else:
        print("silahkan masukkan ulang nomor anda!")
        return linkstart()

def daftar_pasien():
    for pasien in list_pasien:
        print(*pasien['nama'],'(',pasien['Nomor rekam(id pasien)'],')',end='\n')
    a = int(input('masukkan id pasien untuk melihat detail data pasien: '))
    print(list_pasien[a-1])
    return linkstart()

def addpasien():
    adpasien = {'nama':"nama pasien",'Nomor rekam(id pasien)': 'id pasien', 'alamat':'alamat pasien', 'penyakit':'penyakit pasien', 'nomor ruang':'ruang pasien', 'BPJS':'kelas pasien','tanggak masuk':'masuk pasien',
            'tanggal keluar':'keluar pasien', }
    adpasien['nama'] = input("masukkan nama: ")
    adpasien['Nomor rekam(id pasien)'] = len(list_pasien)+1
    adpasien['alamat'] = input("masukkan alamat: ")
    adpasien['penyakit'] = input("masukkan penyakit: ")
    adpasien['nomor ruang'] = input("masukkan no ruangan: ")
    adpasien['BPJS'] = input("masukkan kelas: ")
    adpasien['tanggak masuk'] = input("tanggal masuk pasien: ")
    adpasien['tanggal keluar'] = input("tanggal keluar pasien: ")
    list_pasien.append(adpasien)
    return linkstart()

def ubah_data():
    x = int(input('masukkan id pasien: '))
    c = x-1
    a = input("## pilih opsi ## \n>nama \n>alamat \n>penyakit \n>no ruang \n>BPJS \n>tanggal masuk \n>tanggal keluar \n############### \nmasukkan pilihan: ")
    b = input('perubahan: ')
    list_pasien[c][a] = b
    return linkstart()

def hapus_data():
    a = int(input('masukkan id pasien: '))
    b = a-1
    del list_pasien[b]
    return linkstart()

if __name__ == '__main__':
    linkstart()