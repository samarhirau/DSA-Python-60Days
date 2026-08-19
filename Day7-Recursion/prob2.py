# Tu ek calculator app bana raha hai. Tujhe ek number ka factorial nikalna hai — recursion se (yeh bhi classic hai, sum_to_n jaisa hi simple structure).

def factorial(n: int) -> int:
    if n <= 1:
        return 1
    
    return factorial( n-1) * n

print(factorial(5))