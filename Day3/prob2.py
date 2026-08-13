# Tu ek movie theatre ka manager hai. Ek din mein har show ke liye tickets bike (sold), ek array mein diya hai. Tujhe check karna hai — kya kisi bhi do consecutive shows (ek ke baad wala) mein total tickets ek given target ke barabar ho sakte hain?



def consecutive_pair_sum(tickets: list[int], target: int) -> bool:
    
    for i in range(len(tickets) - 1):
        if tickets[i] + tickets[i+1] == target:
            return True
    
    return False

tickets = [10, 20, 15, 25, 30]
target = 45
print(consecutive_pair_sum(tickets,target))