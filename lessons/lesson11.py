
#1

# a=int(input("a: "))
# b=int(input("b: "))
# c=int(input("c: "))
# if a % b == 0 :
#     print("a soni b ga bo'linad")
# elif a % c == 0:
#     print("a soni c ga bo'linad")
# else:
#     print("a soni b ga bo'linmayd")

#2

# n=int(input("n: "))
# if n % 2 == 0:
#     list_n=(list(range(0,n,2)))
#     print(list_n)   
#     print(sum(list_n))
# else:
#     print("Iltimas jup san kiritin'")


#3
# n=int(input("n: "))
# new_list=[]
# for i in range(1, n+1):
#     a=int(input("a: "))
#     new_list.append(a)
# b=(min(new_list))
# c=(max(new_list))
# print(f"Farq {c-b}")


#4
# lugat={"apple": "olma", "banana": "banan", "cat": "mushuk"}
# a=input("a: ")
# if a in lugat:
#     value=lugat.get(a)
#     print(value)
# else:
#     print("Bunday zat joq")


#5
# baholar = {"Ali": 85, "Bobur": 74, "Diyor": 90, "Madina": 78}
# for key, value in baholar.items():
#     if value > 80:
#         print(f"{key} - {value}\n")

#6
# n=int(input("n: "))
# new_list=[]
# for i in range(1, n+1):
#     a=int(input("a: "))
#     new_list.append(a)
# new_list.sort(reverse=True)
# print(new_list)



#1
class_1={"Class":["1a", "1b","1v"],
         "til":["uzbek","Rus","Qaraqalpaq"],
         "student":"300",
         "qizlar":"130",
         "ballar":"170",
         "sabaq":"8:00-11:40",
         "sabaqlar":"10 pan"}


class_2={"Class":["2a", "2b","2v"],
         "til":["uzbek","Rus","Qaraqalpaq"],
         "student":"345",
         "qizlar":"175",
         "ballar":"170",
         "sabaq":"8:00-12:20",
         "sabaqlar":"12 pan"}


class_3={"Class":["3a", "3b","3v"],
         "til":["uzbek","Rus","Qaraqalpaq"],
         "student":"412",
         "qizlar":"206",
         "ballar":"206",
         "sabaq":"13:00-16:40",
         "sabaqlar":"14 pan"}

class_4={"Class":["4a", "4b","4v"],
         "til":["uzbek","Rus","Qaraqalpaq"],
         "student":"503",
         "qizlar":"203",
         "ballar":"300",
         "sabaq":"13:00-17:10",
         "sabaqlar":"16 pan"}

mektep=[class_1,class_2,class_3,class_4]
print(mektep[3]["Class"][2])
