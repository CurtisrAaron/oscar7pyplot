import csv

file = open("data.txt","r")
f = open("csvData.csv","w", newline = '')

csvfile = csv.writer(f)


time = "__:__:__"
frame = 0
for line in file:
    line = line.partition('$')[0]
    if line[0] != ' ':
        time = line[0:8]
    else:
        prev = line[0]
        i = 0
        for c in line:
            if (c == line[i+1]) & (c == ' '):
                line = line[0:i] + line[i+1:]
            else:
                prev = c
                i = i + 1
            if i + 1 == len(line):
                break
        line = str(frame) + ' ' + time + line
        line = line.replace(' ',',')
        line = line.replace(',\n','')
        line.partition
        line = line.split(",")
        print(line)
        csvfile.writerow(line)
        frame = frame + 1




f.close()
file.close()