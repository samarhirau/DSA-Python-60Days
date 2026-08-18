# Tu ek fruit seller hai. Ek basket mein fruits hain (unke weights ek array mein diye hain, already sorted ascending order mein). Ek customer bolta hai: "mujhe do fruits chahiye jinka total weight kisi bhi 'limit' se zyada na ho, lekin jitna zyada ho sake utna ho" — matlab do fruits ka max possible sum jo limit se zyada na ho.


def best_pair_under_limit(weights: list[int], limit: int) -> int:
    max_limit = 0
    left = 0
    right = len(weights) - 1
    
    while left < right:             
        current_sum = weights[left] + weights[right]
        
        if current_sum <= limit:
            max_limit = current_sum
            left += 1
            
        else:
            right -= 1
            
    
    return max_limit

weights = [1, 3, 4, 6, 8]
limit = 10
print(best_pair_under_limit(weights, limit))