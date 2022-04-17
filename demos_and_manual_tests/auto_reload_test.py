import sys
from time import sleep

def main():
    while True:
        print("Hello World")
        sleep(30/60)
    
if __name__ == "__main__":
    print("Starting...")
    main()
else: 
    print(__name__)