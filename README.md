# lru-cache-py
Implement a LRU cache in python with basic functionalities 

# LRU Cache

Design and implement methods of an LRU cache. The class has two methods get() and set() which are defined as follows.
get(key): returns the value of the key if the key exists in the cache; otherwise returns -1.
set(key, value): inserts the value if the key is not already present. If the cache reaches its capacity, it should invalidate the least recently used item before inserting the new item.

In the constructor of the class, the size of the cache should be initialized.

## Signatures
```
LRUCache(int capacity)
int get(int key)
int set(int key, int value)
```

## Input Constraints
```
1 <= capacity <= 1000
1 <= key, value <= 1000
```

## Output of Test Cases
The result of all get operations.


## Expected Complexity:
1.Expected Time Complexity: O(1) for both get() and set().
2.Expected Auxiliary Space: O(1) for both get() and set(), though, you may use extra space for cache storage and implementation purposes.


## Example 1:
```
capacity = 2
Queries:
SET 1 2 
GET 1

Output: 2
Explanation:
SET 1 2 -->  [(1,2)]
GET 1 : Print the value corresponding to key 1, which is 2.
```

## Example 2:

```
capacity = 2
Queries:
SET 1 2 
SET 2 3 
SET 1 5
SET 4 5 
SET 6 7 
GET 4 
SET 1 2 
GET 3

Output: 5 -1
Explanation: 
SET 1 2  --> [(1, 2)]
SET 2 3  --> [(1, 2), (2, 3)] -> the most recently used one is kept at the rightmost position
SET 1 5  --> [(2, 3), (1, 5)] -> cache size is 2, hence we delete the least recently used key-value pair
SET 4 5  --> [(1, 5), (4, 5)]
SET 6 7  --> [(4, 5), (6, 7)]
GET 4   --> Prints 5, the cache now looks like [(6, 7), (4, 5)]
SET 1 2  --> [(4, 5), (1, 2)] -> again, cache size is 2, so we delete least recently used key-value
GET 3    --> No key value pair with key = 3. Hence, -1 is printed.
```