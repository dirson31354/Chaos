import numpy as np
import matplotlib.pyplot as plt

def logistic(mu,x0,niter):
    val_array = [x0]
    x = x0 # to avoid confusion
    for i in range(niter):
        x = mu*x*(1-x)
        val_array.append(x)
    return val_array

#x = logistic(2.75,0.8,100)
#iter_ls = [i for i in range(101)]
#plt.plot(iter_ls, x)
#plt.title("Population vs Year for a= 2.5, x_0=0.9")
#plt.xlabel("Years")
#plt.ylabel("Population")
#plt.show()
Iter= []
counter=-1
for i in range (1001):
    Iter.append(counter+1)
    counter= counter+1

case2= logistic(3.8701,0.7,1000)
case2b= logistic(3.8705,0.7,1000)
case2c= logistic(3.8709,0.7,1000) 
case2d= logistic(3.8713,0.7,1000)

plt.plot(Iter, case2, label= 'a=3.8701, 0.7')
plt.plot(Iter, case2b, label= 'a=3.8705, 0.7')
plt.plot(Iter, case2c, label= 'a=3.8709, 0.7') 
plt.plot(Iter, case2d, label= 'a=3.8713, 0.7') 
plt.legend()
plt.xlabel('Generations')
plt.ylabel('Population')
plt.title('Behavior for small changes in a')
plt.show()
