#1
import random
print("1-10 shekem san tanlan'")
ulkeni=10
kishisi=1
gotovka=input("Tayinsizba? awa(1)/yaq(2): ")
if gotovka == "1":
    while True:
        n=random.randint(kishisi,ulkeni)
        print(f"tanlagan sanin': {n}")

        answer=input("Durispa? awa(1)/yaq(2): ")
        if answer == "1":
            print("Tawdimgo endi")
            break
        elif answer == "2":
            a= input("Senin' chislon' tomenbe ili koppa? kishi(1)/ulken(2): ")
            if a == "1":
                ulkeni = n - 1 
            elif a == "2":
                kishisi = n + 1
            else:
                print("ulken ili kishi deb jazin'")
else:
    print("ok! keyingi ret koriskenshe")
        
    

    
