import sys
tag = "12X874-32"
def is_odd(n):
    return not (n%2 == 0)
if is_odd(int(tag[0]) + int(tag[1])) or is_odd(int(tag[3]) + int(tag[4])) or is_odd(int(tag[4]) + int(tag[5])) or is_odd(int(tag[5]) + int(tag[7])) or is_odd(int(tag[7]) + int(tag[8])):
    sys.stdout.write('invalid')
    sys.exit()
elif tag[2] not in [ "A","E","I","O","U","Y"]:
    sys.stdout.write('invalid2')
    sys.exit()
sys.stdout.write('valid')
