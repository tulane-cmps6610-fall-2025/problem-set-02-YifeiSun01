"""
CMPS 6610  Problem Set 2
See problemset-02.pdf for details.
"""
import time
import tabulate

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

# some useful utility functions to manipulate bit vectors
def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y
    
def add_bn(a: BinaryNumber, b: BinaryNumber) -> BinaryNumber:
    return BinaryNumber(a.decimal_val + b.decimal_val)

def sub_bn(a: BinaryNumber, b: BinaryNumber) -> BinaryNumber:
    return BinaryNumber(a.decimal_val - b.decimal_val)

def quadratic_multiply(x: BinaryNumber, y: BinaryNumber) -> BinaryNumber:
    if len(x.binary_vec) == 1 and len(y.binary_vec) == 1:
        bit = '1' if (x.binary_vec[0] == '1' and y.binary_vec[0] == '1') else '0'
        return binary2int([bit])
    x_bits, y_bits = pad(x.binary_vec, y.binary_vec)
    n = len(x_bits)
    x1, x2 = split_number(x_bits)
    y1, y2 = split_number(y_bits)
    z2 = quadratic_multiply(x1, y1)
    z0 = quadratic_multiply(x2, y2)
    z1a = quadratic_multiply(x1, y2)
    z1b = quadratic_multiply(x2, y1)
    z1 = add_bn(z1a, z1b)
    return add_bn(add_bn(bit_shift(z2, n), bit_shift(z1, n//2)), z0)

def subquadratic_multiply(x: BinaryNumber, y: BinaryNumber) -> BinaryNumber:
    if len(x.binary_vec) == 1 and len(y.binary_vec) == 1:
        bit = '1' if (x.binary_vec[0] == '1' and y.binary_vec[0] == '1') else '0'
        return binary2int([bit])
    x_bits, y_bits = pad(x.binary_vec, y.binary_vec)
    n = len(x_bits)
    x1, x2 = split_number(x_bits)
    y1, y2 = split_number(y_bits)
    z2 = subquadratic_multiply(x1, y1)
    z0 = subquadratic_multiply(x2, y2)
    s1 = add_bn(x1, x2)
    s2 = add_bn(y1, y2)
    p = subquadratic_multiply(s1, s2)
    z1 = sub_bn(sub_bn(p, z2), z0)
    return add_bn(add_bn(bit_shift(z2, n), bit_shift(z1, n//2)), z0)

## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)).decimal_val == 2*2
    assert quadratic_multiply(BinaryNumber(8), BinaryNumber(9)).decimal_val == 8*9
    assert subquadratic_multiply(BinaryNumber(2), BinaryNumber(2)).decimal_val == 2*2
    assert subquadratic_multiply(BinaryNumber(8), BinaryNumber(9)).decimal_val == 8*9

# some timing functions here that will make comparisons easy    
def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    f(x,y)
    return (time.time() - start)*1000
    
def compare_multiply():
    res = []
    for n in [10,100,1000,10000,100000,1000000,10000000,100000000,1000000000]:
        qtime = time_multiply(BinaryNumber(n), BinaryNumber(n), quadratic_multiply)
        subqtime = time_multiply(BinaryNumber(n), BinaryNumber(n), subquadratic_multiply)        
        res.append((n, qtime, subqtime))
    print_results(res)


def print_results(results):
    print("\n")
    print(
        tabulate.tabulate(
            results,
            headers=['n', 'quadratic', 'subquadratic'],
            floatfmt=".3f",
            tablefmt="github"))

import random, statistics, timeit

def rand_binarynumber_with_bits(L: int) -> BinaryNumber:
    if L <= 1:
        return BinaryNumber(random.randint(0, 1))
    x = random.getrandbits(L) | (1 << (L-1))
    return BinaryNumber(x)

def bench_one(f, L: int, repeats: int = 7) -> float:
    def run_once():
        a = rand_binarynumber_with_bits(L)
        b = rand_binarynumber_with_bits(L)
        f(a, b)
    t = timeit.Timer(run_once)
    return statistics.median(t.repeat(repeat=repeats, number=1))

def compare_multiply_bits():
    rows = []
    for L in [2,4,6,8,10,12,14,20,25,30,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200]:
        tq = bench_one(quadratic_multiply, L)
        tk = bench_one(subquadratic_multiply, L)
        rows.append((L, tq*1000, tk*1000)) 
    print_results(rows)





|   n |   quadratic |   subquadratic |
|-----|-------------|----------------|
|   2 |       0.018 |          0.035 |
|   4 |       0.079 |          0.156 |
|   6 |       0.164 |          0.239 |
|   8 |       0.292 |          0.366 |
|  10 |       0.545 |          0.878 |
|  12 |       0.724 |          0.761 |
|  14 |       0.640 |          0.580 |
|  20 |       1.025 |          1.143 |
|  25 |       1.758 |          1.554 |
|  30 |       2.488 |          2.464 |
|  50 |       7.125 |          4.613 |
|  60 |       9.344 |          6.610 |
|  70 |      13.810 |          8.052 |
|  80 |      23.539 |         11.906 |
|  90 |      25.807 |         19.141 |
| 100 |      30.891 |         14.950 |
| 110 |      43.372 |         20.303 |
| 120 |      41.930 |         21.286 |
| 130 |      47.377 |         26.159 |
| 140 |      61.378 |         28.863 |
| 150 |      90.338 |         28.867 |
| 160 |      90.870 |         38.696 |
| 170 |      93.032 |         34.520 |
| 180 |     176.236 |         65.683 |
| 190 |     186.096 |         79.118 |
| 200 |     196.309 |         77.219 |

