import tensorflow as tf
import time

def main():
    while True:
        print("Hello World")
        time.sleep(5)
        print(tf.__version__)
        
        
if __name__ == "__main__":
    print("start")
    main()

