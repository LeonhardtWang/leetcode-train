def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    res = ''
    crr = 0 # 进位数
    while a and b:
        sum_single = crr + int(a[-1]) + int(b[-1])
        if sum_single == 1:
            res = '1' + res
            crr = 0
        elif sum_single == 2:
            res = '0' + res
            crr = 1
        elif sum_single == 0:
            res = '0' + res
            crr = 0
        else:
            res = '1' + res
            crr = 1
        a = a[:-1]
        b = b[:-1]
    resid = max(a, b)
    if not resid:
        if crr == 0:
            return res
        else:
            return '1' + res
    else:
        while True:
            sum_resid = crr + int(resid[-1])
            if sum_resid < 2:
                return str(int(resid) + crr) + res
            else:
                res = '0' + res
                crr = 1
                resid = resid[:-1]
                if not resid:
                    return '1' + res
print(addBinary("01011", "1111111"))