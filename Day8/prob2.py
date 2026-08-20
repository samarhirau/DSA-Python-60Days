# Tu ek quality inspector hai ek factory mein. Products ki ek row hai (array of numbers). Tujhe check karna hai — kya poora array sorted (ascending) hai — is baar bhi recursion se, koi loop nahi.

def is_sorted(arr: list[int]) -> bool:
	if len(arr) <= 1:
		return True

	if arr[0] > arr[1]:
		return False

	return is_sorted(arr[1:])

print(is_sorted([1, 2, 3, 4, 5]))