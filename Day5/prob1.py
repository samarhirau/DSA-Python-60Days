# Tu ek restaurant reviewer hai. Tere paas ek string hai jisme customer reviews ke words ki sequence hai (simplify karke socho — ek string of characters). Tujhe pata karna hai: sabse lambi substring kitni lambi ho sakti hai jisme koi bhi character repeat na ho (matlab sab characters unique hon us window ke andar).

def longest_unique_substring(review: str) -> int:
    seen = set()
    left = 0
    max_length = 0
    
    for right in range(len(review)):
        while review[right] in seen:
            seen.remove(review[left])
            left += 1
        
        seen.add(review[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length


review = "abcabcbb"
print(longest_unique_substring(review))