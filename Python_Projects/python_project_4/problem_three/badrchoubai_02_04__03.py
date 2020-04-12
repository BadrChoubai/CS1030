def get_input_files(file_path: str) -> list:
    output = []

    try:
        with open(file_path) as file_list:
            for file_name in file_list.readlines():
                output.append(file_name.replace('\n', '.txt'))
    except FileNotFoundError:
        print('Input file not found: ', file_path)

    return output


def main():
    input_file = '1030 Project 04 03 Files.txt'
    output_file = 'BadrChoubai 02 04 03 Output.txt'
    files_to_combine = get_input_files(input_file)

    with open(output_file, 'w') as output:
        for file in files_to_combine:
            with open(file, 'r') as content_file:
                output.write(content_file.read() + '\n')


if __name__ == "__main__":
    main()
