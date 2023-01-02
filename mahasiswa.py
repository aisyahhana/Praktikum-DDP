class Mahasiswa:
    nim = ""
    nama = ""
    rombel = ""

    def welcome(self):
        print("hallo", self.nama, "di STT nurul fikri")

    def __init__(self, nim, nama, rombel):
        self.nim = nim
        self.nama = nama
        self.rombel = rombel
    

    def lulus(self,  nilai):
        if(nilai > 90):
            print ("Lulus")
        else:
            print("tidak lulus")

mhs1 = Mahasiswa("0110222286", "Aisyah Hanani" "TI13")
# mhs1.nama = "Aisyah"
# mhs1.nim = "0110222286"
# mhs1.rombel = "TI13"

print("Nama Mahasiswa", mhs1.nama)
print("NIM Mahasiswa", mhs1.nim)
print("Rombel mahasiswa", mhs1.rombel)
mhs1.lulus(91)