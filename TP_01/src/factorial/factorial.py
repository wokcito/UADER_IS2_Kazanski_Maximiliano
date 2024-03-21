#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py*
#* calcula el factorial de un número   *
#* Dr.P.E.Colla (c) 2022   *
#* Creative commons*
#*-------------------------------------------------------------------------*
import sys

# calculates the factorial of a number
def factorial(num):
	if num < 0:
		print("Factorial de un número negativo no existe")
	elif num == 0:
		return 1
	else:
		fact = 1

	while(num > 1):
		fact *= num
		num -= 1
	return fact

# calculates the factorial between two numbers
# if 'from' is not sent, it's 1 by default
# if 'to' is not sent, it's 60 by default
def calculate_range(num_range):
	num_list = num_range.split('-')

	num_from = 1 if num_list[0] == '' else int(num_list[0])
	num_to = 60 if num_list[1] == '' else int(num_list[1])

	if num_from > num_to:
		print("El primer número es mayor al segundo.")
		return

	for num in range(num_from, num_to + 1):
		print("Factorial ", num, "! es ", factorial(int(num)))

# checks if the arguments were sent with the command
if len(sys.argv) < 2:
	num = input("Ingrese un rango (ej. 4-8) o un número: ")
else:
	num = sys.argv[1]

if '-' in num:
	calculate_range(num)
	sys.exit()

print("Factorial ", num, "! es ", factorial(int(num)))
