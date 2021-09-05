import os, re
os.chdir(r'/Data')

f = open('youtube.txt', 'r', encoding='utf8')
youtube = f.read()

result = re.findall(r'((https?://)?(www.?)?youtu.?be/([a-zA-Z0-9-]+))', youtube)
result

f.close()

# ------------

Line = open('monica.txt', 'r', encoding='utf=8')
monica = ''
for i in Line:
    monica += i + '\n'

monica[:100]

f = open('monica.txt', 'w', encoding='utf8')
f.write(monica)

f.close()