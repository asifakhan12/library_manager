import json
import os

# Load library from file (if exists)
def load_library():
    if os.path.exists("library.txt"):
        with open("library.txt", "r") as file:
            return json.load(file)
    return []

# Save library to file
def save_library(library):
    with open("library.txt", "w") as file:
        json.dump(library, file, indent=4)

# Add a book
def add_book(library):
    title = input("Enter title: ")
    author = input("Enter author: ")
    year = int(input("Enter publication year: "))
    genre = input("Enter genre: ")
    read_input = input("Have you read it? (yes/no): ").lower()
    read = True if read_input == "yes" else False

    book = {
        "Title": title,
        "Author": author,
        "Year": year,
        "Genre": genre,
        "Read": read
    }
    library.append(book)
    print("Book added!")

# Remove a book
def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["Title"].lower() == title.lower():
            library.remove(book)
            print("Book removed!")
            return
    print("Book not found.")

# Search for a book
def search_book(library):
    keyword = input("Enter title or author to search: ").lower()
    found = False
    for book in library:
        if keyword in book["Title"].lower() or keyword in book["Author"].lower():
            print_book(book)
            found = True
    if not found:
        print("No matching books found.")

# Display all books
def display_books(library):
    if not library:
        print("Library is empty.")
        return
    for book in library:
        print_book(book)

# Helper function to print book info
def print_book(book):
    read_status = "Read" if book["Read"] else "Unread"
    print(f"Title: {book['Title']}, Author: {book['Author']}, Year: {book['Year']}, Genre: {book['Genre']}, Status: {read_status}")

# Display statistics
def show_stats(library):
    total = len(library)
    read_count = sum(1 for book in library if book["Read"])
    if total == 0:
        print("Library is empty.")
        return
    percentage = (read_count / total) * 100
    print(f"Total books: {total}")
    print(f"Books read: {read_count} ({percentage:.2f}%)")

# Menu
def menu():
    library = load_library()
    while True:
        print("\nPersonal Library Manager")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            show_stats(library)
        elif choice == "6":
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the program
menu()
