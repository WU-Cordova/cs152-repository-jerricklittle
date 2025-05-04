def countdown(n):
    if n == 0:
        return 1
    else:
        return n + countdown(n-1)
    

def next_prime_after_double(n:int) -> int:
    def is_prime(num:int) -> bool:
        if num < 2:
            return False
        while int(num**.5) % n == 0:
            return False
        return True
    
def main():
    pass

if __name__ == '__main__':
    main()
    
