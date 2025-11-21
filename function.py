def hitungNilai (tugas, uts, uas):
    nilaiAkhir = (0.3*tugas) + (0.3*uts) + (0.4*uas)
    
    if nilaiAkhir >= 85:
        grade = 'A'
    elif nilaiAkhir >= 70 and nilaiAkhir <= 84:
        grade = 'B'
    elif nilaiAkhir >= 60 and nilaiAkhir <= 69:
        grade = 'C'
    elif nilaiAkhir >= 50 and nilaiAkhir <= 59:
        grade = 'D'
    elif nilaiAkhir >= 40 and nilaiAkhir <= 49:
        grade = "E"
    ulang = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5}
    for i in range(ulang[grade]):
        print(grade)
        
hitungNilai(78, 67, 75)
