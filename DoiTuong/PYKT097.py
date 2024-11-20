import re

s = ""
while True:
    try:
        s += input().strip().lower()
        if s[-1] not in '.!?':
            s += ".\n"
        else:
            s += '\n'
    except:
        break
s = re.sub(r'\s+', ' ', s)
s = s.strip()
sentences = re.split(r'([.!?])', s)  

for i in range(0, len(sentences) - 1, 2):
    sentence = sentences[i].strip()
    if sentence:  # Bỏ qua chuỗi rỗng
        print(sentence[0].capitalize() + sentence[1:] + sentences[i + 1])