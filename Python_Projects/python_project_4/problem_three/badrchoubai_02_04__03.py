#!/usr/bin/env python3

from contextlib import ExitStack
# ExitStack Documentation :: https://docs.python.org/3/library/contextlib.html#contextlib.ExitStack
# ExitStack Blog Post :: https://www.rath.org/on-the-beauty-of-pythons-exitstack.html


def open_files(file_list, mode):
    '''Utility function that implements `contextstack.ExitStack`
    to handle the opening of multiple files
    '''
    flist = []
    with ExitStack() as stack:
        for file in file_list:
            flist.append(stack.enter_context(open(file, mode)))
        stack.pop_all()
        return flist


def main():
    input_file = '1030 Project 04 03 Files.txt'
    output_file = 'BadrChoubai 02 04 03 Output.txt'
    files_to_combine = []

    with open(input_file, mode='r') as file_list:
        with open(output_file, mode='w') as output_file:
            for line in file_list.readlines():
                files_to_combine.append(line.replace('\n', '.txt'))

            for file in open_files(files_to_combine, mode='r'):
                output_file.write(file.read() + '\n')
                file.close()


if __name__ == "__main__":
    try:
        main()
    except FileNotFoundError as error:
        print(error)
