a = [(1, ), (2, 3), (4, 5, 6)]
print(a[1][1])
b = [[1, 2, 3, 4], [5, 6, 7, 8], ["a", "b", "c", "d"], ["e", "f", "g", "h"]]
print(b[0][-2:])
print(b[0][1:-1]) # ez a megoldó kulcs szerinti, de nem az utolsó két elemét printeli az első listának, mint ahogy kéri