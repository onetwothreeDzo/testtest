Na, Nb = map(int, input().split())
K, M = map(int, input().split())
ListA = list(map(int, input().split()))
ListB = list(map(int, input().split()))

if ListA[ K - 1 ] < ListB[len(Nb) - M - 1]:
    print("YES")
else:
    print("NO")

# this is a new line 
# but have no new attention
