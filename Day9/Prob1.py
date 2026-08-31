# Tu maze-solver robot bana raha hai — try karo, dead-end mile toh undo karke doosra raasta try karo. Aaj ka pehla concrete problem: saare subsets nikalne hain ek array ke.a


def subsets(nums: list[int]) -> list[list[int]]:
    res = []

    def backtrack(start: int, path: list[int]):
        res.append(path)
        for i in range(start, len(nums)):
            backtrack(i + 1, path + [nums[i]])

    backtrack(0, [])
    return res

nums = [1, 2, 3]
print(subsets(nums))  