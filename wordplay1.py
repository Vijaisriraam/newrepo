fin=open('words.txt')
def word_search(name):
	count=0
	for line in fin:
		word=line.strip()
		if('e'in word):
			print(word)
			count=count+1
	print('total count is:',count)
word_search('words.txt')
