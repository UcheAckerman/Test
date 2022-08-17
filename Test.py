##List
##x = [4, True, 'hi']
##
##x.append(4)
##print(x)
##x.extend([4,5,5,5,6])
##print(len(x))
##print(x)
##x.pop()
##print(x[2])
##
##
##y = (0,0,2,3)
##print(y)
##-------------------------------------------------------------------------------

##Tuple They are immutable
##x = (1,2,4,6,7,8)
##-------------------------------------------------------------------------------


####for loop
##for i in range(10):
##    print(i)
##
##x = [1,2,3,4,5]
##print('-' * 100)
##for i in enumerate(x):
##    
##    print(i)
##
##for i in range(len(x)):
##    print(i)
##--------------------------------------------------------------------------------

####Sliced [start:stop:step] Used to reverse a list [::-1]
##x = [0,1,2,3,4,5,6,7,8]
##y = ['hi', 'hello', 'goodbye', 'cya', 'sure']
##s = 'hello'
##
##sliced = s[::-1]
##
##print(sliced)

####Set
##x = set()
##s = {1,2,3,4,4,5}
##s3 = {4,5,3,2,6,3}
##
##print(s.difference(s3))
##print(s.union(s3))
##print(s.intersection(s3))
##
##s.add(6)
##print(s)

##Dictionary Key & Value
##x = {'key': 4}

##To add
##x[2] = [1,2,3]
##print(x)
##print(list(x.values()))
##print(list(x.keys()))
##
##
##for key, value in x.items():
##    print(key, value)
##
##for key in x:
##    print(key, x[key])

####Comprehension
##x = [x * 5 for x in range(5)]
##x = [i for i in range(100) if i % 3 == 0]
##x = {i:0 for i in range(100) if i % 3 == 0}
##x = {i for i in range(100) if i % 3 == 0}
##x = tuple(i for i in range(100) if i % 3 == 0)
##
##print(x)

##function
def func(x,y):
    print('Run', x, y)
    return x * y, x/y

r1, r2 = func(5,6)
print(r1,r2)

