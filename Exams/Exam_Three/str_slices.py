my_str = 'supercalifragilisticexpialidocious'


def selective_slice(string, slice_len):
    for i in range(0, len(string), slice_len):
        print(string[i:i+slice_len])


selective_slice(my_str, len(my_str)//2)
