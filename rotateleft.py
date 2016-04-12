def rotateleft():
    userarray = list (input("enter three integers \n")
    leftrotated = userarray
    leftrotated += [leftrotated.pop(0)]
    print(leftrotated)
rotateleft()