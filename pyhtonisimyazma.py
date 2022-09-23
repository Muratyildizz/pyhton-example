import time
while True:
    n=11
    print()
    for i in range(n):
        for j in  range(n):
            if (j==1 and i>1)or(i-j==1 and j>1 and j<5)or(i+j==9 and j>3 and j<8)or(j==7 and i>1):
                print(" X ", end='')
            else:
                print("   ", end='')
        print("", end='\n')
    print()
    time.sleep(0.5)
    n=9
    print()
    for i in range(n):
        for j in  range(n):
            if (j==1 and i<8)or(i==8 and j>1 and j<7)or(j==7 and i<8):
                print(" X ", end='')
            else:
                print("   ", end='')
        print("", end='\n')
    print()
    time.sleep(0.5)
    n=9
    print()
    for i in range(n):
        for j in  range(n):
            if(j==1)or(i==0 and j>1 and j<6)or(j==5 and i<5)or(i==4 and j>1 and j<6)or(i-j==3 and i<9 and j>0):
                print(" X ", end='')
            else:
                print("    ", end='')
        print("", end='\n')
    time.sleep(0.5)
    n=10
    print()
    for i in range(n):
        for j in  range(n):
            if (j==1 and i>2)or(j==7 and i>2)or(i+j==4 and j<3 and j>1) or(i==1 and j>2 and j<6)or(i==2 and j==6)or(i==5 and j>1 and j<8):
                print(" X ", end='')
            else:
                print("   ", end='')
        print("", end='\n')
    print()
    time.sleep(0.5)
    n=9
    print()
    for i in range(n):
        for j in  range(n):
            if (i==0 and j<8 and j>0)or(j==4):
                print(" X ", end='')
            else:
                print("   ", end='')
        print("", end='\n')
    print()
    time.sleep(0.5)
