import os

DIR = '/home/ivan/PycharmProjects/python-itvdn-15.10.2020/starter'


# lst = os.listdir(DIR)
# for f in lst:
#     f = os.path.join(DIR, f)
#     print(f)
#     if os.path.isdir(f):
#         sub = os.listdir(f)
#         for t in sub:
#             t = os.path.join(f, t)
#             print(t)


# рекурсия
def walk(p):
    lst = os.listdir(p)
    for f in lst:
        f = os.path.join(p, f)
        print(f, flush=True)
        if os.path.isdir(f):
            walk(f)


walk(DIR)
