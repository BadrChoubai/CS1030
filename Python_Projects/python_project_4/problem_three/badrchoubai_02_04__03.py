from contextlib import ExitStack
# ExitStack Documentation :: https://docs.python.org/3/library/contextlib.html#contextlib.ExitStack
# ExitStack Blog Post :: https://www.rath.org/on-the-beauty-of-pythons-exitstack.html


def combine_files(files_to_combine: list, output_file: str):
    '''combine_files
    This function takes the list of files we'd like to write to our output file
    '''
    output_file = open(output_file, mode='w')

    for file in files_to_combine:
        output_file.write(file.read() + '\n')
        file.close()

    output_file.close()


def open_files(file_list: list, mode: str) -> list:
    '''Utility function that implements `contextstack.ExitStack`
    to handle the opening of multiple files
    '''
    with ExitStack() as stack:
        for i, file in enumerate(file_list):
            file_list[i] = stack.enter_context(open(file, mode))
        stack.pop_all()
        return file_list


def main():
    input_file = '1030 Project 04 03 Files.txt'
    output_file = 'BadrChoubai 02 04 03 Output.txt'
    file_list = []

    input_file = open(input_file, mode='r')

    for line in input_file.readlines():
        file_list.append(line.replace('\n', '.txt'))

    combine_files(open_files(file_list, mode='r'), output_file)


if __name__ == "__main__":
    try:
        main()
    except FileNotFoundError as error:
        print(error)
