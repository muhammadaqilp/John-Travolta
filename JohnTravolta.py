jam_normal = 40
gaji_normal = 15000
gaji_lembur = 1.5 * 15000

try:
    jam_kerja = int(input('Jam kerja minggu ini = '))
    if jam_kerja > jam_normal:
        gaji_total = int((jam_normal * gaji_normal) + ((jam_kerja - jam_normal) * gaji_lembur))
    else:
        gaji_total = int(jam_kerja * gaji_normal)

    print('Gaji John Transvolta minggu ini = Rp' + str(gaji_total))

    try:
        pengeluaran = int(input('Pengeluaran John minggu ini = Rp'))
        if gaji_total > pengeluaran:
            print("John BISA MENABUNG sebesar Rp" + str(gaji_total - pengeluaran))
        elif gaji_total == pengeluaran:
            print('John TIDAK BISA MENABUNG')
        else:
            print('John butuh CARI TAMBAHAN')
    except:
        print("Input yang anda masukkan tidak valid")
except:
    print("Input yang anda masukkan tidak valid")