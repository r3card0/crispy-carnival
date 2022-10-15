# source: https://www.youtube.com/watch?v=UQQsYXa1EHs

import re

pattern = '(\d\d\d)-(\d\d\d)-(\d\d\d\d)'
new_pattern = r'\1\2\3'
your_input = input('enter: ')
new_user_input = re.sub(pattern,new_pattern,your_input)
print(new_user_input)