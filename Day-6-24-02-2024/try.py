try:
    n = int(input())
    k = n//2
except ZeroDivisionError:
    print("0 division error")
except Exception as e:
    print(e)
else:
    print(c)
finally:
    print("Hello")
