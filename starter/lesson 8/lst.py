import sys

lst = []


# http://www.laurentluce.com/posts/python-list-implementation/
for i in range(100):
    lst.append(None)
    print(f'{len(lst)=} {sys.getsizeof(lst)=}')