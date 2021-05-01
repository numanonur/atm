import time
hesNo="1111"
passw="aaaa"
bakiye = 0

hesano=input("hesap no giriniz: ")
passwo=input("şifre girin ")

if hesano == hesNo and passw == passwo:
    print("giriş başarılı")
    while True:
        isl = input("""
yapmak istediğiniz işemin kodunu girin.
1.balkiye sorgulamak
2.bakkiye yatırmak
3.bakkiye çekmek
4.havale yapmak
5.çıkış  """ )

        if isl == "1":
            print("hesabınızda {}tl var.".format(bakiye))
        
        elif isl == "2":
            nb=float(input("eklenecek tutarı girin. "))
            bakiye=nb+bakiye
            print("ekleniyor.")
            time.sleep(0.5)
            print("ekleniyor..")
            time.sleep(0.5)
            print("ekleniyor...")
            time.sleep(0.5)
            print("ekleniyor.")
            time.sleep(0.5)
            print("ekleniyor..")
            print("eklendi yeni bakiye {} tl".format(bakiye))
        elif isl == "3":
            ob=float(input("çekilecek tutarı girin. "))
            bakiye=bakiye-ob
            print("para hazırlanıyor.")
            time.sleep(0.5)
            print("para hazırlanıyor..")
            time.sleep(0.5)
            print("para hazırlanıyor...")
            time.sleep(0.5)
            print("para hazırlanıyor.")
            time.sleep(0.5)
            print("para hazırlanıyor..")
            print("çekildi. kalan bakiye {} tl".format(bakiye))
        elif isl == "4":
            ghn=input("gönderilecek hesap nounu giriniz. ")
            mi=float(input("gçnderilecek miktarı giriniz. "))
            bakiye=bakiye-(mi+(mi*1/1000))
            print("gönderiliyor.")
            time.sleep(0.5)
            print("gönderiliyor..")
            time.sleep(0.5)
            print("gönderiliyor...")
            time.sleep(0.5)
            print("gönderiliyor.")
            time.sleep(0.5)
            print("gönderiliyor..")
            print("gönderildi. kalan bakiye {} tl".format(bakiye))
        elif isl=="5":
            break      

elif hesano == hesNo and passw != passwo:
    print("şifre hatalı")
    
    
    
    
        
    

