# Use recursion to implement a countdown counter

def countdown(n):
    if n == 0:
        print("Done!")
        return

    else:
        print(n, "...")
        countdown(n-1)

countdown(100)