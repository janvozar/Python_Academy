target = input('SEARCH WORD: ')

text = '''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.'''

words = text.split()
found = False
position = 0

for i,word in enumerate(words):
    word = word.strip(';,._/:')
    if word == target:
        found = True
        position = i + 1

if found:
    print('POSITION: ' + str(position))
else:
    print('NO SUCH WORD')