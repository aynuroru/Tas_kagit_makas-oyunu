import random

def tas_kagit_makas_AYNUR_ORUCOGLU(): 
    
    def oyun_tanitimi():
        print("""MERHABA, TAŞ-KAĞIT-MAKAS OYUNUMUZA HOŞ GELDİNİZ
              OYUNUN KURALLARI
              1-TAŞ MAKASI YENER.
              2-KAĞIT TAŞI YENER.
              3-MAKAS KAĞIDI YENER
        İLK İKİ TURU KAZANAN OYUNUN GALİBİ OLUR.
                    """)
    def secimler(oyuncu1,oyuncu2):
        if oyuncu1==oyuncu2:
            return "berabere"
        elif (oyuncu1=="taş" and oyuncu2=="makas") or( oyuncu1=="kağıt" and oyuncu2=="taş") or (oyuncu1=="makas" and oyuncu2=="kağıt"):
            return oyuncu1
        else:
            return oyuncu2
            
    def oyun():
        
        liste=["taş","kağıt","makas"]
        oyun_sayisi=0
        tur_sayisi=0
        oyuncu_tur_galibiyeti=0
        bilgisayar_tur_galibiyeti=0
        
        while True:
            print(f" {oyun_sayisi+1}.oyun başlıyor ")
            oyuncu_galibiyeti=0
            bilgisayar_galibiyeti=0

            
            while oyuncu_tur_galibiyeti<2 and bilgisayar_tur_galibiyeti<2 :
                
                print(f" {tur_sayisi+1}.tur başlıyor ")
                oyuncu=input("Taş, kağıt, makas? \n")
                bilgisayar=random.choice(liste)
                
                if oyuncu not in liste:
                    print("Hatalı giriş yaptınız tekrar deneyiniz.")
                    continue
                
                sonuc=secimler(oyuncu, bilgisayar)
                
                if sonuc==oyuncu:
                    print(" Bu turun galibi sizsiniz")
                    oyuncu_tur_galibiyeti+=1
                
                elif sonuc==bilgisayar:
                    print("Bu turun galibi bilgisayar.")
                    bilgisayar_tur_galibiyeti+=1
                
                else:
                    print("Bu tur berabere.")
                
                print(f"Skor: {oyuncu_tur_galibiyeti}-{bilgisayar_tur_galibiyeti}")
                tur_sayisi+=1
                
            if oyuncu_tur_galibiyeti==2:
                oyuncu_galibiyeti+=1
                print("Bu oyunu kazandınız tebrikler.")
            elif bilgisayar_tur_galibiyeti==2:
                bilgisayar_galibiyeti+=1
                print("Bu oyunu bilgisayar kazandı.")
            oyun_sayisi+=1
            
            sec=input("Oyun oynamaya devam etmek istiyorsanız evet yazınız.")
            
            if sec=="evet":
                continue
            elif sec=="hayır":
                print("Oyun bitti")
                print(f"oyun sayısı:{oyun_sayisi}")
                print(f" Genel skor:\n oyuncu:{oyuncu_galibiyeti}\n bilgisayar:{bilgisayar_galibiyeti}")
                break
            else:
                print("Hatalı giriş yaptınız.")
                
                
                
            
    
    
    oyun_tanitimi()
    oyun()
            
tas_kagit_makas_AYNUR_ORUCOGLU()
            
        

























    