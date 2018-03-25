def move_disk(src, dst):
    dst.append(src.pop())

# Move n-1 disks to temp tower
# Move top disk from src to dst
# Move n-1 disks back from temp to dst
def move_tower(n, src, dst, temp):
    if n <= 0:
        return

    move_tower(n-1, src, temp, dst)
    move_disk(src, dst)
    print src, dst, temp
    move_tower(n-1, temp, dst, src)

def tower_of_hanoi(n):
    a = [i for i in range(1, n+1, 1)]
    b = []
    c = []
    print 'Start:', a, b, c
    move_tower(n, a, b, c)
    print 'End: ', a, b, c

if __name__ == "__main__":
    n = int(input())
    tower_of_hanoi(n)
