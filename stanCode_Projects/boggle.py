"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	Boggle game,find words
	"""
	while True:
		start = time.time()
		boggle = []		# every row of letters

		row_1 = input('1 row of letters: ')
		if len(row_1) != 7:
			print('Illegal input')
			break
		else:
			row_1 = row_1.replace(' ', '')
			boggle.append(row_1)

		row_2 = input('2 row of letters: ')
		if len(row_2) != 7:
			print('Illegal input')
			break
		else:
			row_2 = row_2.replace(' ', '')
			boggle.append(row_2)

		row_3 = input('3 row of letters: ')
		if len(row_3) != 7:
			print('Illegal input')
			break
		else:
			row_3 = row_3.replace(' ', '')
			boggle.append(row_3)

		row_4 = input('4 row of letters: ')
		if len(row_4) != 7:
			print('Illegal input')
			break
		else:
			row_4 = row_4.replace(' ', '')
			boggle.append(row_4)

		find_word(boggle)
		end = time.time()
		print('----------------------------------')
		print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_word(boggle):
	lst = read_dictionary()		# dictionary
	words = []		# all words
	total = [0]		# count for how many words
	for x in range(len(boggle)):		# for counting rows
		for y in range(len(boggle[1])):		# for counting latter of words
			position = [(x, y)]		# start position
			find_word_helper(boggle, lst, boggle[x][y], words, total, x, y, position)
	print(f'There are {total[0]} words in total.')


def find_word_helper(boggle, lst, current_s, words, total, x, y, position):
	if current_s in lst and current_s not in words:
		if current_s in lst:
			words.append(current_s)
			total[0] += 1
			print('Found: ' + current_s)
			for i in range(-1, 2):
				for j in range(-1, 2):
					if i == 0 and j == 0:
						pass
					else:
						new_x = x + i
						new_y = y + j
						if (new_x, new_y) not in position:
							if 0 <= new_x < len(boggle[1]):
								if 0 <= new_y < len(boggle):
									# Choose
									current_s += boggle[new_x][new_y]
									position.append((new_x, new_y))
									if has_prefix(current_s, lst):
										# explore
										find_word_helper(boggle, lst, current_s, words, total, new_x, new_y, position)
									# Un-choose
									current_s = current_s[:-1]
									position.pop()

	else:
		for i in range(-1, 2):
			for j in range(-1, 2):
				if i == 0 and j == 0:
					pass
				else:
					new_x = x + i
					new_y = y + j
					if (new_x, new_y) not in position:
						if 0 <= new_x < len(boggle[1]):
							if 0 <= new_y < len(boggle):
								# Choose
								current_s += boggle[new_x][new_y]
								position.append((new_x, new_y))
								if has_prefix(current_s, lst):
									# explore
									find_word_helper(boggle, lst, current_s, words, total, new_x, new_y, position)
								# Un-choose
								current_s = current_s[:-1]
								position.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		lst = []
		for line in f:
			tokens = line[:-1]
			if len(tokens) >= 4:
				lst.append(tokens)
		return lst


def has_prefix(sub_s, dictionary):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param dictionary: dictionary
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
