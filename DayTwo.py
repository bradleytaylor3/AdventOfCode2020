file = open('DayTwoInput', 'r')
rules = []
password = []
goodPasswords = 0
badPasswords = 0

for line in file:
    rawRules = line.split(':')[0]
    count = rawRules.split()[0]
    letter = rawRules.split()[1]
    rules.append([count, letter])
    password.append(line.split(':')[1].strip('\n'))

for rule, p in zip(rules, password):
    occurrences = p.count(rule[1])
    lowerValue = int(rule[0].split('-')[0])
    higherValue = int(rule[0].split('-')[1])
    if occurrences < lowerValue or occurrences > higherValue:
        badPasswords += 1
    else:
        goodPasswords += 1

print(goodPasswords, badPasswords)
