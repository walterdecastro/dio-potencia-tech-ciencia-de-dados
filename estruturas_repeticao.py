import os 
def draw(c):
    size = os.get_terminal_size().columns 
    for size in range(0, size): 
        print(c, end="")
