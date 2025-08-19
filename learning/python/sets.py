#Sets: unordered, mutable, no duplicates
myset = {1,2,3,1,2} #output is {1,2,3}
myset1 = set([1,2,3,1,2])
myset2 = set('Hello') #good for seeing how many unique characters
print(myset)
print(myset1)
print(myset2)
print(type(myset))

#methods
myset.add(4)
myset.remove(1) #KeyError if not in set
myset.discard(1) #No error if not in set
myset1.clear() #clears set
myset.pop() #returns and removes first item in set

#iteration
for i in myset: #iterated over items in set
    print(i)

if 1 in myset: #check existence of item
    print('yes')
else:
    print('no')

#union and intersection and difference, dont modify original set, return a new set
odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

u = odds.union(evens) #combines elements from two sets without duplication
print(u)

i = odds.intersection(evens) #returns items in both sets
print(i) #returns set() because no intersection

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}
diff = setA.difference(setB) #returns items in first set that aren't also in the second set
diff1 = setA.symmetric_difference(setB) #returns set all elements from set A and set B but not the elements that are in both
print(diff)
print(diff1)

#modifies original set
setA.update(setB) #adds new elements while keeping its own elements no duplicates
print(setA)

setA.intersection_update(setB) #only keeps elements they both have in common
print(setA)

setA.difference_update(setB)
print(setA)

setA.symmetric_difference_update(setB) #prints everything except elements they have in both
print(setA)

setC = {1,2,3,4,5,6}
setD = {1,2,3}
setE = {8,9}
print(setC.issubset(setD)) #subset? T/F
print(setD.issubset(setC))

print(setC.isdisjoint(setD)) #no intersection? T/F
print(setC.issuperset(setE))

#copying two sets
setF = {1,2,3,4,5,6}
setG = setF #original set also changes
setG = setF.copy()
setG.add(7)
print(setF)
print(setG)

#frozen set: immutable
a = frozenset([1,2,3,4,5,6])
#a.add(2), this will give us an error after setting it up you can change it
#update methods don't work | but union, intersection, and diff work

