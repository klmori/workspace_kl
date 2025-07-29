def pelindrome(digit):
    result = ''
    num = digit
    while num >0:
        res = num % 10   # return  reminder
        num = num // 10  # return result floor
        result = result+str(res)
    
    if digit == int(result):
        print('Pelindrome')

def armstrong(num):
    dig = num
    nod = len(str(num))
    total = 0

    while dig:
        res = dig % 10
        dig = dig // 10
        total += res ** nod

    if total == num:
        print("Armstrong number")



def all_factors(dig):

    # div_list = []
    # i = 1
    # while dig > i:
    #     if dig % i == 0:
    #         div_list.append(i)
    #     i += 1
    # print(div_list)

    from math import sqrt

    div_list = []
    res = []
    
    for i in range(1, int(sqrt(dig))):
        if dig % i == 0:
            div_list.append(i)
            div_list.append(int(dig / i))
    print(div_list)


def frequency(arr):
    res = {}

    # for i in arr:
    #     ct = 0
    #     for j in arr:
    #         if i == j and i not in res:
    #             ct += 1
    #     res[i]=ct
    # print(res)

    # for i in arr:
    #     if i not in res:
    #         res[i] = 1
    #     else:
    #         res[i] += 1

    for i in arr:
        res[i] = res.get(i,0) + 1 
    
    print(res)


# frequency([1,3,5,2,1,3,4])



def countNumList(listarry, num):
    pass
