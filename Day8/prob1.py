# Tu ek speech therapist app bana raha hai jo kids ko words backwards bolna sikhata hai. Tujhe ek string reverse karni hai — sirf recursion se (koi [::-1], koi loop nahi).

def reverse_string(s: str) -> str:
    if len(s) <= 1:
        return s
    
    return s[-1] + reverse_string(s[:-1])
    
print(reverse_string("hello"))