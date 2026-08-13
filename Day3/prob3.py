# Tu ek school ka teacher hai. Class mein students ek row mein baithe hain, aur tere paas unke marks ka array hai. Tu ek quick oral quiz lena chahta hai, aur pooch raha hai: kisi bhi single student ke marks kitne hain jo sabse zyada baar repeat hue hain poori class mein (matlab mode — sabse frequent value)?


def most_common_mark(marks: list[int]) -> int:
    freq = {}
    for mark in marks:
        freq[mark] = freq.get(mark, 0) + 1
    
    
    max_value = max(freq.values())
    for mark, count in freq.items():
        if count == max_value:
            return mark

marks = [85, 90, 85, 70, 90, 85, 60]
print(most_common_mark(marks))