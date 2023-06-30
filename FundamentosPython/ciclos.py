#ciclos
# white exp_booleana

i = 1
num = 7
while 1 <= 10:
    print (f"{num} * {i} = {num * i}")
    i += 1
else:
    print("termina el ciclo")

# ciclo for
# permite recorrer iterables
# iterable -> objeto que se puede recorrer
# for item in interable:

my_string = "Hola A Todos"
for letter in my_string:
    print(letter, end=', ')
print()

my_list = ["uno", "dos", "tres", "cuatro"]
for item in my_list:
    print(item, end=', ')
print()

# function range ()
# range (end)
for i in range(10):
    print(i, end=', ')
print()
# range (start, end)
for i in range(10, 20):
    print(i, end=', ')
print()
# range (start, end, step)
for i in range(10, 100, 10):
    print(i, end=', ')
print()