from matlapy import Matlapy, Block


mat = Matlapy()


print(mat.eng)
print(mat.connection.connect_first_matlab())
print(mat.eng)


b = Block()
print(b.eng)



mat2 = Matlapy()

print(mat2.connection.connect_first_matlab())

mat2.Block()