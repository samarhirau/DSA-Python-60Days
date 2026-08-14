# Tu wahi coffee shop owner hai. Ab thoda twist: kal humne fixed 3-day window dekha tha. Aaj tera investor bola hai: "mujhe woh sabse chhota continuous stretch of days chahiye jinka total sale kam se kam ₹100 ho jaaye" — matlab window size fixed nahi, jitna kam din mein target reach ho jaaye utna better.


def min_days_to_target(sales: list[int], target: int) -> int:
    left = 0
    right = 0
    current_sum = 0
    min_length = float('inf') 
    
    for right in range(len(sales)):
        current_sum += sales[right]
        
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= sales[left]
            left += 1
    
    return min_length if min_length != float('inf') else 0


sales = [10, 20, 30, 15, 25]
target = 60
print(min_days_to_target(sales, target))  