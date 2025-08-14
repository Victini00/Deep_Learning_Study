import numpy as np 

'''
y = 0 if (w1x1 + w2x2 + ...) > theta, 1, otherwise.

this is Perceptron!

we can implement and, or, nand..

'''

def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7

    bias = 0.1
    
    temp = x1 * w1 + x2 * w2 + bias

    if temp <= theta: return 0
    else: return 1

def AND(x1, x2): # using numpy
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])

    b = -0.7 # makes theta as bias

    temp = np.sum(x*w) + b

    if temp <= 0: return 0
    else: return 1


'''
How about XOR?

Limitation of Perceptron ~ linear

Solutions)

1. multi - layer Perceptron

XOR = AND(OR, NAND)

2. Kernel trick

feature map: [x1, x2] ~ [x1, x2, x1^2, x1x2, x2^2]
'''

# Make all Logical gates using only NAND

def NAND(x1, y1):
    if x1 and y1: return False
    else: return True

def NOT(x1):
    return NAND(x1, x1)

def AND(x1, y1):
    return NAND(NAND(x1, y1), NAND(x1, y1)) # NOT(NAND) = AND

def OR(x1, y1):
    return NAND(NAND(x1, x1), NAND(y1, y1)) # a or b = not(not a and not b)

def XOR(x1, y1):
    return NAND(NAND(NAND(x1, x1), NAND(x1, y1)), NAND(NAND(y1, y1), NAND(x1, y1)))

# Only using 2-layer perceptron NAND, we can make COMPUTER