import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate, fftpack
from mpl_toolkits import mplot3d
from matplotlib.animation import FuncAnimation


def odefun(t, prev_state1n, nx, ny, N, K):
    prev_state = np.reshape(prev_state1n, (2 * ny, nx))
    uinkd = prev_state[:ny, :]
    utinkd = prev_state[ny:, :]
    return np.append(utinkd, -K * uinkd)


dt = 0.1
tstart = 0
tend = 1
nt = (tend - tstart) / dt
tspan = np.linspace(tstart, tend, int(nt), endpoint=True)

Lx = 4
Ly = 2
nx = 128
ny = 64
N = nx * ny

x = np.linspace(0, Lx, nx + 2)[1:-1]
y = np.linspace(0, Ly, ny + 2)[1:-1]
X, Y = np.meshgrid(x, y)

u0intd = 0.4 * np.exp(-30 * ((X - 0.8) ** 2 + (Y-0.8) ** 2))

fig1 = plt.figure(figsize=(20, 10))
ax = plt.axes(xlim=(0, Lx), ylim=(0, Ly), zlim=(-0.2, 0.4), projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
surf=ax.plot_surface(X, Y, u0intd, cmap='jet', edgecolor='none')
fig1.colorbar(surf)
plt.show()

kx = (np.pi / Lx) * np.array(
    np.concatenate([np.linspace(1, nx / 2, int(nx / 2)), np.linspace((-nx / 2) + 1, 0, int(nx / 2))]))
ky = (np.pi / Ly) * np.array(
    np.concatenate([np.linspace(1, ny / 2, int(ny / 2)), np.linspace((-ny / 2) + 1, 0, int(ny / 2))]))
kx[0] = 1e-6
ky[0] = 1e-6

KX, KY = np.meshgrid(kx, ky)
K = KX ** 2 + KY ** 2

u0inkd = fftpack.dst(fftpack.dst(u0intd, type=1, axis=1), type=1, axis=0)
u0tinkd = fftpack.dst(fftpack.dst(0.1 * u0intd, type=1, axis=1), type=1, axis=0)

ini_cond = np.append(u0inkd, u0tinkd)

fun = lambda t, y: odefun(t, y, nx, ny, N, K)

soln = integrate.solve_ivp(fun, (tstart, tend), ini_cond, method='RK45', t_eval=np.linspace(0, 1, 100))
numt = len(soln.t)

for j in range(numt):
    i = j + 1
    if np.mod(i, 10) == 0:
        uinkd = np.reshape(soln.y[:, i - 1], (2 * ny, nx))[:ny, :]
        uintd = 1 / (2 * (ny + 1)) * fftpack.dst(1 / (2 * (nx + 1)) * fftpack.dst(uinkd, type=1, axis=0), type=1,
                                                 axis=1)
        fig1 = plt.figure(figsize=(20, 10))
        ax = plt.axes(xlim=(0, Lx), ylim=(0, Ly), zlim=(-0.2, 0.4), projection='3d')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        plotsnap = ax.plot_surface(X, Y, uintd.real, cmap='jet', edgecolor='none')
        plt.title("$ t $= " + str(soln.t[i - 1]))
        fig1.colorbar(plotsnap)
        plt.show()

"""
i=0

fig = plt.figure()
ax = plt.axes(xlim=(-Lx / 2, Lx / 2), ylim=(-Ly / 2, Ly / 2), zlim=(-0.2, 0.4), projection='3d')
plotsnap, =ax.plot_surface(X, Y, uintd.real, cmap='jet', edgecolor='none')

def init():
    line.set_data([], [], [], cmap='jet', edgecolor='none')
    return plotsnap,

def animate(i):
    i = i + 1
    uinkd = np.reshape(soln.y[:, i - 1], (2 * ny, nx))[:ny, :]
    uintd = np.fft.ifft(np.fft.ifft(uinkd, axis=0), axis=1)
    plotsnap.set_data(X, Y, uintd.real)
    return plotsnap,

anim = FuncAnimation(fig, animate, init_func=init,
                               frames=100, interval=20, blit=True)

"""
"""

N = 24;
x = cos(pi * arange(0, N + 1) / N);
y = x;
t = 0.0;
dt = (6.0) / (N ** 2)
xx, yy = meshgrid(x, y)
plotgap = int(round((1.0 / 3.0) / (dt)));
dt = (1.0 / 3.0) / (plotgap);
vv = exp(-40 * ((xx - 0.4) ** 2 + yy ** 2));
vvold = vv;

# Time stepping Leapfrog Formula:
fig = figure(figsize=(10, 10))
k = 1;
for n in range(0, (3 * plotgap) + 1):
    t = n * dt;
    if (remainder(n + 0.5, plotgap) < 1):
        ax = fig.add_subplot(2, 2, k, projection='3d')
        f = interp2d(x, y, vv, kind='cubic');
        xxx = arange(-1., 1. + 1. / 16, 1. / 16);
        vvv = f(xxx, xxx)
        X, Y = meshgrid(xxx, xxx);
        ax.plot_surface(X, Y, vvv, rstride=1, cstride=1, cmap=cm.jet)
        ax.set_zlim3d([-0.15, 1])
        ax.set_xlim3d([-1, 1])
        ax.set_ylim3d([-1, 1])
        ax.view_init(elev=40., azim=250.)
        title("$ t $= " + str(t))
        xlabel("x");
        ylabel("y");
        k = k + 1;


    uxx = zeros((N + 1, N + 1));
    uyy = zeros((N + 1, N + 1));
    ii = arange(1, N);

    for i in range(1, N):
        v = vv[i, :];
        V = list(v) + list(flipud(v[ii]));
        U = real(fft(V));
        w1_hat = 1j * zeros(2 * N);
        w1_hat[0:N] = 1j * arange(0, N)
        w1_hat[N + 1:] = 1j * arange(-N + 1, 0)
        W1 = real(ifft(w1_hat * U))
        w2_hat = 1j * zeros(2 * N);
        w2_hat[0:N + 1] = arange(0, N + 1)
        w2_hat[N + 1:] = arange(-N + 1, 0)
        W2 = real(ifft((-w2_hat ** 2) * U))
        uxx[i, ii] = W2[ii] / (1 - x[ii] ** 2) - (x[ii] * W1[ii]) / (1 - x[ii] ** 2) ** (3.0 / 2);
    for j in range(1, N):
        v = vv[:, j];
        V = list(v) + list(flipud(v[ii]));
        U = real(fft(V))
        w1_hat = 1j * zeros(2 * N);
        w1_hat[0:N] = 1j * arange(0, N)
        w1_hat[N + 1:] = 1j * arange(-N + 1, 0)
        W1 = real(ifft(w1_hat * U))
        w2_hat = 1j * zeros(2 * N);
        w2_hat[0:N + 1] = arange(0, N + 1)
        w2_hat[N + 1:] = arange(-N + 1, 0)
        W2 = real(ifft(-(w2_hat ** 2) * U))
        uyy[ii, j] = W2[ii] / (1 - y[ii] ** 2) - y[ii] * W1[ii] / (1 - y[ii] ** 2) ** (3.0 / 2.0);
    vvnew = 2 * vv - vvold + dt ** 2 * (uxx + uyy)
    vvold = vv;
    vv = vvnew;
"""
