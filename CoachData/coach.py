"""deal with data 2"""

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

print(sorted(james))
print(sorted(julie))
print(sorted(mikey))
print(sorted(sarah))

