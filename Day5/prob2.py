
# Tu ek security guard hai ek building ke entrance pe. Log ek queue mein aa rahe hain (unke ID cards ke numbers ek array mein diye hain, order mein). Tujhe check karna hai: kya kisi bhi 2 consecutive logon ke IDs same hain (matlab koi aadmi apna ID card duplicate use kar raha hai back-to-back)?


def has_adjacent_duplicate(ids: list[int]) -> bool:
    current = ids[0]
    for i in range(1,len(ids)):
        if current == ids[i]:
            return True
        else:
            current = ids[i]
    
    return False

ids = [101, 102, 102, 103, 104]
print(has_adjacent_duplicate(ids))