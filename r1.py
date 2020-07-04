def read_file(filename): 
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip()) #strip為去掉換行符號
    return lines

def convert(lines):  #convert為轉換功能
    new = []
    person = None #一開始預設沒有person
    for line in ines:
        if line=='Allen':
            person = 'Allen'
            continue
        elif line=='Tom':
            person = 'Tom'
            continue
        if person:   #如果person有值的話
            new.append(person + ':' + line)    
        return new

def write_file(filename, lines):
    with open(filename, 'w', encoding='utf-8-sig') as f:
        for line in lines:
            f.write(line + '\n') #\n為換行符號


