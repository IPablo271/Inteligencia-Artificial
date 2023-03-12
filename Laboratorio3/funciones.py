import numpy as np

hyp = lambda x,th: sum([x[i] * th[i] for i in range(len(th))])
costo = lambda X,y,th: sum([(hyp(X[i],th) -y[i]) **2 for i in range(len(y))]) / len(y)
    #Tood: fo

def hyp2(x,th):
    res = 0
    for i in range(len(th)):
        res += x[i] * th[i]

    return res

def cost2(X,y,th):
    res = 0
    for i in range(len(y)):
        res+= (hyp(X[i],th) - y[i] ** 2)
    return res/len(y)

#X -> (m,n)
#T -> (n,1)
#Y -> (n,1)

cost3 = lambda X,y,t: ((X @ t - y) ** 2).sum() /len(y) 


def gradient(X,Y,th):
    grad = []
    for j in range(len(X[0])):
        res = 0
        for i in range(len(Y)):
            res+= hyp2(X[i],th) - Y[i] * X[i][j]

        grad.append(2* res / len(Y))
    
    return grad

gardn = lambda X,y,t : 2 * X.T @ (X @ t - y) / len(y)


def linear_regression(X,y,t,a, n=10000):
    #X todos los valores de entrada
    # Y valores de salida
    # T teta
    # a learning rate
    # n cantidad de iteraciones
    for i in range(n):
        t -= a * gardn(X,y,t)
        if np.sqrt(t**2).sum() <0.5:
            return t
def linear_regression(X,y,theta,a,threshold, n=10000,): #Metodo final
    while True:
        nabla = gardn(X,y,theta)
        theta -= a * nabla

        if np.sqrt(nabla ** 2).sum() < threshold:
            return theta
        
        #Np range de 1000 elementos y le agregamos una columna de unos

def linear_regression(X,y,t,a, n=10000):
    while(True):
            t -= a * gardn(X,y,t)
            if np.sqrt(t**2).sum() <0.5:
                return t







