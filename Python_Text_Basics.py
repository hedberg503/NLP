# dependencies:
#   - pip=22.0.4
#   - spacy=3.7.2
#   - numpy=1.26.1
#   - keras=2.14.0
#   - matplotlib=3.8.0
#   - pandas=2.1.1
#   - nltk=3.8.1
#   - scikit-learn=1.3.2

# from datetime import datetime
import os

print(f' {os.getcwd()} is the current working directory')

# Method 1
f = open('testfile.txt', 'w')
# Truncate file to zero length or create text file for writing.
# The stream is positioned at the beginning of the file.
f.write("Hello World")
f.close()

f = open('testfile.txt', 'r')
# Open text file for reading.
# The stream is positioned at the beginning of the file.
# This is the default
print(f'The file contents are: {f.read()}')
f.close()

# Method 2
with open("testfile.txt", "a+") as f:
    f.write("\nNew line!")
    f.seek(0)
    print(f'The file contents are: {f.read()}')
    # file closed automatically

with open("testfile.txt") as f:
    mylines = f.readlines()
    for ind, line in enumerate(mylines):
        print(f'Line {ind} of file: {line}')
