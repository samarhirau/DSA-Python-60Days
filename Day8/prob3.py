# Tu ek security system bana raha hai jo check karta hai ki koi passcode string mein sirf digits hain ya nahi (matlab har character 0-9 hona chahiye).  


def all_digits(s: str) -> bool:
    if len(s) == 0:
           return True

    if s[0] < "0" or s[0] > "9":
        return False

    return all_digits(s[1:])
        

print(all_digits("12345"))