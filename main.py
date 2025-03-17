# the follwing function will pull the text from a file and convert it to a string
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
def main():
    # Call get_book_text with the path to your file
    book_text = get_book_text("books/frankenstein.txt")
    print(book_text)
#main
main()
