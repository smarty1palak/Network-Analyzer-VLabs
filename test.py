with open('urls1.txt') as f:
    content = f.read().splitlines()
text_file = open("segmented1.txt", "w")
text_file1 = open("codepart.txt", "w")
for i in range(0,len(content)):
    seg = content[i].rpartition('/')
    text_file.write(seg[0])
    text_file.write("\n")
    text_file1.write('/'+ seg[2])
    text_file1.write("\n")

text_file.close()
text_file1.close()

