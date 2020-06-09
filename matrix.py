import numpy as np
from math import exp
'''
design = np.matrix('1 0.8 0.64 0.512; 1 1 1 1; 1 1.2 1.44 1.728; 1 1.4 1.96 2.744; 1 1.6 2.56 4.096')

targets = np.matrix('24; 20; 10; 13; 12')

designT = design.transpose()

print(design)

print("TRANSPOSED IS: ")

print(designT)

A = np.dot(designT, design)

Ainv = np.linalg.inv(A)


print("\nTHIS IS A: ")
print(A)

print("\nTHIS IS A^-1: ")
print(Ainv)


print("THIS IS targets: ")
print(targets)


res = np.dot( np.linalg.inv(A + 2* np.identity(4)) , designT)

res = np.dot(res , targets)


print("THIS IS W:")
print(res)


'''


#mew = np.matrix([[10],[15]])
#mew = np.matrix([[93.3333],[156.6667]])
mew1 = np.matrix([[0],[4]])
mew2 = np.matrix([[4],[0]])
#E = np.matrix([[133.3333,0],[0,33.3333]])
#E = np.matrix([[4433.3333,216.6667],[216.6667,33.3333]])
E1 = np.identity(2)
E2 = np.identity(2)


E1inv = np.linalg.inv(E1)
E2inv = np.linalg.inv(E2)
print("INVERSO: ")
print(E1inv)
x1 = np.matrix([[2],[4]])
x2 = np.matrix([[4],[2]])
x3 = np.matrix([[0],[0]])
pCentro1 = 0.7
pCentro2 = 0.3
D = 2
pi = np.pi


E1det = np.linalg.det(E1)
E2det = np.linalg.det(E2)
print("DET: ")
print(E1det)

#print(x-mew)

a = x3-mew2
b = np.matmul(a.transpose(), E2inv)
c = np.matmul(b,a) 

calc = (-1/2) * c


res = (1/(2*pi)**(D/2)) * (1/(E2det)**(1/2)) * exp(calc)
# print(res)
# print(res*pCentro2)

#print("\nO Q NOS QUEREMOS")
#print(res * pCentro2)
#print("O Q NOS QUEREMOS\n")

pc1x1 = 0.9999
pc1x2 = 0.00078       
pc1x3 = 0.7

pc2x1 = 0.00014
pc2x2 = 0.99912     
pc2x3 = 0.3


mewC1 = (pc1x1 * x1 + pc1x2 * x2 + pc1x3 * x3)/ (pc1x1 + pc1x2 + pc1x3)
mewC2 = (pc2x1 * x1 + pc2x2 * x2 + pc2x3 * x3)/ (pc2x1 + pc2x2 + pc2x3)

print("mew centro 1:")
print(mewC1)
print("mew centro 2:")
print(mewC2)

E11c1 = (pc1x1 * (x1.item(0)-mewC1.item(0)) * (x1.item(0)-mewC1.item(0)) + pc1x2 * (x2.item(0)-mewC1.item(0)) * (x2.item(0)-mewC1.item(0)) + pc1x3 * (x3.item(0)-mewC1.item(0)) * (x3.item(0)-mewC1.item(0)))/ (pc1x1 + pc1x2 + pc1x3)
E22c1 = (pc1x1 * (x1.item(1)-mewC1.item(1)) * (x1.item(1)-mewC1.item(1)) + pc1x2 * (x2.item(1)-mewC1.item(1)) * (x2.item(1)-mewC1.item(1)) + pc1x3 * (x3.item(1)-mewC1.item(1)) * (x3.item(1)-mewC1.item(1)))/ (pc1x1 + pc1x2 + pc1x3)
E12c1 = (pc1x1 * (x1.item(0)-mewC1.item(0)) * (x1.item(1)-mewC1.item(1)) + pc1x2 * (x2.item(0)-mewC1.item(0)) * (x2.item(1)-mewC1.item(1)) + pc1x3 * (x3.item(0)-mewC1.item(0)) * (x3.item(1)-mewC1.item(1)))/ (pc1x1 + pc1x2 + pc1x3)
E21c1 = E12c1

EcovarianceC1 = np.matrix([[E11c1 , E12c1],[E21c1 , E22c1]])


E11c2 = (pc2x1 * (x1.item(0)-mewC2.item(0)) * (x1.item(0)-mewC2.item(0)) + pc2x2 * (x2.item(0)-mewC2.item(0)) * (x2.item(0)-mewC2.item(0)) + pc2x3 * (x3.item(0)-mewC2.item(0)) * (x3.item(0)-mewC2.item(0)))/ (pc2x1 + pc2x2 + pc2x3)
E22c2 = (pc2x1 * (x1.item(1)-mewC2.item(1)) * (x1.item(1)-mewC2.item(1)) + pc2x2 * (x2.item(1)-mewC2.item(1)) * (x2.item(1)-mewC2.item(1)) + pc2x3 * (x3.item(1)-mewC2.item(1)) * (x3.item(1)-mewC2.item(1)))/ (pc2x1 + pc2x2 + pc2x3)
E12c2 = (pc2x1 * (x1.item(0)-mewC2.item(0)) * (x1.item(1)-mewC2.item(1)) + pc2x2 * (x2.item(0)-mewC2.item(0)) * (x2.item(1)-mewC2.item(1)) + pc2x3 * (x3.item(0)-mewC2.item(0)) * (x3.item(1)-mewC2.item(1)))/ (pc2x1 + pc2x2 + pc2x3)
E21c2 = E12c2

EcovarianceC2 = np.matrix([[E11c2 , E12c2],[E21c2 , E22c2]])

print("covariancia centro 1:")
print(EcovarianceC1)
print("covariancia centro 2:")
print(EcovarianceC2)

denominador = pc1x1 + pc1x2 + pc1x3 + pc2x1 + pc2x2 + pc2x3


pCentro1 = (pc1x1 + pc1x2 + pc1x3) / denominador
pCentro2 = (pc2x1 + pc2x2 + pc2x3) / denominador


print("probabilidade nova c1:")
print(pCentro1)
print("probabilidade nova c2:")
print(pCentro2)

#print(Ec1)






#=================STEP 2==================


#mew = np.matrix([[10],[15]])
#mew = np.matrix([[93.3333],[156.6667]])
mew1 = mewC1
mew2 = mewC2
#E = np.matrix([[133.3333,0],[0,33.3333]])
#E = np.matrix([[4433.3333,216.6667],[216.6667,33.3333]])
E1 = EcovarianceC1
E2 = EcovarianceC2


E1inv = np.linalg.inv(E1)
E2inv = np.linalg.inv(E2)
print("INVERSO: ")
print(E1inv)
x1 = np.matrix([[2],[4]])
x2 = np.matrix([[4],[2]])
x3 = np.matrix([[0],[0]])
#pCentro1 = 0.7
#pCentro2 = 0.3
D = 2
pi = np.pi


E1det = np.linalg.det(E1)
E2det = np.linalg.det(E2)
print("DET: ")
print(E1det)

#print(x-mew)

a = x3-mew2
b = np.matmul(a.transpose(), E2inv)
c = np.matmul(b,a) 

calc = (-1/2) * c


res = (1/(2*pi)**(D/2)) * (1/(E2det)**(1/2)) * exp(calc)
print(res)
print(res*pCentro2)

#input()
#print("\nO Q NOS QUEREMOS")
#print(0.02160168321005311 /(0.02160168321005311 + 0.0024650550232798952))
#print("O Q NOS QUEREMOS\n")

'''
x1
resC1 = 0.07896684869038663
resC2 = 0
res * pCentro1 = 0.04476667541043046
res * pCentro2 = 0


x2
resC1 = 0
resC2 = 0.11785721586498457
res * pCentro1 = 0
res * pCentro2 = 0.05104340962977256

x3
resC1 = 0.03810461317188814
resC2 = 0.005691714642595236
res * pCentro1 = 0.02160168321005311
res * pCentro2 = 0.0024650550232798952
'''


pc1x1 = 1
pc1x2 = 0       
pc1x3 = 0.897574195581

pc2x1 = 0
pc2x2 = 1     
pc2x3 = 0.10242580441899996


mewC1 = (pc1x1 * x1 + pc1x2 * x2 + pc1x3 * x3)/ (pc1x1 + pc1x2 + pc1x3)
mewC2 = (pc2x1 * x1 + pc2x2 * x2 + pc2x3 * x3)/ (pc2x1 + pc2x2 + pc2x3)

print("mew centro 1:")
print(mewC1)
print("mew centro 2:")
print(mewC2)

E11c1 = (pc1x1 * (x1.item(0)-mewC1.item(0)) * (x1.item(0)-mewC1.item(0)) + pc1x2 * (x2.item(0)-mewC1.item(0)) * (x2.item(0)-mewC1.item(0)) + pc1x3 * (x3.item(0)-mewC1.item(0)) * (x3.item(0)-mewC1.item(0)))/ (pc1x1 + pc1x2 + pc1x3)
E22c1 = (pc1x1 * (x1.item(1)-mewC1.item(1)) * (x1.item(1)-mewC1.item(1)) + pc1x2 * (x2.item(1)-mewC1.item(1)) * (x2.item(1)-mewC1.item(1)) + pc1x3 * (x3.item(1)-mewC1.item(1)) * (x3.item(1)-mewC1.item(1)))/ (pc1x1 + pc1x2 + pc1x3)
E12c1 = (pc1x1 * (x1.item(0)-mewC1.item(0)) * (x1.item(1)-mewC1.item(1)) + pc1x2 * (x2.item(0)-mewC1.item(0)) * (x2.item(1)-mewC1.item(1)) + pc1x3 * (x3.item(0)-mewC1.item(0)) * (x3.item(1)-mewC1.item(1)))/ (pc1x1 + pc1x2 + pc1x3)
E21c1 = E12c1

EcovarianceC1 = np.matrix([[E11c1 , E12c1],[E21c1 , E22c1]])


E11c2 = (pc2x1 * (x1.item(0)-mewC2.item(0)) * (x1.item(0)-mewC2.item(0)) + pc2x2 * (x2.item(0)-mewC2.item(0)) * (x2.item(0)-mewC2.item(0)) + pc2x3 * (x3.item(0)-mewC2.item(0)) * (x3.item(0)-mewC2.item(0)))/ (pc2x1 + pc2x2 + pc2x3)
E22c2 = (pc2x1 * (x1.item(1)-mewC2.item(1)) * (x1.item(1)-mewC2.item(1)) + pc2x2 * (x2.item(1)-mewC2.item(1)) * (x2.item(1)-mewC2.item(1)) + pc2x3 * (x3.item(1)-mewC2.item(1)) * (x3.item(1)-mewC2.item(1)))/ (pc2x1 + pc2x2 + pc2x3)
E12c2 = (pc2x1 * (x1.item(0)-mewC2.item(0)) * (x1.item(1)-mewC2.item(1)) + pc2x2 * (x2.item(0)-mewC2.item(0)) * (x2.item(1)-mewC2.item(1)) + pc2x3 * (x3.item(0)-mewC2.item(0)) * (x3.item(1)-mewC2.item(1)))/ (pc2x1 + pc2x2 + pc2x3)
E21c2 = E12c2

EcovarianceC2 = np.matrix([[E11c2 , E12c2],[E21c2 , E22c2]])

print("covariancia centro 1:")
print(EcovarianceC1)
print("covariancia centro 2:")
print(EcovarianceC2)

denominador = pc1x1 + pc1x2 + pc1x3 + pc2x1 + pc2x2 + pc2x3


pCentro1 = (pc1x1 + pc1x2 + pc1x3) / denominador
pCentro2 = (pc2x1 + pc2x2 + pc2x3) / denominador


print("probabilidade nova c1:")
print(pCentro1)
print("probabilidade nova c2:")
print(pCentro2)
print('\n')

#print(Ec1)




Ukl = np.matrix('-0.8234 0.567; 0.567 0.8234')

x1 = np.matrix('2; 4')
x2 = np.matrix('4; 2')
x3 = np.matrix('0; 4')
x4 = np.matrix('1; 5')

print(np.dot(Ukl, x1))
print('\n')

print(np.dot(Ukl, x2))
print('\n')

print(np.dot(Ukl, x3))
print('\n')

print(np.dot(Ukl, x4))
print('\n')















