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


def fixMessage(rules, message):
	newMessage = []
	l = len(message)
	for j in range(l):
		for i in range(len(message)):
			if message[i] in rules:
				if all(x in rules[message[i]] for x in message if x != message[i]):
					newMessage.append(message[i])
					message.pop(i)
					break
	return newMessage


def checkAllMessages(rule, messages):
	res = 0
	for message in messages:
		if not checkMessage(rule, message):
			message = fixMessage(rules, message)
			res += int(message[len(message) // 2])
	return res


print(checkAllMessages(rules, messages))