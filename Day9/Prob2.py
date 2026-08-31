# Tu ek event planner hai. Teen alag VIP guests hain ([1, 2, 3] unke badge numbers), aur tujhe unke stage pe baithne ke saare possible arrangements (orders) nikalne hain — kyunki client ko dekhna hai kaunsa order sabse acha lagta hai.

# Yeh subsets se different hai — is baar saare elements hamesha shamil honge, bas order badalta rahega.


def permutations(nums: list[int]) -> list[list[int]]:
    result = []
    
    def backtrack(path, used):
        
        if len(path) == len(nums):
            result.append(path[:])   
            return
        
        # Har element try karo poore array mein se
        for num in nums:
            if num in used:
                continue   # yeh already use ho chuka hai is path mein, skip
            
            # Choose: is num ko path mein daalo
            path.append(num)
            used.add(num)
            
            # Recurse: agle position ke liye try karo
            backtrack(path, used)
            
            # Un-choose (backtrack): wapas hatao taaki agla option try ho sake
            path.pop()
            used.remove(num)
    
    backtrack([], set())
    return result

li = [1, 2, 3]
print(permutations(li))
        
        