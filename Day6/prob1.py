# Tu ek palindrome checker bana raha hai ek library app ke liye. Ek book ka title diya hai (string), tujhe check karna hai ki wo palindrome hai ya nahi (aage se piche padhne pe same lagta hai) — bina Python ke [::-1] trick use kiye, sirf do pointers se.

def is_palindrome(title: str) -> bool:
    left = 0 
    right = len(title) - 1
    
    while left < right:
        if title[left] != title[right]:
            return False
        left += 1 
        right -= 1
    
    return True

title = "hello"
print(is_palindrome(title))
            