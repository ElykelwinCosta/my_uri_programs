j = 7
for i in range(1, 10):
    if(i % 2 == 1):
        for k in range(3):
            print("I={} J={}".format(i, j))
            j -= 1
        j += 5
