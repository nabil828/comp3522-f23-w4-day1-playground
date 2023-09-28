# # args to a function
# def my_print(*args):
#     print(args)
#     print(type(args))
#     for item in args:
#         print(item)


# my_print('dog', 5, {'name': 'Fido'}, [1, 2, 3], 7, 6, 6)

def f(a, b, c, d, e):
    print(a, b, c, d, e)
    print(a, b, c, d, e)


# unpacking args
list = [1, 2, 3, 4, 5]

a, b, c, d, e = *list
print(c) # 3  
