from collections import Counter
a = 13
b = 3
x = a
y = b

remmap = {}
while b > 1:
    q, r = divmod(a, b)
    remmap[r] = (a, b, q) # r = a - b*q
    a, b = b, a%b

counts = Counter()
counts[1] = 1


while len(counts) > 2 or x not in counts or y not in counts:
    for i, n in counts.items():
        if i in remmap:
            a, b, r = remmap[i]
            counts[a] += n
            counts[b] -= n*r
            del counts[i]
            break
            
print(counts)
print(divmod(8146798528947, 17))