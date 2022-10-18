"""
File: largest_digit.py
Name: Adam
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, find the largest number
	:return: largest number
	"""
	if n < 0:
		n = -n
	max_num = -float('inf')
	max_num = find_largest_digit_helper(n, max_num)
	return max_num


def find_largest_digit_helper(n, max_num):
	if n < 10:
		if n > max_num:
			max_num = n % 10
		return max_num
	else:
		if n % 10 > max_num:
			max_num = n % 10
		return find_largest_digit_helper(n//10, max_num)


if __name__ == '__main__':
	main()
