file = open('DayTwoInput', 'r')
rules = []
passwords = []
goodPasswords = 0
badPasswords = 0

for line in file:
    rawRules = line.split(':')[0]
    count = rawRules.split()[0]
    letter = rawRules.split()[1]
    rules.append([count, letter])
    passwords.append(line.split(':')[1].strip('\n'))

for rule, p in zip(rules, passwords):
    password = p.strip()
    firstPosition = int(rule[0].split('-')[0]) - 1
    secondPosition = int(rule[0].split('-')[1]) - 1
    characterCheck = rule[1].strip()
    onePosition = False
    if password[firstPosition] == characterCheck:
        onePosition = True
    else:
        onePosition = False

    if onePosition:
        if password[secondPosition] == characterCheck:
            onePosition = False
    else:
        if password[secondPosition] == characterCheck:
            onePosition = True

    if onePosition:
        goodPasswords += 1

print(goodPasswords)