'''
Takes in a complex number c and complex z = 0 + 0i and calculates f_4(z, c) where
f_n(z_0, c_0) = f_(n-1)(z_0, c_0)^2 + c_0

I can recall absolutely no reason I would have for doing this other than someone had it in a meme and I wanted to check convergence maybe?
'''

import sys

#multiplies two complex numbers together
def complexmult(z1, z2):
	return (z1[0]*z2[0]-z1[1]*z2[1], z1[0]*z2[1]+z1[1]*z2[0])

#adds two complex numbers together
def complexadd(z1, z2):
        return (z1[0]+z2[0], z1[1]+z2[1])

#returns z^2 + c
def fn(z, c):
	return complexadd(complexmult(z,z),c)

#calculates f_n(z_0, c_0) = f_(n-1)(z_0, c_0)^2 + c_0 4 times where z = 0 and c is provided by the user
def rtest(c):
        result = (0,0)
        for i in range(0, 4):
            result = fn(result, c)
        print(result)

rtest((float(sys.argv[1]),float(sys.argv[2])))
