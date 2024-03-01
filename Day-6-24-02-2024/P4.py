#check palindrome and prime or not
class Total:
    def __init__(self, n, s):
        self.n = n
        self.s = s

    def is_prime(self):
        if self.n <= 1:
            print("No")
            return
        for i in range(2, int(self.n**0.5) + 1):
            if self.n % i == 0:
                print("No")
                return
        print("Yes")

    def is_palindrome(self):
        if self.s == self.s[::-1]:
            print("Yes")
        else:
            print("No")


ob1 = Total(12, "SaS")
ob1.is_prime()
ob2 = Total(14, "Hello")
ob2.is_palindrome()
ob3 = Total(13, "SaS")
ob3.is_prime()
ob3.is_palindrome()
