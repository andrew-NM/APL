import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    
    def __exit__(self, a, b, c):
        end = time.time()
        print(f"Execution took {end - self.start} seconds")

with Timer():
    for i in range(11241141):
        pass