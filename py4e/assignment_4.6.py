def computepay(h, r):
    if h > 40:
        p = 1.5 * r * (h - 40) + (40 *r)
    else:
        p = h * r
    return p

hrs = input("Enter Hours:")
hr = float(hrs)
rate = input("Enter Rate:")
rphr = float(rate)

p = computepay(hr, rphr)
print("Pay", p)
