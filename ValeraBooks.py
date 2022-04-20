# def custom_sum5000(ind, arr):
#     if len(arr) < (ind + 1 + 5000):
#         su = sum(arr[ind:len(arr) - 1]) + sum(arr[:(5000 - (len(arr) - 1 - ind))])
#     else:
#         su = sum(arr[ind:ind + 5000])
#     return su


# def walkthrough5000(pos, minsL, ft2, totalbook2):
#     for el in range(pos, pos + 5000):
#         if ft2 < minsL[el]:
#             break
#         else:
#             ft2 -= minsL[el]
#             totalbook2 += 1
#     return totalbook2


# def maxbooks5000(bks, ft, minsL):
#     if sum(minsL) < ft:
#         return bks
#     totalbook = 0
#     for pos in range(len(minsL)-1):
#         ft2 = ft
#         totalbook2 = 0
#         for el in range(-pos, -pos + len(minsL), 5000):
#             if ft2 < custom_sum5000(el, minsL):
#                 totalbook2 = walkthrough5000(el, minsL, ft2, totalbook2)
#                 break
#             else:
#                 ft2 -= custom_sum5000(el, minsL)
#                 totalbook2 += 5000
        
#         if totalbook2 > totalbook:
#             totalbook = totalbook2 
        
#     return totalbook

# # core algorithm
# def maxbooks(bks, ft, minsL):
#     if sum(minsL) < ft:
#         return bks
#     totalbook = 0
#     for pos in range(len(minsL)-1):
#         ft2 = ft
#         totalbook2 = 0
#         for el in range(-pos, -pos + len(minsL)): # because Valera read books in sequence, so we have to keep el negative
#             if ft2 < minsL[el]:
#                 break
#             else:
#                 ft2 -= minsL[el]
#                 totalbook2 +=1
#         if totalbook2 > totalbook:
#             totalbook = totalbook2        
#     return totalbook


# if __name__ == '__main__':
#     numofb, freetime = map(int, input().split())
#     numofmins = list(map(int, input().split()))
#     if numofb > 10000:
#         print(maxbooks5000(numofb, freetime, numofmins))
#     else:
#         print(maxbooks(numofb, freetime, numofmins))




# if __name__ == '__main__':

n, t = map(int, input().split())
a = list(map(int, input().split()))
 
j = 0
read_books = max_books = 0
 
for i in range(n):
    while t < a[i]:
        t += a[j]
        j += 1
        read_books -= 1
 
    t -= a[i] 
    read_books += 1
    max_books = max(max_books, read_books) 
 
print(max_books)

# DONE
    
  