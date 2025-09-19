"""
CMPS 6610  Problem Set 2
See problemset-02.pdf for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec))
    

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
    assert binary2int(quadratic_multiply(BinaryNumber(2), BinaryNumber(2))) == 2*2

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
    
    

