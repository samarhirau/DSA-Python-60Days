# Tu ek mausam vibhag (weather department) ka analyst hai. Tere paas last n dino ka temperature array hai. Log poochte hain: "kal se aaj tak temperature kitna gira/badha?" — nahi, aise nahi. Actual kaam yeh hai: har din ke liye batao — kitne din baad temperature usse zyada hoga (warmer day). Agar aisa din kabhi nahi aata (baaki sab dino mein bhi thanda hi rehta hai), toh 0 bolna hai (na ki index ya -1, is baar rule change hai — "kitne days wait karne padenge").



# Pichhli baar tune stack mein values store kiye the. Is baar stack mein indices store kar (values nahi) — kyunki jab tujhe answer nikalna hai ("kitne din baad"), tujhe do indices ka farak chahiye hoga (current_index - stored_index), sirf value nahi. Baaki logic bilkul same hai — right ya left se chalna, decide kar konse direction se chalna easier hoga is baar (hint: is baar left-to-right bhi chal sakta hai, kyunki humein "future mein kab" chahiye, past nahi).
def days_until_warmer(temps: list[int]) -> list[int]:
    n = len(temps)
    answer = [0] * n 
    stack = []  

    for current_index in range(n):
        while stack and temps[current_index] > temps[stack[-1]]:
            previous_index = stack.pop()  
            answer[previous_index] = current_index - previous_index  
        stack.append(current_index)  

    return answer
    

temps = [73, 74, 75, 71, 69, 72, 76, 73]
print(days_until_warmer(temps))  