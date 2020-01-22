"""
https://scicomp.stackexchange.com/questions/32491/fft-solver-for-the-poisson-problem-with-dirichlet-boundary-conditions
"""

from scipy.fftpack import dst
import numpy as np
import matplotlib.pyplot as plt
import time

def Poisson_1D(mu,f,N):
    x = np.linspace(0,1,N)
    hh = (x[1]-x[0])**2
    NN = x.size
    u = np.zeros(NN)
    d = 2*np.ones(NN-2)
    dd = -1*np.ones(NN-3)
    A = np.diag(d) + np.diag(dd,1) + np.diag(dd,-1)
    ff = f(x[1:-1])*hh/mu
    u[1:-1] = np.linalg.solve(A,ff)
    return x,u

def Poisson_fft_1D(mu,f,N,L=1):
    dx=L/(N-1)
    N=N-2
    x = np.linspace(0,L,N+2)[1:-1]
    ff = f(x)
    F = dst(ff,type=1)
    k = np.array([(np.pi*(i+1)/L)**2 for i in range(-1,N+1)])[1:-1]
    U = F/(mu*k)
    u = dst(U,type=1)/(2*(N+1))
    return x, u

def f3(x): return 16*mu*np.pi**2*np.sin(4*np.pi*x)
def u3(x): return np.sin(4*np.pi*x)

if __name__ == "__main__":


    error_fd = []
    error_fft = []
    nlist = np.arange(3,13)
    for n in nlist:
        N = 2**n
        mu = 1
        # FINITE DIFFERENCE
        t1 = time.time()
        x,u = Poisson_1D(mu,f3,N)
        t2 = time.time() - t1
        ue = u3(x)
        # FFT
        t3 = time.time()
        x_fft,u_fft = Poisson_fft_1D(mu,f3,N)
        t4 = time.time() - t3
        ue_fft = u3(x_fft)
        # ERRORS
        e1 = np.sqrt(np.sum((ue_fft-u_fft)**2))
        e2 = np.sqrt(np.sum((ue-u)**2))
        error_fft.append( e1 )
        error_fd.append( e2  )
        print("N : {2:10d}   ,   error fft : {0:5.3e}   ,   time fft : {3:5.3e}   ,   error df : {1:5.3e}   ,   time df : {4:5.3e}".format(e1,e2,N,t4,t2))
        fig1=plt.figure(1)
        plt.plot(x_fft, u_fft, "+-", label='FFT')
        plt.plot(x, u, "x-", label='Finite difference')
        plt.legend()
        plt.show()


fig1=plt.figure(2)
plt.plot(np.log2(2**nlist),np.log2(error_fft),"+-",label='FFT')
plt.plot(np.log2(2**nlist),np.log2(error_fd),"x-",label='Finite difference')
plt.plot(np.log2(2**nlist),-np.log2(2**nlist),"k--",label=r"$y=-x$")
plt.plot(np.log2(2**nlist),-2*np.log2(2**nlist),"b--",label=r"$y=-2x$")

plt.legend()
plt.show()




