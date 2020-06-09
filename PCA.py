import numpy as np

print("Numero de training data:")
n = int(input())
print("Dimensao de cada dataSet:")
dim = int(input())

dataSet = [None] * n

for i in range(n):
    print("valores para o elemento numero " + str(i+1))
    listAux = []
    for e in range(dim):
        listAux += [int(input())]
    dataSet[i] = np.transpose(np.array([listAux]))

print("\ncalcular mean vector (mew)  1/n * (x1 + x2 + x3 + x4 + ... + xn):") #1/4 * (x1 + x2 + x3 + x4)
mean = dataSet[0]
for e in range(1, len(dataSet)):
    mean = mean + dataSet[e]

mean = mean/n
print(mean)

covarianceCalculus = [None] * n

print("\nCalculos aux para covariance matrix (x-mew)(x-mew)^T:")
for e in range(len(dataSet)):
    covarianceCalculus[e] = np.dot( dataSet[e] - mean, np.transpose(dataSet[e] - mean))
    print("para x" + str(e+1) + ":")
    print(covarianceCalculus[e])


covarianceMatrix = covarianceCalculus[0]
for e in range(1, len(covarianceCalculus)):
    covarianceMatrix += covarianceCalculus[e]

print("\nCovarianceMatrix (1/(n-1)) * (soma dos calculos anteriores):")
covarianceMatrix = (1/(n-1)) * covarianceMatrix
print(covarianceMatrix)

print("\nEigenValues and EigenVectors:")
w,v = np.linalg.eig(covarianceMatrix)
print(w)
print(v)