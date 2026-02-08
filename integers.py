num=2512
print(num)
print(type(num))

#decimal formate to (bin, oct & hex)

binary=bin(num)
print("binary formate is : ",binary)
octal=oct(num)
print("octal formate is : ",octal)
hexa_decimal=hex(num)
print("hexa decimal formate is : ", hexa_decimal)

# create floting-point numbers
a=10.5
b=3.2

#arithmetic operations
add=a+b
sub=a-b
mul=a*b
div=a/b

print("a =", a, "type:", type(a))
print("b =", b, "type:", type(b))
print("addition : ", add)
print("subtraction:", sub)
print("multiplecation:", mul)
print("division:", div)

# create complex number using direct notation
c1= 3 + 4j
c2= 1 + 2j

# creat complex number using complex() funtion
c3 = complex(5,6)


# access real and imaginary parts
print("\nreal part of c1:", c1.real)
print("imaginary part of c1:", c1.imag)
print("c1+c2=", c1 + c2)
print("c1-c2=", c1 - c2)
print("c1*c2=", c1 * c2)
print("c1/c2=", c1 / c2)
