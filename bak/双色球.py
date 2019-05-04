def HelloWorld():
    import random
    from collections import Counter
    
    x=range(1000)
    print('--------------------------------------------------\n')
    while True:
        y=random.choice(x)
        # print(y)
        if y==0:
            break
        l = []
        kk = []
        i = [i for i in range(1, 34)]
        for j in range(6):
            for jj in range(1000):
                k=random.choice(i)
                kk.append(k)
            o=Counter(kk)
            p=o.most_common(1)
            l.append(p[0][0])
            try:
                i.remove(p[0][0])
            except:
                pass
        kk=[]
        l.sort()
        for jj in range(1000):
            k=random.choice(range(1,17))
            kk.append(k)
        o=Counter(kk)
        p=o.most_common(1)
        l.append(p[0][0])
        print('--->',end="  ")
        print(l)
        # print('\n')
        # count-=1
        y=random.choice(x)
        # print(x)
    print('--------------------------------------------------\n')
    input("完成!")


if __name__=="__main__":
    HelloWorld()
