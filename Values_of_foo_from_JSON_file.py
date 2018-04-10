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
