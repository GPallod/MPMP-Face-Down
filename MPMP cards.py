
# Hey Matt! just run this program to get a feel.


# return all numbers in binary. gets rid of the initial '0b'. and makes all the numbers the given length. 
# because we want '0001' and not '1'
def binary(n, num_digits):
	ans = bin(n)[2:] # get the binary nums, without the initial 0b
	num_zeros = num_digits - len(ans) # to make them 'num_digits' digits long
	return ('0' * num_zeros) + ans


# returns list of all possible combinations, except all face down.
def give_lst(num_of_cards):
	num1 = (2 ** num_of_cards)
	lst = []
	for i in range(1, num1):
		lst.append(binary(i, num_of_cards))
	return lst


'''
this function return True only if the given answer is the most efficient.
basically, if you apply the move and one possition is all Face Down, then it a correct move
and if only one move doesn't result in a '0000' in the list, then the reply becomes False and immediately returns it
So, only if the function is most efficient, i.e., it solves one position at each move, then this function will return True.
'''
def check_ans(num_cards, key):
	lst = give_lst(num_cards)
	correct = '0' * num_cards
	for func in key:
		lst = func(lst)
		if correct in lst:
			lst.remove(correct)
			reply = True
		else:
			reply =  False
			exit
	return reply


'''
This function return a list of all possibles moves. like, for 3 moves, it will return a list of functions 
which will flip the 0th, 1st, and 4th cards. and for 4 cards, [0, 1, 2, 3]
'''
def find_options(num_cards):
	options = []
	lst = give_lst(num_cards)
	for i in range(num_cards):
		def func(lst = lst, i = i):
			ans_lst = []
			for position in lst:
				if position[i] == '1':
					result = position[:i] + '0' + position[i + 1:]
				else:
					result = position[:i] + '1' + position[i + 1:]
				ans_lst.append(result)
			return ans_lst
		options.append(func)
	return options


'''
This function returns the most efficient list of moves to be done to complete the Face Down puzzle, given the number of moves.
basically, it will try every move from the find_options functions. for 3 cards, options = [0, 1, 2]
so, if flipping card 0 doesn't result one possition to get all face down ('000'), then it will just ignore it for now
then lets say flipping card 1 results in one possition to get all face down, then it is a correct move. so it will append this move 1, to the ans_lst
and we will return ans_lst at the end
'''
def find_ans(num_cards):
	ans_lst = []
	options = find_options(num_cards)
	lst = give_lst(num_cards)
	correct = '0' * num_cards
	for n in range(len(lst)):
		for i in options:
			if correct in i(lst):
				lst = i(lst)
				lst.remove(correct)
				ans_lst.append(i)
	return ans_lst


'''
the last 2 functions are made to give a result for humans to read.
this find_options_num is very similar to find_options functions, but it returns a dictionary. 
In each key - value pair, key is the card number which will be flipped, using the function in this value.
for example, if the key is 2, then the function in the value will flip the 2nd card (in computers. in humans it will flip the 3rd card)
This dictionary is useful for the find_ans_num
'''
def find_options_num(num_cards):
	options = {}
	lst = give_lst(num_cards)
	count = 0
	for i in range(num_cards):
		def func(lst = lst, i = i):
			ans_lst = []
			for position in lst:
				if position[i] == '1':
					result = position[:i] + '0' + position[i + 1:]
				else:
					result = position[:i] + '1' + position[i + 1:]
				ans_lst.append(result)
			return ans_lst
		options.update({count : func})
		count += 1
	return options


'''
if you want to read the solution, in the human language of Arabic numerals, then you have to use the find_ans_num function
here, it uses the dictionary from the find_options_num
just like the find_ans function, this function finds the correct move at this time.
instead of appending the function itself to ans_lst. this function appends the key of the function in the find_options_num dictionary.
and the key is the card number which it is flipping.
hence, you get the correct move list
'''
def find_ans_num(num_cards):
	ans_lst = []
	options = find_options_num(num_cards)
	lst = give_lst(num_cards)
	correct = '0' * num_cards
	for n in range(len(lst)):
		for count, i in options.items():
			if correct in i(lst):
				lst = i(lst)
				lst.remove(correct)
				ans_lst.append(count)
				count += 1
	return ans_lst

# Note : if you want to check_ans, then you have to use the find_ans function, as it returns a list of functions
# only for human legibility, you can use the find_ans_num function.

for n in range(10):
	print(
	'the number of cards are = ' + str(n), '\n',
	'the answer key is = ' + str(find_ans_num(n)), '\n')

print('and the answer is ... ' + str(check_ans(8, find_ans(8))) + '!')