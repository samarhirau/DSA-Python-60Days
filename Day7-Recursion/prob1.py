# Tu ek matryoshka doll maker hai. Har doll ke andar do chhoti dolls hoti hain (ek nahi, do — thoda alag concept). Tujhe Fibonacci sequence ka n-wa number nikalna hai — jahan har number apne pichhle do numbers ka sum hota hai.

def fibonacci(n: int) -> int:
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)
   

print(fibonacci(6))