#Write a recursive function that takes one parameter:
# n and adds numbers from 1 to n.

def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)


print(recur_sum(7))


