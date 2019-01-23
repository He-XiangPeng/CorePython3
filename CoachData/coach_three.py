"""deal with data 3"""


# >>> distance = {1, 1, 1, 1, 2, 3}
# >>> print(distance)
# set([1, 2, 3])
# set usage

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' +secs)

with open('james.txt') as jaf:
    data = jaf.readline()
james = data.split(',')

with open('julie.txt') as juf:
    data = juf.readline()
julie = data.split(',')

with open('mikey.txt') as mif:
    data = mif.readline()
mikey = data.split(',')

with open('sarah.txt') as saf:
    data = saf.readline()
sarah = data.split(',')

james = sorted([sanitize(t) for t in james])
julie = sorted([sanitize(t) for t in julie])
mikey = sorted([sanitize(t) for t in mikey])
sarah = sorted([sanitize(t) for t in sarah])

"""delete the repeat data"""
unique_james = []
for each_t in james:
    if each_t not in unique_james:
        unique_james.append(each_t)
print(unique_james[0:3])

unique_julie = []
for each_t in julie:
    if each_t not in unique_julie:
        unique_julie.append(each_t)
print(unique_julie[0:3])

unique_mikey = []
for each_t in mikey:
    if each_t not in unique_mikey:
        unique_mikey.append(each_t)
print(unique_mikey[0:3])

unique_sarah = []
for each_t in sarah:
    if each_t not in unique_sarah:
        unique_sarah.append(each_t)
print(unique_sarah[0:3])