def dos_cero(*args):
    count = 0
    for arg in args:
        if arg==0:
            count +=1
        else:
            count=0
        if count==2:
            return True
    return False

print(dos_cero(2,3,4,5,6,0,3,0,0,3))
