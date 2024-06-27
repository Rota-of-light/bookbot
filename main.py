def getting_book():
	with open("books/frankenstein.txt") as f:
		book_text = f.read()
	return book_text
def counting_words(book):
	words = book.split()
	number = len(words)
	return number

def main():
	print(getting_book())
	print("-----------------------------------------------------------")
	print(f"{counting_words(getting_book())} words found")
main()