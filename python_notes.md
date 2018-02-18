

## Python

###complexity

sorted(): O(nlogn)

list search complexity: O(n)

dictionary: O(1)


### Code syntax

List

```
l_without_num = l[:k] + l[(k + 1):]
```


Dictionary

```
dict[key] = val
key in dict
```

None value

```
a = None
a is not None # FALSE
if (a)  # FALSE

b = 0
b is not None # TRUE
if (b) # FALSE

```

Multiple dimensions

```
[[False for i in range(2)] for j in range(3)]
# [[False, False], [False, False], [False, False]]
```

Iterator

```
['(' + str(x) + ')' + str(y) for x in [1,2] for y in [4,5]]
# ['(1)4', '(1)5', '(2)4', '(2)5']
```

References

```
a = [1,2,3]
b = a
a[1] = 4
b
[1,4,3]

a = 1
b = a
a = 4
b
1

a = 1
la = [1,2,3,a]
la
[1,2,3,1]
a = 2
la
[1,2,3,1]
```


Or gate

```
a = None
b = 5
a or b
# 5
```

