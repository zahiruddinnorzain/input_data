import os
while True:
	nama = raw_input("nama apa: ")
	umur = raw_input("umur berapa: ")

	file = open("qw.csv","a")
	file.write(nama + ',' + umur + '\n')
	file.close()
	os.system('clear')

	