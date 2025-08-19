#Collections: Counter, namedtuple, OrderedDict, defaultdict, deque

#counter: a container that stores the elements as dictionary keys and their counts as dictionary values
from collections import Counter
a = 'aaaaabbbbccc'
my_counter = Counter(a)
print(my_counter) #characters as keys and their count as values, ex. Counter({'a': 5, 'b': 4, 'c': 3})
print(my_counter.items()) #all key value pairs
print(my_counter.keys())  #gives all keys
print(my_counter.most_common(1)) #gives the most common of the given items, will return list of tuple, ex. [('a', 5)]
print(my_counter.most_common(1)[0][0]) #gives most common element
print(list(my_counter.elements())) #gives each element as a list ex. ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c']

#namedtuple: easy to create and lightweight object type
from collections import namedtuple
Point = namedtuple('Point', 'x,y')



