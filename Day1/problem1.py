# Socho tu ek railway platform par khada hai. Har minute ek train ka announcement hota hai jisme bताया jaata hai ki train kitni late hai (minutes mein), positive number ka matlab late, aur agar train time pe ya jaldi hai toh number 0 ya negative bhi ho sakta hai.

# Tujhe pata karna hai: kaunse consecutive announcements (ek continuous block) ka total delay sabse zyada tha — taaki tu unhe "worst stretch of the day" bol sake station master ko.

# Example:

# Delays = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# Yahaan best continuous stretch hai [4, -1, 2, 1] jiska sum = 6 hai — baaki kisi bhi continuous stretch ka sum isse zyada nahi.

def worst_stretch(arr):
    current_sum = arr[0]     
    max_sum = arr[0]          

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum

Delays = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(worst_stretch(Delays))   