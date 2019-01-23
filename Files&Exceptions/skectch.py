"""Files and Exceptions"""
from __future__ import print_function

import pickle

man = []
other = []

try:
    # open file
    data = open('sketch.txt')

    print(data.readline(), end='')
    print(data.readline(), end='')
    print()  # print empty line

    data.seek(0)
    for each_line in data:
        print(each_line, end='')
    print()  # print empty line

    data.seek(0)
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)

                # print(role, end='')
                # print(' said: ', end='')
                # print(line_spoken, end='')

        except ValueError:
            pass
    # close file
    data.close()
except IOError:
    print('The data file is missing!')

"""try except finally"""
# try:
#     man_file = open('man_data.txt', 'a')
#     other_file = open('other_data.txt', 'a')
#
#     print(man, file=man_file)
#     print(other, file=other_file)
#
#     # man_file.close()
#     # other_file.close()
# except IOError:
#     print('File error.')
#
# finally:
#     if 'man_file' in locals():
#         man_file.close()
#     if 'other_file' in locals():
#         other_file.close()


"""with replace finally"""
# try:
#     with open('man_data.txt', 'w') as man_file, open('other_data.txt', 'w') as other_file:
#
#         print(man, file=man_file)
#         print(other, file=other_file)
#
#
# except IOError as err:
#     print('File error.' + str(err))

"""pickle dump load"""
try:
    with open('man_data.txt', 'wb') as man_file, open('other_data.txt', 'wb') as other_file:

        pickle.dump(man, man_file)
        pickle.dump(other, other_file)

except IOError as err:
    print('File error.' + str(err))
except pickle.pickleError as perr:
    print('pickling error: ' + str(perr))