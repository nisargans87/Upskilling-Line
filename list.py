#list basics
list1=[1,1,2,3,4,5,8,6,7,8,1]
print(type(list1))
print(type(list1[2]))
print(id(list1))
print(id(list[2]))
print(dir(list1))
mod_list=list1
for method in dir(mod_list):
    if not method.startswith("__"):
        print(method)
#list methods
print(len(list1))
print(list1.append(9))
#print(help(list1.append))
print(list1.copy())
#print(help(list1.copy))
print(list1.sort())
print(list1.reverse())
print(list1.remove(1))
print(list1.pop(8))
print(list1.insert(12,22))
print(list1.index(8))
print(list1.extend([9,10]))
print(list1.count(1))
print(list1.clear())
print(list1)

#Lists Operations by operators
list2=["Nisarga",87,"BCA","$12000",True]
list3=["Yes"]
print(list2+list3)
print(list2*1)
print(list2==list3)
print(list2!=list3)
print(list2>list3)
print(list2<list3)
print(list2<=list3)
print(list2>=list3)
print("nisarga" in list2)
print("Yes" in list3)
print("Placed" not in list3)
list3[0]="placed"
print(list3)
del list3[0]

# mathematical methods and set operations
list5=[2,3,4,5,6]
list6=[2,7,8,9,3]
print(sum(list5))
print(min(list6))
print(max(list5))
print(sorted(list5))
print(reversed(list5))
print(list5)
print(sum(list5)/len(list5))
print(set(list5) & set(list6))
print(set(list5) | set(list6))
print(set(list5) - set(list6))
print(zip(list5,list6))
print(list5)
print(list6)

#list fundamentals - creating,indexing,positive,negative,slicing,step slicing,reverse list,nested list, updating, adding,removing,comparision, membership operators
listf=[2,3,4,0,5]
listf2=["n",23.789,10,True]
empty=[]
print(listf[2])
print(listf[-2])
print(listf[1:3])
print(listf[::2])
print(listf[::-2])
nested=[
        ["N",0],
        [8,False]
        ]
print(nested[0][1])
listf[3]=100
listf.append(101)
listf.extend([2,3,4])
listf.insert(1,99)
listf.remove(99)
listf.pop(0)
del listf[3]
print(listf==listf2)
listf.clear()
print(2 not in listf)

# Copying lists - direct assigment, shallow copy, slice copy
z=[1,2,3,4]
assign=z
print(z.copy())
f=z[1:]
print(f)

#Traversing a list, Iterating a list
# for loop
iterable=[2,4,6,8,10]
iterable1=[2,3,4,5,6]
for num in iterable:
    print(num)
total=0
for num in iterable:
    total+=num
print(total)
# while loop
i=0
while i<4:
    print(i)
    i+=1
# enumerate
for index, value in enumerate(iterable):
    print(index,value)
#zip
for num,number in zip(iterable,iterable1):
    print(num,number)
# Nested loops
#unpacking
arr=[2,3,4]
x,x1,y2 = arr
print(x)
print(x1)
print(y2)

#Numpy library - Scientific Computing, conversion of a list datatype into numpy array
import numpy as np
#print(dir(np))
a=np.array([1,2,3,4])
b=np.array([5,6,1,2])
# numpy basics
print(type(a))
print(list(a))
print(type(a))
#print(dir(b))
# numpy methods
print(np.add(a,b))
print(a+b)
print(np.subtract(a,b))
print(a-b)
print(np.multiply(a,b))
print(a*b)
print(np.divide(a,b))
print(a/b)
print(np.floor(a,b))
print(a//b)
print(a%b)
print(np.exp(a))
print(a**b)
print(np.sqrt(a))
print(np.square(a))
print(np.log(a))
print(np.std(a))
print(np.add(a,b))
print(np.max(a))
print(np.argmin(a))
print(np.argmax(b))
print(np.var(b))
print(np.mean(b))
#cumulative operations
print(np.cumsum(b))
print(np.cumprod(b))
print(np.argsort(b))
print(np.sort(b))
print(np.nonzero(b))
print(np.median(b))
print(np.percentile(b,50))
print(np.quantile(b,0))
print(np.transpose(b))
print(np.ndim(a))
print(np.size(b))
print(np.shape(b))
# bitwise operations
print(np.bitwise_and(a,b))
print(np.bitwise_or(a,b))
print(np.bitwise_not(a,b))
print(np.invert(a,b))
print(np.cbrt(b))
print(np.log10(b))
#trigonometric functions
print(np.sin(b))
print(np.radians(b))
print(np.degrees(b))
print(np.arcsin(b))
print(np.tan(b))
# comparision functions
print(np.less_equal(b,a))
print(np.less(b,a))
print(np.equal(a,b))
#Logical functions
print(np.logical_and(a,b))
print(np.logical_not(a,b))
print(np.all(b))
print(np.any(b))
#rounding functions
print(np.trunc(b))
print(np.floor(b))
print(np.ceil(b))
print(np.round(b))
#Array joining functions
print(np.vstack(b))
print(np.hstack(b))
#linear algebra functions
print(np.dot(a,b))
print(np.inner(a,b))
print(np.outer(a,b))
print(np.any(b))
print(np.concatenate((a,b)))




















