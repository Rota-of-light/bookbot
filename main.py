def getting_book():
	with open("books/frankenstein.txt") as f:
		book_text = f.read()
	return book_text
def counting_words(book):
	words = book.split()
	number = len(words)
	return number

def counting_characters(book):
    chara = {}
    for letters in book:
        low_letters = letters.lower()
        if low_letters in chara:
            chara[low_letters] += 1
        else:
            chara[low_letters] = 1
    return chara
			
def sort_by_num(dict):
	return dict["num"]

def chara_dict_to_sorted_list(chara_dict):
	sorted_list = []
	for key in chara_dict:
		if key.isalpha() == True:
			sorted_list.append({"chara": key, "num": chara_dict[key]})
	sorted_list.sort(reverse=True, key=sort_by_num)
	return sorted_list

def main():
	first_time = True
	book_holder = getting_book()
	chara_counted = counting_characters(book_holder)
	sorted_chara_dict = chara_dict_to_sorted_list(chara_counted)
	print(book_holder)
	print(sorted_chara_dict)
	print("")
	print("")
	print("--------------------------------------------------------------------------------------")
	print("Starting fun facts and trivia!")
	print("--------------------------------------------------------------------------------------")
	print(f"Did you know? This classic novel is composed of {counting_words(book_holder)} words")
	print("--------------------------------------------------------------------------------------")
	print("")
	print("Ever wonder how many times each letter was used? No?... Here you go anyways!")
	for dicts in sorted_chara_dict:
		if first_time == True:
			print("")
			print(f"The letter that appeared most is '{dicts['chara']}' at a whopping {dicts['num']} times!")
			print("")
			print("And here are the runners-up:")
			first_time = False
		else:
			print(f" The letter '{dicts['chara']}' appeared {dicts['num']} times!")
	print("")
	print("")
	print("--------------------------------------------------------------------------------------")
	print("End of fun facts and trivia.")
	print("--------------------------------------------------------------------------------------")

main()