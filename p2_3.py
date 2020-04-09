from collections import deque
 
fruit_list = ['apple', 'banana', 'orange']
fruit = fruit_list.pop() 
print(fruit, fruit_list) 
 
fruit_deque = deque(['apple', 'banana', 'peach'])
fruit_deque.append('straberry')
fruit_deque.appendleft('blueberry')
 
pop_item = fruit_deque.pop()
print(pop_item)
 
pop_left_item = fruit_deque.popleft()
 
fruit_deque.extend(deque(('mango', 'lemon')))
 
fruit_deque.extendleft(deque(['coconut','durian']))
 
print(fruit_deque)

from collections import Counter
c = Counter()
for word in ['mango','apple', 'banana', 'apple','mango', 'banana', 'peach', 'mango']:
    c[word] += 1
print(c.most_common())

a = Counter(m=37, n=21)
b = Counter(m=24, n=26)
print(a+b)
print(a&b)
print(a|b)