# File Objects

print("========================")
print()
###############################################################################



"""
open( 'directory/file.extension' , 'r|w|a|r+|w+|a+' )
r = read
w = write
a = append
r+ = read + write
w+ = 
a+ = 

NOTE: When read() reaches EOF, it returns an empty string.
"""
# This is NOT a good way to handle files.
f1 = open('test.txt', 'r')
print(f1.name)
print(f1.mode)
f1.mode = 'w'
print("file access mode has been changed to:")
print(f1.mode)
f1.close()


# Instead, use a CONTEXT MANAGER.
print()
with open('test.txt', 'r') as f2:
    print(f2.name)
    print(f2.mode)
    f2.mode = 'w'
    print("file access mode has been changed to:")
    print(f2.mode)
    print(f2.closed)

print(f2.closed)


# Read line-by-line METHOD #1
print()
with open('test.txt', 'r') as f3:
    print(f3.readline(), end='')
    print(f3.readline(), end='')
    print(f3.readline(), end='')


# Read line-by-line METHOD #2
print()
with open('test.txt', 'r') as f4:
    # readlines() => list[str]
    for line in f4.readlines():
        print(line, end='')


# Read line-by-line METHOD #3
print()
with open('test.txt', 'r') as f5:
    for line in f5:
        print(line, end='')


# Read by char count
print()
with open('test.txt', 'r') as f6:
    f6_contents = f6.read(16)
    print(f6_contents, end='')
    print('___________')
    f6_contents = f6.read(153)
    print(f6_contents, end='')
    print('___________')
    f6_contents = f6.read(1000)  # EOF reached way before 1000 characters
    print(f6_contents, end='')


# Read by char count (MORE CONTROL)
print()
with open('test.txt', 'r') as f7:
    size_to_read = 10

    f7_contents = f7.read(size_to_read)
    while len(f7_contents):
        print(f7_contents, end='_')
        f7_contents = f7.read(size_to_read)
        






###############################################################################
print("========================")