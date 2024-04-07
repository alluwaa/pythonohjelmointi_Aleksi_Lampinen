import functions

print("Anna tunnit")
hours = int(input())
print("Anna minuutit")
minutes = int(input())
print("Anna sekunnit")
seconds = int(input())
print("Yhteensä " + str(functions.count_seconds(hours, minutes, seconds)) + " sekuntia")