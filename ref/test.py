'''
# teacher
n=int(input("Please enter an integer number: "))
int_sum = 0
if (n>=0):
  for i in range(1, n+1):   #loop
    int_sum += i
  print("Summation = ", int_sum)
else:
  print("No computation for a negative integer!")

# me
print(f"Summation = {sum(range(1, n:=int(input('Please enter an integer number: '))+1))}" if n>=0 else "No computation for a negative integer!")
'''

'''
fac = lambda x: 1 if x == 0 else x * fac(x - 1)
print(fac(5))

sum_odds = lambda n: sum(x for x in range(1, n+1) if x % 2 != 0)
print(sum_odds(10))

sum_evens = lambda n: sum(x for x in range(1, n+1) if x % 2 == 0)
print(sum_evens(10))
'''

for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i * j}", end="\t")
    print()