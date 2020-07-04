
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f: #sig可去掉開頭亂碼
		for line in f:
			lines.append(line.strip())  #strip為去掉換行符號
	return lines


def convert(lines): #convert為轉換功能
	new = []
	person = None #一開始預設沒有person
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:  #如果有person的話
			new.append(person + ': ' + line)
	return new


def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n') #\n為換行符號


def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)


main()  #執行function功能