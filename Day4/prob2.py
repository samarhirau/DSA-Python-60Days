# Same coffee shop, ab thoda different sawaal. Investor ab bola: "mujhe woh sabse LAMBA continuous stretch of days chahiye jinme koi bhi single day ka sale ₹0 na ho" (matlab window mein koi bhi din ₹0 sale wala include nahi ho sakta — agar aaya, toh window wahin tootega).


def longest_stretch_no_zero(sales: list[int]) -> int:
    left = 0
    right = 0
    
    max_length = 0
    for right in range(len(sales)):
        if sales[right] == 0:
            left = right + 1  
        else:
            max_length = max(max_length, right - left + 1)
    
    return max_length

sales = [10, 20, 0, 15, 25, 30, 0, 5]
print(longest_stretch_no_zero(sales))