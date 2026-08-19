# Tu ek gaming app bana raha hai jisme players ek array of numbers dekhte hain aur unhe container banana hai — do "walls" choose karke (array ke indices se), jinki height array ki values hain, taaki beech mein jitna paani (water) store ho sake utna zyada ho



def max_water(heights: list[int]) -> int:
    left = 0 
    right = len(heights) - 1 
    max_area = 0
    while left < right:
        current_area = min(heights[left], heights[right]) * (right - left)
        max_area = max(max_area, current_area)
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_area
        
heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(max_water(heights))