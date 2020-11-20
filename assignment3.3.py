#Implement List comprehensions to produce the following lists.
#Write List comprehensions to produce the following Lists
#['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
#['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
#['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
#[[2], [3], [4], [3], [4], [5], [4], [5], [6]] [[2, 3, 4, 5], [3, 4, 5, 6],
#[4, 5, 6, 7], [5, 6, 7, 8]]
#[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
#1:-['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
j="ACADGILD"
list1=[i for i in j]
print(list1)
#2:- ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
A="xyz"
list2=[i*k for i in A for k in range(1,5)]
print(list2)
#3:- ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
B="xyz"
list3=[p*i for i in range(1,5) for p in B]
print(list3)
#3:-[[2], [3], [4], [3], [4], [5], [4], [5], [6]] [[2, 3, 4, 5], [3, 4, 5, 6],[4, 5, 6, 7], [5, 6, 7, 8]]
j=[]
n=[2,3,4]
list4=[[p+q] for p in n for q in range(0,3)]
j.append(list4)
m=[3,4,5,6]
list5=[[r+s for r in m ]for s in range(0,4)]
j.append(list5)
print(j)
#4:- [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
h=[1,2,3]
list6=[(r,i) for i in range(1,4) for r in h]
print(list6)















