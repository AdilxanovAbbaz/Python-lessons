#while 

#1
# i=0
# while i <=10:
#     print(i)
#     i += 1


#2
# a="abbaz8889"
# while True:
#     b=input("a: ")
#     if a == b:
#         print("Parol durus")
#         break
#     else:
#         print("Parol qate")


#3

# print("Kiasdnak;jdbsk;dnjs")
# soraw="Qalegeasdkasd"
# soraw+="adh'aksd'l/ajs'ld"
# while True:
#     juwap=input(soraw)
#     if juwap == 'exit':
#         break
#     else:
#         print(float(juwap)**2)
# print("Dastur tawsildi")



#4


#0-5 бесплатно
# 5-12 5к
# 12-18 7к
# 18-40 10к
#  <40 15к

print("Cirk kiriw Jaska qarap")
print("Bul funsiadan chigu ushin 'exit' dep jasin'0")
while True:
    a=input("a: ")
    if a == "exit":
        break
    else:
        a=int(a)

    if a <=5:
        print("Kiriw free")
    elif a <=12:
        print("Kiriw 5k")
    elif a <=18:
        print("Kiriw 10k")
    elif a <=40:
        print("Kiriw 15k")
    elif a > 40:
        print("Kiriw free")
    else:
        print("Iltimas jasin'izdi kiritin'")

        
        
