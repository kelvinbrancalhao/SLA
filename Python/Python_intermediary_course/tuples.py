import sys

my_list = [0, 1, 2, 3, "hello", True]
my_tuple = (0, 1, 2, 3, "hello", True)
print(sys.getsizeof(my_tuple), bytes)
print(sys.getsizeof(my_list), bytes)
