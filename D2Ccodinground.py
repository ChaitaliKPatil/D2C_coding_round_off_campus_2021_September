#D2C coding round Problem 1

oper=[]
N=int(input('How many coins do you withdraw from ATM? '))
nn=int(N)
#print(N,type(N))

def nine(N):
    for n in range(15):
        if (9**n)<=N and (9**(n+1))>N:
            return 9**n
            '''global A
            A=N-9**n
            #print(A)
            return A'''
        '''else:
            return 0'''
def six(A):
    #print(A,type(A))
    for m in range(20):
        if (6**m)<=A and (6**(m+1))>A:
            return 6**m
nnn=nn
if nn<=100000:
    try:
        while nn<=100000:
            x,y=nine(nn),six(nn)
            #print(x,type(x))
            #print(y,type(y))
            maxxy=max(x,y)
            oper.append(maxxy)
            nn=nn-maxxy
    except:
        print("")
    finally:
        rem=nnn-sum(oper)
        #print(rem)
        #oper.append(rem)
        print('Take out coins in this manner: ',oper)
        nopr=len(oper)+rem
        print('No. of operations you will need to perform to take out %d coins from ATM is: '%nnn,nopr)
elif nn>100000:
    print("Sorry, because of Technical error in ATM machine, you will be able to withdraw cash below 100000 in a day!!")


#D2C coding round problem 2
ls=[]
print('You will have to enter a list in order to join elemnts in it one by one and then reverse it after appending')
ip=int(input("How many elements do you want in a list? "))
for iip in range(1,ip+1):
    ls.append(int(input('enter %dth element'%iip)))
#print(dir(ls))
ls1=[]
for i in range(len(ls)):
    ls1.append(ls[i])
    ls1.reverse()
print(ls,ls1,sep='\n')



#D2C coding round problem 3
B=[]
N=int(input('\n\n\n\n\n No. of elements in array B: '))
for x in range(1,N+1):
    y=int(input('Give %dth element:'%x))
    B.append(y)
print(B)
A=list(range(len(B)))
for i in range(len(B)):
    A[i]=(i+1)*B[i]-(i)*B[i-1]
print(A,'\n\n\n\n\n')