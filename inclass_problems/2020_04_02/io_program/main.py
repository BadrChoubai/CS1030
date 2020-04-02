input_file = 'student_names.txt'
output_file = 'sorted_student_names.txt'


def cleanse_input(lines: list) -> list:
    for i, line in enumerate(lines):
        if '\n' in line:
            lines[i] = line.replace('\n', '')

    return lines


def main():
    all_names = None

    try:
        with open(input_file, 'r') as student_names:
            all_names = student_names.readlines()

    except IOError:
        print("Could not read file", input_file)

    else:
        # Clean the input (remove newline characters, etc...)
        all_names = cleanse_input(all_names)
        # Sort the names list
        sorted_names_list = sorted(all_names)

        try:
            with open(output_file, 'w') as student_names_output:
                for name in sorted_names_list:
                    student_names_output.write(f'{name}\n')

        except IOError:
            print('Could not read file', output_file)


if __name__ == "__main__":
    main()
