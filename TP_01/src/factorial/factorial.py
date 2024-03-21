#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py*
#* calcula el factorial de un número   *
#* Dr.P.E.Colla (c) 2022   *
#* Creative commons*
#*-------------------------------------------------------------------------*
import sys

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

def calculate_range(num_range):
	num_list = num_range.split('-')

	num_from = int(num_list[0])
	num_to = int(num_list[1])

	if num_from > num_to:
		print("El primer número es mayor al segundo.")
		sys.exit()

	for num in range(num_from, num_to + 1):
		print("Factorial ", num, "! es ", factorial(int(num)))

if len(sys.argv) < 2:
	num_range = input("Ingrese un rango (ej. 4-8): ")
	calculate_range(num_range)
