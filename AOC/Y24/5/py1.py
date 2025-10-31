from aocd import get_data

rules = {}
messages = []

addRule = True

data = get_data(day=3, year=2024).split("\n")
for line in data:
	if line == '\n':
		addRule = False
		continue
	if addRule:
		rule = line.strip().split('|')
		if rule[0] in rules:
			rules[rule[0]].append(rule[1])
		else:
			rules[rule[0]] = [rule[1]]
	else:
		messages.append(line.strip().split(","))
		

def checkMessage(rule, message):
	print(message)
	for i in range(len(message) - 1):
		for j in range(i + 1, len(message)):
			if message[i] not in rule:
				return False
			if message[j] not in rule[message[i]]:
				return False
	return True


def checkAllMessages(rule, messages):
	res = 0
	for message in messages:
		if checkMessage(rule, message):
			# add the middle element of message to res
			res += int(message[len(message) // 2])
	return res
	
	
print(checkAllMessages(rules, messages))