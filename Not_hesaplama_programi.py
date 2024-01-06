def not_hesapla(satir):
    # Satırın sonundaki newline karakterini kaldır
    satir = satir[:-1]

    # Satırı virgül (,) karakterine göre ayır ve listede sakla
    liste = satir.split(",")

    # Öğrencinin ismi ve notları
    isim = liste[0]
    not1 = float(liste[1])
    not2 = float(liste[2])
    not3 = float(liste[3])

    # Notları kullanarak genel notu hesapla
    son_not = (not1 * 0.3) + (not2 * 0.4) + (not3 * 0.4)

    # Nota göre harf notunu belirle
    if son_not > 90:
        harf = "AA"
    elif son_not > 85:
        harf = "AB"
    elif son_not > 80:
        harf = "BB"
    elif son_not > 75:
        harf = "BC"
    elif son_not > 70:
        harf = "CC"
    elif son_not > 65:
        harf = "CD"
    elif son_not > 60:
        harf = "DD"
    elif son_not > 50:
        harf = "DE"
    elif son_not > 45:
        harf = "EE"
    else:
        harf = "FF"

    # İsim ve harf notunu birleştirip döndür
    return isim + "----------------> " + harf + "\n"

# Dosyayı okuyup, notları hesaplayarak yeni bir listeye ekleyin
with open("dosya.txt", "r", encoding="utf-8") as file:
    eklenecek = []
    for i in file:
        eklenecek.append(not_hesapla(i))
    print(eklenecek)

# Yeni listeyi kullanarak dosyayı güncelleyin
with open("dosya.txt", "w", encoding="utf-8") as file2:
    for i in eklenecek:
        file2.write(i)
