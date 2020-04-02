"""
1. Open a file named 'IODemo.txt'
2. Read the file line by line
3. Lines that begin with '#' are ignored; the other are written to the output file, IODemoSquished.txt
4. Count how many lines are kept and how many are ignored
5. Print the value of the two counts and the total
"""
input_file = 'IODemo.txt'
output_file = 'IODemoSquished.txt'

with open(input_file) as input_file:
    lines = input_file.readlines()

lines_kept = 0
lines_ignored = 0

with open(output_file, 'w') as output_file:
    for line in lines:
        if line.startswith('#'):
            lines_ignored += 1
        else:
            lines_kept += 1
            output_file.write(line)

print(
    f'Lines Kept: {lines_kept} :: Lines Ignored: {lines_ignored} \nLines Total :: {lines_kept+lines_ignored}')
