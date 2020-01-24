from sys import argv
import os
import numpy as np
from numpy.random import choice

VALID_COMMANDS = {'--help', '-h', '--make', 'm', '--clean', '-c', '--estimate', '-e'}
HELP = {'--help', '-h'}
CLEAN = {'--clean', '-c'}
MAKE = {'--make', '-m'}
ESTIMATE = {'--estimate', '-e'}
WORDS_IN_DICTIONARY = 370103

def printInstructions():
	print('This program creates a text file of randomly selected')
	print('words from the dictionary, which can then be used to')
	print('estimate how many english words you know.')
	print('\nCommands: ')
	print('--make <optional: sampleSize>')
	print('description: takes a random sample of words from the')
	print('dictionary and puts them in a file call sample.txt')
	print('by default, the sample size is 500. But it can be')
	print('changed using a number after the --make argument.')
	print('you should then edit the file and fill out a 1 for')
	print("each word you don't.  Separate the words and numbers")
	print('by a space.  Or if you prefer choose your own delimiter')
	print('(Just make sure to be consistent).')
	print('\n--estimate <optional: delimiter>')
	print('description: uses the filled out sample.txt file to estimate')
	print('how many words you know.  By default, it assumes that the')
	print('labels are separated from the words by a space.  But if you')
	print('chose to use a different delimiter, you can add the delimiter')
	print('as an argument.')
	print('\n--clean')
	print('description: --make will not overwrite sample.txt if it exists')
	print("if you want to remove it and trying 'rm sample.txt' is too bland")
	print("for your tastes, you can use --clean.  (it uses 'rm sample.txt'")
	print("under the hood so you don't have to!)")
	print('\nexample command: ')
	print('python howManyWords.py --make 150')

# the option for the dictionary exists for development purpose.  I wanted to be able
# to test this function with a smaller text file.
def make(num_words=500, dic='words_alpha.txt'):
	if not os.path.isfile('sample.txt'):
		print('creating sample.txt...')
		file = open(dic)
		words = np.array([w for w in file.read().split('\n') if len(w) > 0])
		file.close()
		selected_words = words[choice(len(words), num_words, replace=False)]
		file = open('sample.txt', 'w')
		for word in selected_words:
			file.write(f'{word}\n')
		file.close()
		print('sample.txt has been created')
	else:
		print('sample.txt has already been made')

def estimate(delim=' '):
	if os.path.isfile('sample.txt'):
		print('opening sample.txt.  If there are errors, double check how you have formatted sample.txt')
		file = open('sample.txt')
		lines = [line for line in file.read().split('\n') if len(line) > 0]
		file.close()
		total_words = float(len(lines))
		known_words = float(sum([int(line.split(delim)[1]) for line in lines]))
		ratio = known_words / total_words
		estimated_words = ratio * WORDS_IN_DICTIONARY
		print(f'total_words: {total_words}')
		print(f'known_words: {known_words}')
		print(f'ratio: {ratio}')
		print(f'estimate: {estimated_words}')
	else:
		print('you need to use --make first')

def clean():
	if os.path.isfile('sample.txt'):
		print('removing sample.txt...')
		os.remove('sample.txt')
		print('sample.txt has been removed')
	else:
		print('there were no files to remove')


if len(argv) < 2 or argv[1] in HELP:
	printInstructions()
elif len(argv) > 3 or argv[1] not in VALID_COMMANDS:
	print('use a valid argument.  for help use --help')
elif argv[1] in MAKE:
	if len(argv) == 3:
		n_words = int(argv[2])
		make(num_words=n_words)
	else:
		make()
elif argv[1] in ESTIMATE:
	if len(argv) == 3:
		delim = argv[2]
		estimate(delim=delim)
	else:
		estimate()
else:
	clean()