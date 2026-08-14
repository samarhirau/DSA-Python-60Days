# Same coffee shop. Ab investor ek naya sawaal poochta hai: "kisi bhi continuous stretch mein, agar main sirf ek hi din ki chhutti allow karu (ek din ka sale hata sakte ho count se), tab sabse lambi 'no-zero' stretch kitni lambi ho sakti hai?" — matlab is baar tu ek zero ko ignore kar sakta hai window ke andar, do zero allowed nahi.

def longest_stretch_one_zero_allowed(sales: list[int]) -> int:
    left = 0
    right = 0 
    max_length = 0
    zero_count = 0
    
    for right in range(len(sales)):
        if sales[right] == 0:
            zero_count += 1
        
        while zero_count > 1:
            if sales[left] == 0:
                zero_count -= 1
            left += 1
        
        max_length = max(max_length, right - left + 1)

    return max_length
sales = [10, 20, 0, 15, 25, 30, 0, 5]
print(longest_stretch_one_zero_allowed(sales))