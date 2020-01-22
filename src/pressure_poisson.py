def build_up_b(rho, dt, dx, dy, u, v):
    import numpy
    b = numpy.zeros_like(u)
    b[1:-1, 1:-1] = (rho * (1 / dt * ((u[1:-1, 2:] - u[1:-1, 0:-2]) / (2 * dx) +
                                      (v[2:, 1:-1] - v[0:-2, 1:-1]) / (2 * dy)) -
                            ((u[1:-1, 2:] - u[1:-1, 0:-2]) / (2 * dx)) ** 2 -
                            2 * ((u[2:, 1:-1] - u[0:-2, 1:-1]) / (2 * dy) *
                                 (v[1:-1, 2:] - v[1:-1, 0:-2]) / (2 * dx)) -
                            ((v[2:, 1:-1] - v[0:-2, 1:-1]) / (2 * dy)) ** 2))

    # Periodic BC Pressure @ x = 2
    b[1:-1, -1] = (rho * (1 / dt * ((u[1:-1, 0] - u[1:-1, -2]) / (2 * dx) +
                                    (v[2:, -1] - v[0:-2, -1]) / (2 * dy)) -
                          ((u[1:-1, 0] - u[1:-1, -2]) / (2 * dx)) ** 2 -
                          2 * ((u[2:, -1] - u[0:-2, -1]) / (2 * dy) *
                               (v[1:-1, 0] - v[1:-1, -2]) / (2 * dx)) -
                          ((v[2:, -1] - v[0:-2, -1]) / (2 * dy)) ** 2))

    # Periodic BC Pressure @ x = 0
    b[1:-1, 0] = (rho * (1 / dt * ((u[1:-1, 1] - u[1:-1, -1]) / (2 * dx) +
                                   (v[2:, 0] - v[0:-2, 0]) / (2 * dy)) -
                         ((u[1:-1, 1] - u[1:-1, -1]) / (2 * dx)) ** 2 -
                         2 * ((u[2:, 0] - u[0:-2, 0]) / (2 * dy) *
                              (v[1:-1, 1] - v[1:-1, -1]) / (2 * dx)) -
                         ((v[2:, 0] - v[0:-2, 0]) / (2 * dy)) ** 2))

    return b


def solve(p, rho, dt, dx, dy, u, v, nit):
    import numpy

    b = build_up_b(rho, dt, dx, dy, u, v)
    pn = numpy.empty_like(p)

    for q in range(nit):
        pn = p.copy()

        p[1:-1, 1:-1] = (((pn[1:-1, 2:] + pn[1:-1, 0:-2]) * dy ** 2 +
                          (pn[2:, 1:-1] + pn[0:-2, 1:-1]) * dx ** 2) /
                         (2 * (dx ** 2 + dy ** 2)) -
                         dx ** 2 * dy ** 2 / (2 * (dx ** 2 + dy ** 2)) * b[1:-1, 1:-1])

        p=enforce_bc_channel(p,pn,dx,dy,b)

    return p

def enforce_bc_channel(p,pn,dx,dy,b):
    # Periodic BC Pressure @ x = 2
    p[1:-1, -1] = (((pn[1:-1, 0] + pn[1:-1, -2]) * dy ** 2 +
                    (pn[2:, -1] + pn[0:-2, -1]) * dx ** 2) /
                   (2 * (dx ** 2 + dy ** 2)) -
                   dx ** 2 * dy ** 2 / (2 * (dx ** 2 + dy ** 2)) * b[1:-1, -1])

    # Periodic BC Pressure @ x = 0
    p[1:-1, 0] = (((pn[1:-1, 1] + pn[1:-1, -1]) * dy ** 2 +
                   (pn[2:, 0] + pn[0:-2, 0]) * dx ** 2) /
                  (2 * (dx ** 2 + dy ** 2)) -
                  dx ** 2 * dy ** 2 / (2 * (dx ** 2 + dy ** 2)) * b[1:-1, 0])

    # Wall boundary conditions, pressure
    p[-1, :] = p[-2, :]  # dp/dy = 0 at y = 2
    p[0, :] = p[1, :]  # dp/dy = 0 at y = 0
    return p

