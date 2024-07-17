library = [
    ("A001", "Harry Potter and the Cursed Child", "J. K. Rowling"),
    ("A002", "The Secret Seven", " Enid Blyton "),
    ("A004","Forrest Gump", "Winston Groom"),
    ("A007", "P. JACKSON", "ABC")
]
all_books = library
print("All Books:")
for book in all_books:
    print(book)
a=input("Do you want to add any book:")
if(a.lower()=="yes"):
    x=input("Enter the name of book:")
    y=input("Enter the author name:")
    z=input("Enter the unique code for novel:")
    new_book = (z,x,y)
    library.append(new_book)
    all_books = library
    print("All Books:")
    for book in all_books:
        print(book)
b=input("Do you want to remove any book:")
if(b.upper()=="YES"):
    print("Remove th book by:","\n","1. Serial Number","\n",
          "2.Book Title","\n","3.Author's Name")
    c=int(input("Enter your choice:"))
    if(c==1):
        d=input("Enter the serial number of book:")
        library=[book for book in library if book[0]!=d]
        all_books = library
        print("All Books:")
        for book in all_books:
            print(book)
    elif (c==2):
    elif(c==3):
    else:
        
'''
library.append(("A005", "The Hunger Games", "Suzanne Collins"))
library = [book for book in library if book[0]!= "A002" ]'''