import os

print(os.name)
print(system.platform)

path = os.path.dirname(__file__)

handler = open\

    (path + '/text.txt')

json_str = '"key":"value", "key2":1234'
loaded = json.loads(json_str)

#while True:
#        print(1)
#        time.sleep(1)

#print(handler.read)
#print(handler.readline())
#print(handler.tell())
#print(handler.readline())
#print(handler.tell())
#print(handler.readline())
#print(handler.readline())

#print(handler)
#print(type(handler))

########################################################################################################

def read_specific_fine(file_path, line_number: int) -> str:
    handler = open(file_path)
    current_line = None
    current_line_number = 0
    while   current_line_number < line_number:
        current_line = handler.readline()
        current_line_number += 1
    print(current_line)

    return ''

read_specific_fine()

with open(path + '/home/janvozar/PycharmProjects/Python_Academy/8_lesson/text.txt', 'w') as handler:
    # do something with file
    handler.write('a\n')
    handler.write('a\n'
    print(handler.closed)
print(handler.closed)