library = [
    ("N12", "Harry Potter and the Cursed Child", "J. K. Rowling"),
    ("N13", "The Secret Seven", " Enid Blyton "),
    ("N14", "Forrest Gump", "Winston Groom")
]

all_books = library
print("All Books:")
for book in all_books:
    print(book)
i = input("Do you want to add any novel:")
if (i.lower()=="yes"):
    a=input("Enter the book name:")
    b=input("Enter the auther of book (write ABC in case you don't know auther):")
    c=input("Enter Book code:")
    new_book = (c,a,b)
    library.append(new_book)
    print("All Books:")
    for book in all_books:
        print(book)

y=input("Do you want to remove any novel:")
if(y.lower()=="yes"):
    a=input("Enter the serial code for novel:")
    library = [book for book in library if book[0] != a]
    all_books = library
    print("All Books:")
    for book in all_books:
        print(book)


