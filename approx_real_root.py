def approx_real_root(coeffs, interval):
    a, b = interval
    def p(x):
        c0, c1, c2, c3 = coeffs
        return c0 + c1 * x + c2 * x**2 + c3 * x**3
    fa = p(a)
    fb = p(b)
    if fa * fb > 0:
        raise ValueError("No sign change in interval—root may not exist here!")
    tolerance = 1e-6  
    while (b - a) / 2 > tolerance:
        mid = (a + b) / 2
        f_mid = p(mid)
        if abs(f_mid) < tolerance:
            return mid
        if fa * f_mid < 0:
            b = mid
            fb = f_mid
        else:
            a = mid
            fa = f_mid
    return (a + b) / 2