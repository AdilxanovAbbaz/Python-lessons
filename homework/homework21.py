#1
# balance = 5000

# try:
#     withdrawal_amount = float(input("Qansha pul shishejaqsan? "))
    
#     if withdrawal_amount > balance:
#         print("Akshan' jok tupoi")
#     else:
#         balance -= withdrawal_amount
#         print(f"Aksha sheshildi. Taza balans: {balance} so'm")
        
# except ValueError:
#     print("San kirit mal")



#2
# products = ["kitob", "qalam", "daftar"]

# product_choice = input("tanla, qayssi? (kitob, qalam, daftar): ")

# if product_choice in products:
#     print(f"Boldi qabbulandi: {product_choice}")
# else:
#     print("Onday producti joqqo Eshak bas")



#3
# seats = 20

# try:
#     tickets = int(input("Neshe bilet alajaqsan?: "))
    
#     if tickets > seats:
#         print("dim kop alip jberdin' jora")
#     else:
#         seats -= tickets
#         print(f"boldi boldi qabbulandi, bos qalg'an orinlar : {seats}")
        
# except ValueError:
#     print("San kiritse")



#4
# try:
#     temperature = float(input("temoeratura neshe eken jazib jber: "))
    
#     if temperature < -50 or temperature > 60:
#         print("Qate temperatura kirintin' joraa!")
#     else:
#         print(f"Bugingi temperatura : {temperature}°C")
        
# except ValueError:
#     print("San kirit!!!")


#5
password = input("Parol kirit: ")

if len(password) < 6:
    print("Dim qisqa bolip kettigo !")
else:
    print("Boldi duris duris")
