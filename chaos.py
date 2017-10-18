# file: chaos.py
# A simple program illustrating chaotic behavior.

def main():
    print("this program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    y = eval(input("how many times you want to loop?"))
    for i in range(y):
        x = 3.9 * x * (1 - x)
        print(i, ":" ,x)

main()
