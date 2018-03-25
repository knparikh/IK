def power(base, power):
    if power == 0:
        return 1

    if power == 1:
        return base

    temp = power(base, power/2)

    # Even powers
    if (power % 2) == 0:
        return temp*temp
    else:
        if power > 0:
            return base*temp*temp
        else:
            return temp*temp/base   # temp is containing 1/xpowy, and for odd case, this is multiplying by 1/base
    
_dblbase = float(input());
_ipower = int(input());
res = pow(_dblbase, _ipower);
print res
