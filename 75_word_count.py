# Exceptions
# Working with Multiple Files


from pathlib import Path


def count_words(path):
    """ Đếm gần đúng số lượng từ trong 1 file"""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        # đếm gần đúng số lượng từ trong một file
        words = contents.split()
        num_words = len(words)
        print(f" The file {path} has about {num_words} words. ")


'''Main'''
path = Path('alice.txt')
count_words(path)
