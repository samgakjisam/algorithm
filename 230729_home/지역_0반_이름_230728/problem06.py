def fibonacci(n):
    # pass를 지우고 작성해주세요.
    if n <= 0:
        return None
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) 

# 테스트 케이스
print(fibonacci(0))   # Output: None
print(fibonacci(1))   # Output: 1
print(fibonacci(5))   # Output: 5 (1, 1, 2, 3, 5)
print(fibonacci(10))  # Output: 55 (1, 1, 2, 3, 5, 8, 13, 21, 34, 55)