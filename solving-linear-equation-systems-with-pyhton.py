import numpy as np

A = np.array([[ 1.0, 2.0, 3.0],[ 4.0, 5.0, 2.0],[ 2.0, 8.0, 5.0]]) #3x3 coefficient array
b = np.array([5.0,10.0,15.0])
c = np.array([1.0,1.0,1.0])





def myGE(A,b):

    if A.shape[0]!=A.shape[1]:
        print ("Matrix cannot solved because it's not in correct form ")
        return

    if np.linalg.det(A)==0:
        print ("Matrix is not linearly independent. Solving not possible")
        return

    stepcounter = 1
    lenght = len(A)
    print("\nFirst Step")
    print("\n",np.matrix(A),np.matrix(b).T,"\n")

    for g in range(lenght):
        for p in range(g,lenght):
            if abs(A[g][p]) > abs(A[g][g]):
                A[[g,p]] = A[[p,g]]
                b[[g,p]] = b[[p,g]]
                print("Pivoting done:R%d <---> R%d"%(g,p))
            else : pass


    print("\n",np.matrix(A),np.matrix(b),"\n")
    x=0
    y=0


    # if diagonal is not 0
    #it does  A[x][y]-= A[x][y]*c
    if x < A.shape[0]-1:
        glork =  A.shape[0]-1 -x
        for r in range(glork):
            if glork==0:
                pass
            print("Step : ", stepcounter)
            for ner in range(A.shape[0]-x-1):
                if A[x][y]!=0: #if Akj=0 gauss it
                    c = A[x+1+ner][y]/A[x][y] #to find if c of equation Akj += c*Aij
                    A[x+1+ner]=A[x+1+ner]-c*A[x]
                    b[x+1+ner]=b[x+1+ner]-c*b[x]
                    print("R%s = R%s - R%s*%s"%(x+2+ner,x+2+ner,x+1,c))

            print("\n",np.matrix(A),np.matrix(b),"\n")
            y=y+1
            stepcounter=stepcounter+1
            x=x+1

    else : pass



    print("“Back Substitution Started.”")
    x3=b[2]/A[2][2]
    x2=(b[1]-A[1][2]*x3)/A[1][1]
    x1=(b[0]-A[0][1]*x2-A[0][2]*x3)/A[0][0]
    print("x1:",x1,"\n")
    print("x2:",x2,"\n")
    print("x3:",x3,"\n")
    b[0]=x1
    b[1]=x2
    b[2]=x3


    print("--result vector x.--")
    print(np.matrix(b))



def main():
    myGE(A,b)



main()
