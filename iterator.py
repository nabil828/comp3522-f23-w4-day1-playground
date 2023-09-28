my_tuple = (1, 2, 3, 4, 5)
my_it = iter(my_tuple)
# try:
#   print(next(my_it))
#   print(next(my_it))
#   print(next(my_it))
#   print(next(my_it))
#   print(next(my_it))
#   print(next(my_it))
# except StopIteration:
#   print("1111")

for item in my_it:
    print(item)
