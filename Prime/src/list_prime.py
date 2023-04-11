def list_prime(number):
    list = []
    for i in range(2,number+1):
        if i == 2:
            list.append(i)
        elif i % 2 == 0:
            continue
        else:
            list.append(i)
            for j in range(3,int(i**0.5)+1,2):
                if i % j ==0:
                    list.pop()
                    break
    return list


