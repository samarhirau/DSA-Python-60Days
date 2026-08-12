# Tu ek library ka librarian hai. Ek shelf pe books hain jinke thickness (pages) diye hain array mein. Tujhe ek birthday gift box banani hai jisme sirf do books rakhni hain, aur tera goal hai — un do books ka total thickness ek target number ke bilkul barabar ho.


def two_book_gift(books: list[int], target: int) -> list[int]:
    
    for i in range(len(books)):
        find = target - books[i]
        if find in books[i+1:]:
            return [i, books.index(find)]
        
        


books = [2, 7, 11, 15]
target = 9
print(two_book_gift(books, target))  
