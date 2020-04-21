def parse_input_file(file_path: str) -> list:
    output = []

    try:
        with open(file_path) as file_list:
            for line in file_list.readlines():
                if '\n' in line:
                    line = line.replace('\n', '')

                output.append(line)

    except FileNotFoundError:
        print('Input file not found: ', file_path)

    finally:
        return output


def main():
    input_file = '1030 Project 04 03 Files.txt'
    output_file = 'BadrChoubai 02 04 03 Output.txt'
    files_to_combine = parse_input_file(input_file)

    with open(output_file, 'w') as output_file:
        for file in files_to_combine:
            with open(file + '.txt', 'r') as content_file:
                output_file.write(content_file.read() + '\n')


if __name__ == "__main__":
    main()
