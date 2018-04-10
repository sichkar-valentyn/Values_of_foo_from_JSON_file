# File: Values_of_foo_from_JSON_file.py
# Description: Finding values of key foo from JSON file
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
# 
# Reference to:
# [1] Valentyn N Sichkar. Finding values of key foo from JSON file // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/Values_of_foo_from_JSON_file (date of access: XX.XX.XXXX)


# Implementing the task
# Finding the values for all keys 'foo' from JSON file
sum = 0
n = ''
set_of_numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
with open('dataset_51_9.txt') as inf:
    for line in inf:
        line = line.strip()
        foo = line.find('foo')
        if foo >= 0:
            for i in range(foo + 6, len(line)):
                if line[i] in set_of_numbers:
                    n += line[i]
            sum += int(n)
        n = ''

print(sum)
