# Bankamatik Uygulaması

# Hesap bilgileri tutulacak. (dictionary)
# menu, paraCekme, bakiyeSorgula, paraYatirma fonksiyonları tanımlanacak.
# çekilmek istenen tutar hesapta yoksa ek hesabın kullanılmak istendiği sorulacak.

hesap = {"ad": "Melis Yalçın", "hesapNumarası": "12345678", "bakiye": 9000, "ekHesap": 5000}

def menu():
    print("\n--- Bankamatik Uygulaması ---")
    print("1. Bakiye Sorgula")
    print("2. Para Yatırma")
    print("3. Para Çekme")
    print("4. Çıkış")
    return input("Lütfen yapmak istediğiniz işlemi seçin: ")


def bakiye_sorgulama(hesap):
    print(f"\n{hesap["ad"]} - Hesap Numarası: {hesap["hesapNumarası"]}")
    print(f"Bakiye: {hesap["bakiye"]} TL")
    print(f"Ek Hesaptaki Bakiye: {hesap["ekHesap"]} TL")


def para_yatirma(hesap):
    miktar= float(input("Lütfen yatırmak istediğiniz tutarı girin: "))
    hesap["bakiye"] += miktar
    print(f"{miktar} Paranız başarıyla yatırıldı. Güncel bakiye: {hesap["bakiye"]}")


def para_cekme(hesap):
    miktar=float(input("Çekmek istediğiniz tutarı yazınız: "))

    if miktar <= hesap["bakiye"]:
        hesap["bakiye"] -= miktar
        print(f"{miktar} Parnızı alabilirsiniz. Güncel bakiye: {hesap["bakiye"]} TL")
    else:
        toplam_bakiye = hesap["bakiye"] + hesap["ekHesap"]
        if miktar <= toplam_bakiye:
            ek_hesap_kullan=input("Hesap bakiyeniz yetersiz. Ek hesabınızı kullanmak ister misiniz? (e/h): ").lower()
            if ek_hesap_kullan == "e":
                ek_hesap_kullanilan = miktar - hesap["bakiye"]
                hesap["bakiye"]=0
                hesap["ekHesap "] -= ek_hesap_kullanilan
                print(f"{miktar} TL başarıyla çekilmiştir. Güncel ek hesap bakiyesi:{hesap["ekHesap"]} TL")
            else:
                print("İşleminiz iptal edildi. Yetersiz bakiye.")
        else:
            print("Yetersiz bakiye. İşleminiz gerçekleştirelemedi.")




def main():
    print("Bankamatik Uygulamasına Hoş Geldiniz. ")
    while True:
        secim=menu()

        if secim == "1":
            bakiye_sorgulama(hesap)
        elif secim == "2":
            para_yatirma(hesap)
        elif secim == "3":
            para_cekme(hesap)
        elif secim == "4":
            print("Çıkış yapılıyor. İyi günler dileriz.")
            break
        else:
            print("Hatalı bir seçim yaptınız. Lütfen tekrar deneyiniz.")

if __name__ == "__main__":
    main()
            
            
