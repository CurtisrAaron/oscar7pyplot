import csv

file = open("data.txt","r")
f = open("csvData.csv","w", newline = '')

csvfile = csv.writer(f)


time = "__:__:__"
frame = 0

last_pos = file.tell()

if file.readline()[0:2] == 'hi':
    file.seek(last_pos)
    for line in file:
        line = str(frame) + ' ' + str(frame) + ' ' + line
        line = line.replace(' ',',')
        line = line.replace(',\n','')
        line.partition
        line = line.split(",")
        if line[14] == None:
            line = None
        print(line)
        csvfile.writerow(line)
        frame += 1
else:
    file.seek(last_pos)
    for line in file:
        print(line)
        print(line.find(':'))
        pos = line.find(':')
        if(pos > 0):
            time = line[(pos-2):(pos+6)]
            print(time)
        else:
            line = line[line.find('hi'):]
            line = str(frame) + ' ' + time + ' ' + line
            line = line.replace(' ',',')
            line = line.replace('\n','')
            line = line.split(',')
            print(line)
            csvfile.writerow(line)
            frame = frame + 1




f.close()
file.close()
