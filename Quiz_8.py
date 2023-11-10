import random
def lotto (a):
    list=[]
    for i in range(a+1):
        number=random.randint(1,45)
        if number not in list:
            list.append(number)
    list.sort()
    print('생성된 로또 번호는' +str(list)+'입니다.')
lotto(6)
