library = {}

def add_book():
    """
    Prompts the user to enter the title, genre, and price of a book separated by vertical bars.
    Adds the book to the library dictionary with the title as the key and the genre and price as the value.
    Prints a message indicating that the book has been added.
    Returns True to indicate that the book was successfully added.
    """

    # your code here
    add=input('Enter the title, genre, and price of the book (separated by |):')
    title,genre,price=add.split('|')#str->list
    price=float(price)#str->float
    print('Added',title,'to the library.')
    library[title]=(genre,price)#加入dictionary
    return True



def remove_book():
    """
    Prompts the user to enter the title of a book to remove.
    Removes the book from the library if it is found and prints a message indicating that the book has been removed.
    If the book is not found, prints an error message and returns False.
    Returns True if the book is successfully removed.
    """
    # your code here
    r_book=input('Enter the title of the book to remove:')
    if r_book not in library.keys():#當要移除的書根本不再dictionary裡面
        print('Error: %s not found in the library.\n'%(r_book))
    else:
        print('Remove %s from library.\n'%(r_book))
        del library[r_book]#有的話則直接移除
        return True



def get_book_info():
    """
    Prompts the user to enter the title of a book to get information about.
    Prints the title, genre, and price of the book if it is found in the library.
    If the book is not found, prints an error message.
    """

    # your code here
    enter=input("Enter the title of the book:")
    if enter not in library.keys():#當那本書根本不再dictionary裡面時
        print("Error: %s not found in the library."%(enter))

    else:#有的話則分別print出title genre price
        print('\nTitle: ',enter)
        print('Genre: ',library[enter][0])
        print('Price: ',library[enter][1])
    return True


def list_books():
    """
    Lists all books in the library in alphabetical order by title.
    If the library is empty, prints a message indicating that it is empty and returns False.
    Returns True if there are books in the library.
    """
    if not library:
        print("\nThe library is empty.\n")
        return False
    print()
    for title, (genre, price) in sorted(library.items()):
        print("%s (%s, $%.2f)" % (title, genre, price))
    print()
    return True

def list_books_by_genre():
    """
    Prompts the user to enter a genre to search for.
    Lists all books in the library that match the specified genre in alphabetical order by title.
    If no books are found in the specified genre, prints an error message and returns False.
    Returns True if at least one book is found in the specified genre.
    """
    
    # your code here
    genre_book=input('Enter the genre to search for :')
    genre_all=[]
    for(gen,pri)in library.values():
        if gen not in genre_all:
            genre_all.append(gen)
    if genre_book not in genre_all:        
        print('\nError: No books found in %s genre.\n'%(genre_book))
    else:
        gen_search={}
        for title,(gen,pri) in library.items():
            if gen==genre_book:
                gen_search[title]=(gen,pri)
        for title,(gen,pri) in sorted (gen_search.items()):#for 迴圈要將書本照順序排好
            print('%s %s ($%.2f)'%(title,gen,pri))
        print()
    return True






while True:
    print("Menu:\n1. Add a book\n2. Remove a book\n3. Get book information\n4. List all books\n5. List books by genre\n6. Quit")
    choice = input("\nEnter your choice (1-6): ")
    if choice == "1":
        add_book_return = add_book()
        if add_book_return:
            list_books()
    elif choice == "2":
        remove_book_return = remove_book()
        if remove_book_return:
            list_books()
    elif choice == "3":
        get_book_info()
    elif choice == "4":
        list_books()
    elif choice == "5":
        list_books_by_genre()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

print("Goodbye!")

