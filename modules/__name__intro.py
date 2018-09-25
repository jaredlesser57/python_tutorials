# Every python file has __name__ 


def say_hi():
    print(f"Hi, my __name__ is {__name__}")

# say_hi() # will be __main__ because existing file is main file, else import, expect __<file_name>__

if __name__ == "__main__": # will ONLY run if file is MAIN
    say_hi() 