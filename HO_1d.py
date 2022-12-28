import numpy as np
import matplotlib.pyplot as plt

## the latex display shall run only in jupyter notebook if
## this code is to be run in the console remove the line 2 and the display line

def harmonic_trial(x,alpha):
    return (alpha/np.pi)**0.5*np.exp(-alpha*(x**2) )

def local_en(x,alpha):
    return alpha + (0.5 - 2*alpha**2)*x**2

def distribution(x,alpha):
    return ( harmonic_trial(x , alpha)**2 )

def variational_int(alpha, Npoints=1000):
    l = 3*(1/(2*alpha))**0.5
    X = np.linspace(-l,l,Npoints)
    N=0
    su=0
    for x in X:
        if np.random.random()<distribution(x,alpha):
            su+=local_en(x,alpha)
            N+=1
    return su/N
da=0.05
alphas = []
energies = []
alpha0=0.1
N=20
for i in range(N):
    alpha = alpha0+i*da
    alphas.append(alpha)
    energies.append( variational_int(alpha,10000) )

E=min( energies )
print(r'The Ground State Energy is: {}hbar X omega'.format(E))

plt.rcParams['font.family']='serif'
plt.plot(alphas, energies,color='#F56A79',marker='D')
plt.ylabel(r'E$\to$')
plt.xlabel(r'$\alpha\to$')
plt.title('Calculation of Ground State Energy of 1-D Harmonic Oscillator')
plt.savefig('1dhovariational',dpi=300)
