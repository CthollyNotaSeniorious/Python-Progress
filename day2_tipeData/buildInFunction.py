# abs() mengermbalikan nilai mutlak suatu angka
x = -5
print(abs(x)) #Output 5

# int() mengonversi string atau angka ke integer
x = 3.7
y = "10"
print(int(x)) # Output 3
print(int(y)) # Output 10

# float() mengonversi angka atau string ke floating(desimal)
x = 5
y = "3.14"
print(float(x)) # Output 5.0
print(float(y)) # Output 3.14 string haruslah angka

# len() mengembalikan panjang suatu variabel
x = [1, 2, 3, 4]
y = "Hello World!"
print(len(x)) # Output 4
print(len(y)) # Output 12

# max() mengembalikan nilai tertinggi dari suatu value sebuah variable
x = (1, 2, 3, 4) # Output 4
y = [1, 2, 3, 4] # Output 4

print(max(x))
print(max(y))

# min() mengembalikan nilai terkecil dari suatu value sebuah variable
x = (1, 2, 3, 4) # Output 1
y = [1, 2, 3, 4] # Output 1

print(min(x))
print(min(y))