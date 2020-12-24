b=0
v=7
for b in range(v):
    c = 0
    for c in range(b):
        if c==0 or c==b-1 or b==v-1:
            print('*',end='')
        else:
            print(' ',end='')

    print()

