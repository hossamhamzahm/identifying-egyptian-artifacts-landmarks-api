import time

def timer(f, txt="time"):
    def wrapper(*args):
        tic = time.time()
        val = f(*args)
        tac = time.time() - tic

        print(txt, tac, "s")
        return val
    return wrapper