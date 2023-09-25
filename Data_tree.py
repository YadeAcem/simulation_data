
# # Read only r
# # Read and Write r+  (beginning of file)
# # Write Only w   (over-written)
# # Write and Read w+  (over written)
# # Append Only a  (end of file)
# # Append and Read a+  (end of file)


# def open_file():
#     file_name = askopenfilename(
#         filetypes=[('experiment files', '*.txt')])
#
#     print('wtf')
#     return file_name
#     # return file_name
#     # print(file_name)
#     # return file_name
#     # if file_name is not None:
#     #     content = file_name.read()
#     #     # print(content)
#     # # print(file_name)
#     # return file_name
#
#         # print(self.rows[0])
#         # print(rows)


from plb import *
import pandas as pb

def read_file(file):
    with open (file) as f:
        lines = f.readline()
        print(lines)
        # self.content
        # rows.extend(content.splitlines())
        # print(rows)
    # return rows


def split_elements():
    print('je ziet mij')
    # print(rijen)


if __name__ == '__main__':
    my_gui = GUI()
    namen = my_gui.get_path()
    read_file(namen)

