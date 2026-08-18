# Tu ek teacher hai. Class ke students ke marks diye hain. Tujhe batana hai: kitne students ne average se zyada marks liye (pehle average nikal, phir count kar kitno ne usse zyada score kiya).


def above_average_count(marks: list[int]) -> int:
    avg = sum(marks) / len(marks)
    count = 0
    for mark in marks:
        if mark > avg:
            count += 1
        
    return count
        
    

marks = [40, 60, 80, 90, 30]
print(above_average_count(marks))