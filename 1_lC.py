# def sum(L,A):
#     l=[i**A for i in L]
#     return l
# L=[1,2,3,4,5,6]
# print(sum(L,2))
# print(sum(L,3))


# makers = ["Honda", "Toyota", "Ford", "Nissan", "Dodge"]
# cars = ["Honda civic", "Honda accord", "Toyota supra", "Toyota camry", "Ford Mustang", "Nissan skylineGTR", "Dodge Hellcat", "Dodge challenger"]
# l1=[]
#
# for i in makers:
#     l=[]
#     for j in cars:
#         if i in j:
#             l.append(j)
#     l1.append(l)
# d={i:j for i,j in zip(makers,l1)}
# print(d)
# print(l)

makers = ["Honda", "Toyota", "Ford", "Nissan", "Dodge"]
cars = ["Honda civic", "Honda accord", "Toyota supra", "Toyota camry", "Ford Mustang", "Nissan skylineGTR", "Dodge Hellcat", "Dodge challenger"]
L=[]
for i in makers:
    for j in cars:
        if i in j:
            L.append(j.replace(i+" ",""))
print(L)



