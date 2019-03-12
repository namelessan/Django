rd,rm,ry = [int(x) for x in input().split(' ')]
ed,em,ey = [int(x) for x in input().split(' ')]

if (rd,rm,ry) == (ed, em, ey):
    print(0)
elif (rm, ry) == (em, ey):
    print(15*(rd-ed))
elif ry == ey:
    if rm <= em:
        print(0)
    else:
        print(500*(rm-em))
elif ry > ey:
    print(10000)
else:
    print(0)
