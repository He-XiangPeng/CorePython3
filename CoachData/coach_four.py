"""deal with data 4 multiple-cursor Alt+click"""


"""change the data to same type"""
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' +secs)

# with open('james.txt') as jaf:
#     data = jaf.readline()
# james = data.split(',')
#
# with open('julie.txt') as juf:
#     data = juf.readline()
# julie = data.split(',')
#
# with open('mikey.txt') as mif:
#     data = mif.readline()
# mikey = data.split(',')
#
# with open('sarah.txt') as saf:
#     data = saf.readline()
# sarah = data.split(',')
"""change to method"""
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        return(data.strip().split(','))

    except IOError as ioerr:
        print('File Error:' + str(ioerr))
        return(None)


james = get_coach_data('james.txt')
julie = get_coach_data('julie.txt')
mikey = get_coach_data('mikey.txt')
sarah = get_coach_data('sarah.txt')


"""delete the repeat data use set()"""
# >>> distance = {1, 1, 1, 1, 2, 3,5, 2, 7, 4}
# >>> print(distance)
# set([1, 2, 3, 4, 5, 7])
#
# unique_james = []
# for each_t in james:
#     if each_t not in unique_james:
#         unique_james.append(each_t)
# print(unique_james[0:3])
#
# unique_julie = []
# for each_t in julie:
#     if each_t not in unique_julie:
#         unique_julie.append(each_t)
# print(unique_julie[0:3])
#
# unique_mikey = []
# for each_t in mikey:
#     if each_t not in unique_mikey:
#         unique_mikey.append(each_t)
# print(unique_mikey[0:3])
#
# unique_sarah = []
# for each_t in sarah:
#     if each_t not in unique_sarah:
#         unique_sarah.append(each_t)
# print(unique_sarah[0:3])
print(sorted(set([sanitize(t) for t in james]))[0:3])
print(sorted(set([sanitize(t) for t in julie]))[0:3])
print(sorted(set([sanitize(t) for t in mikey]))[0:3])
print(sorted(set([sanitize(t) for t in sarah]))[0:3])