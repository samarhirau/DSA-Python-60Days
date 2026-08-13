# Tu ek coffee shop ka owner hai. Har din ke sales (₹ mein) ek array mein diye hain. Tujhe janna hai: kisi bhi 3 consecutive dino ka average sale sabse zyada kab tha (matlab konsa 3-day window sabse profitable tha)?


def best_3day_avg(sales: list[int]) -> float:
    n = len(sales)
    if n < 3:
        return 0
    
    max_avg = 0
    best_start_index = 0
    
    for i in range(n - 2):
        current_avg = (sales[i] + sales[i+1] + sales[i+2]) / 3
        if current_avg > max_avg:
            max_avg = current_avg
            best_start_index = i
    
    return max_avg

sales = [100, 200, 300, 400, 500]
print(best_3day_avg(sales))
