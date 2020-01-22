import numpy
from matplotlib import pyplot, cm
from scipy.fftpack import dst
from mpl_toolkits.mplot3d import Axes3D


def plot2D(x, y, p):
    fig = pyplot.figure(figsize=(11, 7), dpi=100)
    ax = fig.gca(projection='3d')
    X, Y = numpy.meshgrid(x, y)
    surf = ax.plot_surface(X, Y, p[:], rstride=1, cstride=1, cmap=cm.viridis,
            linewidth=0, antialiased=False)
    ax.view_init(30, 225)
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    pyplot.show()


# Parameters
nx = 64
ny = 64
nt  = 100
xmin = 0
xmax = 2
ymin = 0
ymax = 1
Lx=xmax-xmin
Ly=ymax-ymin

dx = (xmax - xmin) / (nx - 1)
dy = (ymax - ymin) / (ny - 1)

# Initialization
p  = numpy.zeros((ny, nx))
pd = numpy.zeros((ny, nx))
b  = numpy.zeros((ny, nx))
x  = numpy.linspace(xmin, xmax, nx)
y  = numpy.linspace(ymin, ymax, ny)

# Source
b[int(ny / 4), int(nx / 4)]  = 100
b[int(3 * ny / 4), int(3 * nx / 4)] = -100
bk=dst(dst(b[1:-1,1:-1],type=1,axis=1),type=1,axis=0)

nx_sp=nx-2
ny_sp=ny-2
kx = numpy.array([(numpy.pi*(i+1)/Lx) for i in range(-1,nx_sp+1)])[1:-1]
ky = numpy.array([(numpy.pi*(i+1)/Ly) for i in range(-1,ny_sp+1)])[1:-1]
KX, KY = numpy.meshgrid(kx, ky)
K = KX ** 2 + KY ** 2

pk=bk/(-K)

p[1:-1,1:-1]=dst(dst(pk,type=1,axis=0)/(2*(ny_sp+1)),type=1,axis=1)/(2*(nx_sp+1))

plot2D(x, y, p)