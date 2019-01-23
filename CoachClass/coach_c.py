"""deal with data """

"""change the data to same type"""


def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)


"""change to method"""


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        return (data.strip().split(','))

    except IOError as ioerr:
        print('File Error:' + str(ioerr))
        return (None)


sarah = get_coach_data('sarah2.txt')
"""one way"""
# (sarah_name, sarah_dob) = sarah.pop(0), sarah.pop(0)
# print(sarah_name + "'s fastest time are: " +
#       str(sorted(set([sanitize(t) for t in sarah]))[0:3]))

"""Dict way"""
sarah_data = {}
sarah_data['name'] = sarah.pop(0)
sarah_data['DOB'] = sarah.pop(0)
sarah_data['Times'] = sarah
print(sarah_data['name'] + "'s fastest time are: " +
      str(sorted(set([sanitize(t) for t in sarah_data['Times']]))[0:3]))
