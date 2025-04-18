
# 📌lesson13
# items( )metodi

# telefonlar={'Amir':'iphone x',
#             'Artur':'samsung A02',
#             'Sevara': 'nokia 3310'}
# name = input('kimnin telefon markasin bilejaqsiz: ')
# phone=telefonlar.get(name.title(), 'Ol telefon uslamaydi')
# print(phone)
# # phone=telefonlar.get(name.title(), 'Ol telefon uslamaydi')
# # print(phone)
# phone=telefonlar.get('Sultan')
# print(phone)

# name=input('kimnin telefon markasin bilejaqsiz: ')
# phone= telefonlar.get(name.title(), "joq")
# if phone== "joq":
#     print("bizlerde bunday adam joq")
# else:
#     print(f" {name.title()} {phone} telefonin uslaydi eken ")




# python={'int': 'san',
#     'float': 'bolshek san',
#     'str':'text',
#     'if':'eger',
#     'else':'bolmasa',
#     'and': 'ham',
#     'or': 'yaki',
#     'sort': 'sortirovka',
#     }
#
# n=input("Gilt sozdi kiritin' : ")
# N=python.get(n, " Onday gilt soz joq")
# print(N)

# if n in python:
#         print(python[n])
# else:
#     print(f"onday gilt soz joq")



# zatlar={'alma': 1000,
#         'erik': 2000,
#         'juzim': 3000,
#         'apelsin': 5000
#         }
# print('Magazindegi miyweler:')
# for zat in zatlar.keys():
#     print(zat)



# student={'ati': ['Maqsetbaev',  'Timur'],
#          'jasi': 20,
#          't_jil': 2003}
# for key, value in student.items():
#     print(f" gilt: {key}")
#     print(f" tusindirme: {value} \n")



# zatlar={'alma': 1000,
#         'erik': 2000,
#         'juzim': 3000,
#         'apelsin': 5000
# }
# bazarliq=['alma', 'nan', 'juzim', 'erik']
# for zat in bazarliq:
#     if zat in zatlar.keys():
#         print(f"{zat.title()} - {zatlar[zat]} swm")
#     else:
#         print(f"{zat} joq eken")



# telefonlar={'Amir':'iphone x',
#             'Artur':'samsung A02',
#             'Sevara': 'nokia 3310'}
# print(" Paydalaniwshilar to'mendegi telefonlardi uslaydi: ")
# for tel in telefonlar.values():
#     print(tel)



# telefonlar={'Amir':'iphone x',
#             'Artur':'samsung A02',
#             'Sevara': 'nokia 3310 ',
#             'Alim':'iphone x',
#             'roza':'samsung A02',
#             'Sayora': 'nokia 3310'}
# print("Paydalaniwshilar tomendegi telefonlardi uslaydi: ")
# for tel in set( telefonlar.values()):
#       print(tel)


# fakultet_0={'ati': "matfak",
#             'student': 1300,
#             'qizlar': 600,
#             'balalar': 700,
#             'waqit': "4 jil",
#             'korpus': "glav"}

# fakultet_1={'ati': "yurfak",
#             'student': 1650,
#             'qizlar': 650,
#             'balalar': 1000,
#             'waqit': "4 jil",
#             'korpus': " -korpus"}

# fakultet_2={'ati': "economfak",
#             'student': 1160,
#             'qizlar': 610,
#             'balalar': 550,
#             'waqit': "4 jil",
#             'korpus': " -korpus "}


# QMU=[fakultet_0, fakultet_1, fakultet_2]
# print(QMU[0])
# print(QMU[0]['student'])
