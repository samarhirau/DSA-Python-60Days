# Tu ek event manager hai. Ek concert mein log queue mein khade hain entry ke liye, aur tere paas unki heights (cm mein) ka array hai, entry order mein. Security team ne bola: "har guard ko sirf apne right side dekhna hai — batao, sabse pehla taller (ya equal) person kaun milega uske right mein." Agar koi taller nahi milta right mein, toh us guard ke liye answer -1 hoga.

# Hint: Right se left chal — aur ek stack use kar jisme tu "abhi tak dekhe gaye candidates" rakhta hai. Jab bhi kisi naye element pe pahunche, stack ke top wale ko check kar — agar wo chhota hai current element se, toh wo kabhi kisi ke liye "next taller" nahi ban sakta (discard kar de, pop kar de stack se). Jo bacha stack mein top pe, wahi tera answer hai.

def next_taller_or_equal(heights: list[int]) -> list[int]:
    arr = []
    i = 0
    for num in reversed(heights):
        while arr and arr[-1] < num:
            arr.pop()
        if not arr:
            heights[len(heights) - 1 - i] = -1
        else:
            heights[len(heights) - 1 - i] = arr[-1]
        arr.append(num)
        i += 1
    return heights

heights = [4, 2, 1, 5, 3]
result = next_taller_or_equal(heights)
print(result)  