__author__ = ''

def day(n):
    if n > 366:
        return "overflu"
    else:
        if n < 186:
            m = n/31
            d = n % 31
            return m + 1,d
        else:
            m = n - 186
            m1 = m / 31
            d = m % 30
            return m1+ 7 , d

if __name__ == '__main__':
    print day(365)
