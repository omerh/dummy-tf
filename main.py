import tenserflow as tf
import time

def main():
    while True:
        print("Hello World")
        time.sleep(5)
        print(tf.__version__)
        
        
if __name__ == "main":
    main()

