# source: https://www.youtube.com/watch?v=UQQsYXa1EHs

import re

pattern = '.(com|edu|net)'
your_input: str = input('enter the string: ')
if (re.search(pattern, your_input)):
    print('Valid email')
else:
    print('invalid email')