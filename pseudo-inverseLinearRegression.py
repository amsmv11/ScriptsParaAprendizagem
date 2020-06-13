import numpy as np

#X = np.matrix('1 0.8 0.64 0.512; 1 1 1 1; 1 1.2 1.44 1.728; 1 1.4 1.96 2.744; 1 1.6 2.56 4.096')
X = np.matrix('1 1 1; 1 2 1; 1 1 3; 1 3 3')

#targets = np.matrix('24; 20; 10; 13; 12')
targets = np.matrix('1.4; 0.5; 2.0; 2.5')

XT = X.transpose()

print(X)

print("TRANSPOSED IS: ")

print(XT)

A = np.dot(XT, X)

Ainv = np.linalg.inv(A)


print("\nTHIS IS A: ")
print(A)

print("\nTHIS IS A^-1: ")
print(Ainv)


print("THIS IS targets: ")
print(targets)


res = np.dot( np.linalg.inv(A) , XT)

res = np.dot(res , targets)


print("THIS IS W:")
print(res)

