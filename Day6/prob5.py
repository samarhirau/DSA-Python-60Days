# Tu ek social media analyst hai. Ek post ke comments ka string diya hai (sirf letters). Tujhe pata karna hai: sabse lambi substring jisme koi bhi ek character zyada se zyada 2 baar aaye (3 baar ya usse zyada repeat nahi hona chahiye).


def longest_substring_max_2_repeats(comments: str) -> int:
    left = 0
    max_length = 0
    freq = {}

    for right in range(len(comments)):
        character = comments[right]

        freq[character] = freq.get(character, 0) + 1

        
        while freq[character] > 2:
            left_character = comments[left]
            freq[left_character] -= 1
            left += 1
            
        max_length = max(max_length, right - left + 1)

    return max_length


comments = "eceba"

print(longest_substring_max_2_repeats(comments))

