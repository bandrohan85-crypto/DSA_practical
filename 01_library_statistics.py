library_data = {
    "M001": ["Book A", "Book B"],
    "M002": ["Book C"],
    "M003": [],
    "M004": ["Book A", "Book A"],
    "M005": [],
    "M006": ["Book B", "Book D"]

}
total_members = len(library_data)
total_books_borrowed = sum(len(books) for books in library_data.values())
average = total_books_borrowed / total_members
print("Average books borrowed:", average)
all_books = []
for books in library_data.values():
    all_books.extend(books)

book_counts = {}
for book in all_books:
    if book in book_counts:
        book_counts[book] += 1
    else:
        book_counts[book] = 1

most_borrowed = max(book_counts, key=book_counts.get)
print("Most borrowed book:", most_borrowed)
least_borrowed = min(book_counts, key=book_counts.get)
print("Least borrowed book:", least_borrowed)
zero_borrowers = sum(1 for books in library_data.values() if len(books) == 0)
print("Members with 0 borrowings:", zero_borrowers)
print("Most frequently borrowed book (mode):", most_borrowed)
