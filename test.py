#import re
#with open("entry.txt","r+", encoding="UTF-8") as vocab:
#    read = vocab.read()
#    read_split = read.split()
#    vocab.seek(0)
#    vocab.truncate()
#    for line in read_split:
#        line = line.strip().lower().replace("ã¥", "å").replace("ã¤", "ä").replace("ã¶", "ö").replace("�", "å")
#        line = (re.sub('[^A-Za-zåäöüéÅÄÖß]', '', line))
#        vocab.write(line + '\n)

import chardet

with open('swedish_vocabulary_database.txt', 'rb') as f:
    result = chardet.detect(f.read())

print(result['encoding'])