input_file = 'ZipAndCity.txt'

zip_code = {}

with open(input_file, 'r') as zip_codes:
    for line in zip_codes.readlines():
        z, c = (line.replace('\n', '').rstrip().split(','))

        if z in zip_code:
            zip_code[z] = c
        else:
            zip_code[z] = c


print(zip_code)
