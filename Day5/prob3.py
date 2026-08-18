# Tu ek cinema hall ka manager hai. Ek show ke tickets bike hain, unke prices ek array mein hain. Tujhe batana hai: sabse zyada aur sabse kam price wale ticket ka farak (difference) kitna hai.




def price_range(prices: list[int]) -> int:
    min_val = float('inf')
    max_val = float('-inf')
    
    for price in prices:
        if price < min_val:
            min_val = price
        if price > max_val:
            max_val = price
    return max_val - min_val


prices = [45, 60, 30, 90, 55]
print(price_range(prices))