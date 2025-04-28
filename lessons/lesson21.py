#try - except
# try:
#     a=int(input("a: "))
#     b=2025-a
#     print(f"Siz {b} jastasiz")
# except:
#     print(f" Iltimas san kiriting")


sanlar=[1,2,3,4,5,6,7,8,9]
i=int(input("a: "))
try:
    i=int(i)
    print(sanlar[i-1])
except IndexError:
    print("Onday element joq")
except ValueError:
    print("Putin san kiritin'")