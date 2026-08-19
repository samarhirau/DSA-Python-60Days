def longest_unique_substring(review: str) -> str:
    seen = set()        
    left = 0
    max_length = ""
    
    for right in range(len(review)):
        while review[right] in seen:
            seen.remove(review[left])
            left += 1
            
        seen.add(review[right])
        
        if right - left + 1 > len(max_length):
            max_length = review[left:right + 1]
        
    
    return max_length

print(longest_unique_substring(review="abcabcbb"))