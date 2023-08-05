def devolver_distintos(num1,num2,num3):
    sum = num1+num2+num3
    list = [num1,num2,num3]
    list.sort()
    if sum >15:
        return list[len(list)-1]
    elif sum <10 :
        return  list[0]
    else:
        return list[1]

print(devolver_distintos(1,9,0))
