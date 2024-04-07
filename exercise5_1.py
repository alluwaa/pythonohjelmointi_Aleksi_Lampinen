# a) 
counter = 1
while counter < 51:
    print(counter)
    counter = counter +1
# b)
for x in range(50):
    print(x+1)
# c)
counter = 1
lopputulos = 0
while counter < 31:
    lopputulos += counter
    counter = counter +1
print("Summa: " + str(lopputulos))
# d)
for vuosiluku in range(2005, 2011):
    print(vuosiluku, end=' ')
