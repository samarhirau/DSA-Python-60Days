# Tu ek share bazaar (stock market) trader hai. Tere paas ek din ke andar, har ghante ka ek stock price hai. Tujhe sirf ek baar stock kharidna hai aur ek baar baad mein bechna hai (kharidne ke baad hi bech sakte ho, pehle nahi) — taaki tera profit maximum ho.

# Example:

# prices = [7, 1, 5, 3, 6, 4]

# Agar tu price 1 pe khareedta hai (din ka sabse sasta point uske aage) aur 6 pe bechta hai, profit = 5. Yahi maximum possible profit hai.

# Agar prices har ghante girti hi jaayen (jaise [7,6,4,3,1]), toh koi profit possible nahi — us case mein answer 0 return karna hai (mat becho, loss mat karo).

def max_profit(prices):
    max_profit = 0
    min_price = float('inf')
    
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    
    return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(max_profit(prices))  