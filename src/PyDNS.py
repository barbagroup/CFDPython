#!venv/bin/python
def PyDNS():
    import numpy
    from matplotlib import pyplot
    from src import pressure_poisson

    ##variable declarations
    nx = 64
    ny = 64
    nt = 10
    nit = 100
    c = 1
    Lx=2
    Ly=2
    dx = Lx / (nx - 1)
    dy = Ly / (ny - 1)
    x = numpy.linspace(0, Lx, nx)
    y = numpy.linspace(0, Ly, ny)
    X, Y = numpy.meshgrid(x, y)

    ##physical variables
    rho = 1
    nu = .1
    F = 1
    dt = .005

    # initial conditions
    u = numpy.zeros((ny, nx))
    un = numpy.zeros((ny, nx))

    v = numpy.zeros((ny, nx))
    vn = numpy.zeros((ny, nx))

    p = numpy.ones((ny, nx))
    pn = numpy.ones((ny, nx))

    b = numpy.zeros((ny, nx))

    udiff = 1
    stepcount = 0

    while udiff > .001:
        un = u.copy()
        vn = v.copy()

        #p = pressure_poisson.solve(p, rho, dt, dx, dy, u, v, nit)

        p = pressure_poisson.solve_spectral(p, rho, dt, dx, dy, u, v, X, Y)

        u[1:-1, 1:-1] = (un[1:-1, 1:-1] -
                         un[1:-1, 1:-1] * dt / dx *
                         (un[1:-1, 1:-1] - un[1:-1, 0:-2]) -
                         vn[1:-1, 1:-1] * dt / dy *
                         (un[1:-1, 1:-1] - un[0:-2, 1:-1]) -
                         dt / (2 * rho * dx) *
                         (p[1:-1, 2:] - p[1:-1, 0:-2]) +
                         nu * (dt / dx ** 2 *
                               (un[1:-1, 2:] - 2 * un[1:-1, 1:-1] + un[1:-1, 0:-2]) +
                               dt / dy ** 2 *
                               (un[2:, 1:-1] - 2 * un[1:-1, 1:-1] + un[0:-2, 1:-1])) +
                         F * dt)

        v[1:-1, 1:-1] = (vn[1:-1, 1:-1] -
                         un[1:-1, 1:-1] * dt / dx *
                         (vn[1:-1, 1:-1] - vn[1:-1, 0:-2]) -
                         vn[1:-1, 1:-1] * dt / dy *
                         (vn[1:-1, 1:-1] - vn[0:-2, 1:-1]) -
                         dt / (2 * rho * dy) *
                         (p[2:, 1:-1] - p[0:-2, 1:-1]) +
                         nu * (dt / dx ** 2 *
                               (vn[1:-1, 2:] - 2 * vn[1:-1, 1:-1] + vn[1:-1, 0:-2]) +
                               dt / dy ** 2 *
                               (vn[2:, 1:-1] - 2 * vn[1:-1, 1:-1] + vn[0:-2, 1:-1])))

        # Periodic BC u @ x = 2
        u[1:-1, -1] = (un[1:-1, -1] - un[1:-1, -1] * dt / dx *
                       (un[1:-1, -1] - un[1:-1, -2]) -
                       vn[1:-1, -1] * dt / dy *
                       (un[1:-1, -1] - un[0:-2, -1]) -
                       dt / (2 * rho * dx) *
                       (p[1:-1, 0] - p[1:-1, -2]) +
                       nu * (dt / dx ** 2 *
                             (un[1:-1, 0] - 2 * un[1:-1, -1] + un[1:-1, -2]) +
                             dt / dy ** 2 *
                             (un[2:, -1] - 2 * un[1:-1, -1] + un[0:-2, -1])) + F * dt)

        # Periodic BC u @ x = 0
        u[1:-1, 0] = (un[1:-1, 0] - un[1:-1, 0] * dt / dx *
                      (un[1:-1, 0] - un[1:-1, -1]) -
                      vn[1:-1, 0] * dt / dy *
                      (un[1:-1, 0] - un[0:-2, 0]) -
                      dt / (2 * rho * dx) *
                      (p[1:-1, 1] - p[1:-1, -1]) +
                      nu * (dt / dx ** 2 *
                            (un[1:-1, 1] - 2 * un[1:-1, 0] + un[1:-1, -1]) +
                            dt / dy ** 2 *
                            (un[2:, 0] - 2 * un[1:-1, 0] + un[0:-2, 0])) + F * dt)

        # Periodic BC v @ x = 2
        v[1:-1, -1] = (vn[1:-1, -1] - un[1:-1, -1] * dt / dx *
                       (vn[1:-1, -1] - vn[1:-1, -2]) -
                       vn[1:-1, -1] * dt / dy *
                       (vn[1:-1, -1] - vn[0:-2, -1]) -
                       dt / (2 * rho * dy) *
                       (p[2:, -1] - p[0:-2, -1]) +
                       nu * (dt / dx ** 2 *
                             (vn[1:-1, 0] - 2 * vn[1:-1, -1] + vn[1:-1, -2]) +
                             dt / dy ** 2 *
                             (vn[2:, -1] - 2 * vn[1:-1, -1] + vn[0:-2, -1])))

        # Periodic BC v @ x = 0
        v[1:-1, 0] = (vn[1:-1, 0] - un[1:-1, 0] * dt / dx *
                      (vn[1:-1, 0] - vn[1:-1, -1]) -
                      vn[1:-1, 0] * dt / dy *
                      (vn[1:-1, 0] - vn[0:-2, 0]) -
                      dt / (2 * rho * dy) *
                      (p[2:, 0] - p[0:-2, 0]) +
                      nu * (dt / dx ** 2 *
                            (vn[1:-1, 1] - 2 * vn[1:-1, 0] + vn[1:-1, -1]) +
                            dt / dy ** 2 *
                            (vn[2:, 0] - 2 * vn[1:-1, 0] + vn[0:-2, 0])))

        # Wall BC: u,v = 0 @ y = 0,2
        u[0, :] = 0
        u[-1, :] = 0
        v[0, :] = 0
        v[-1, :] = 0

        udiff = (numpy.sum(u) - numpy.sum(un)) / numpy.sum(u)
        stepcount += 1

        print(stepcount)

    fig = pyplot.figure(figsize=(11, 7), dpi=100)
    pyplot.quiver(X[::3, ::3], Y[::3, ::3], u[::3, ::3], v[::3, ::3])

    fig = pyplot.figure(figsize=(11, 7), dpi=100)
    pyplot.quiver(X, Y, u, v)

    pyplot.show(block=True)

if __name__ == "__main__":
    PyDNS()
