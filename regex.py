import re

a = '^a...s$'
b = 'abyss'
c = 'axis'
d = bool(re.match(a,b))
e = re.match(a,b)
f = re.match(a,c)
print(d)
print(e)
print(f)
print("\n")

# list of meta characters --> [] . ^ $ * + ? {} () \ |
# Metacharacters are characters that are interpreted in a special way by a RegEx engine

a = '[abc]'
b = 'a'
c = 'ac'
d = 'Hey Roy'
e = 'abc de ac'
print(re.findall(a,b))
print(re.findall(a,c))
print(re.findall(a,d))
print(re.findall(a,e))
print("\n")

a = "How are you? how is everything?"
b = "It is what it is"
print(re.findall('[hH]ow',a))
print(re.search("How",a))
print("\n")
c = re.search("what",b)
print(c.span()) # returns starting index and ending index of the word 'what' in a
print(c.start(),c.end())
print(c.group())
print(c.string)
print("\n")

a = "[a-zA-z]"
b = "Abhishek"
print(re.findall(a,b))
c = 'A[^b]' # Any combinations of 2 words starting with A except Ab
print(re.findall(c,b))
print("\n")

a = "My name is Abhishek"
b = '^My' # string should start with My
c = 'Abhishek$' # string should end with Abhishek
print(re.search(b,a))
print(re.search(c,a))
print("\n")

a = '12 03 25 982 2345'
b = '[0-5][0-9]'
print(re.findall(b,a))
print(re.findall('24..',a)) # search 4 digit number in a starting with 24
print("\n")

a = "Blue colour is my favourite color"
print(re.findall('colou?r',a))
print(re.findall('colo[ur]',a))
print("\n")

a = "Today's date is 30-05-2022 and tomorrow will be 31-06-2023. 1 23 345"
print(re.findall('[\d]{2}-[\d]{2}-[\d]{4}',a))
print(re.findall('[\d]{2,3}',a))
#  + character to specify one or more ({1,}) and * character to specify zero or more ({0,}.
print(re.findall('[\d]+',a))
print(re.findall('[\d]*',a))
print("\n")

print(re.sub('([\d]{4})-([\d]{4})-([\d]{4})-([\d]{4})',r'\1.\2.\3.\4','1111-2222-3333-4444'))
print(re.sub('([\d]{4})-([\d]{4})-([\d]{4})-([\d]{4})',r'\1--\2--\3--\4','1111-2222-3333-4444'))
print("\n")

regex = re.compile(r'([\d]{2})-([\d]{2})-([\d]{4})')
print(regex.sub(r'\1.\2.\3', '26-08-2020'))
print("\n")

a = '..'
b = 'a'
c = 'ab'
d = 'abc'
e = 'abcd'
print(re.findall(a,b))
print(re.findall(a,c))
print(re.findall(a,d))
print(re.findall(a,e))
print("\n")

# The plus symbol + matches one or more occurrences of the pattern left to it.
a = 'ma+n'
b = 'mn'
c = 'man'
d = 'maan'
e = 'main'
f = 'woman'
g = 'womaan'
print(bool(re.match(a,b)))
print(bool(re.match(a,c)))
print(bool(re.match(a,d)))
print(bool(re.match(a,e)))
print(re.findall(a,f))
print(re.findall(a,g))
print("\n")

# The star symbol * matches zero or more occurrences of the pattern left to it.
a = 'ma*n'
b = 'mn'
c = 'man'
d = 'maan'
e = 'main'
f = 'woman'
g = 'womaan'
print(bool(re.match(a,b)))
print(bool(re.match(a,c)))
print(bool(re.match(a,d)))
print(bool(re.match(a,e)))
print(re.findall(a,f))
print(re.findall(a,g))
print("\n")

# The question mark symbol ? matches zero or one occurrence of the pattern left to it.
a = 'ma?n'
b = 'mn'
c = 'man'
d = 'maan'
e = 'main'
f = 'woman'
g = 'womaan'
print(bool(re.match(a,b)))
print(bool(re.match(a,c)))
print(bool(re.match(a,d)))
print(bool(re.match(a,e)))
print(re.findall(a,f))
print(re.findall(a,g))
print("\n")

#Consider this code: {n,m}. This means at least n, and at most m repetitions of the pattern left to it.
a = 'a{2,3}'
b = 'abc dat'
c = 'abc daat'
d = 'aabcdaaat'
e = 'aabc daaaat'
print(re.findall(a,b))
print(re.findall(a,c))
print(re.findall(a,d))
print(re.findall(a,e))
print("\n")

# at least 2 digits but not more than 4 digits
a = '[0-9]{2,4}'
b = 'abc123de'
c = '12 and 123456'
d = '1 and 2'
e = '12 and 12345'
print(re.findall(a,b))
print(re.findall(a,c))
print(re.findall(a,d))
print(re.findall(a,e))
print("\n")

# '|' stands for or
a = 'a|b'
b = 'abhishek is blessing in disguise'
print(re.findall(a,b))

a = '(a|b|c)xz'
b = 'ab xz'
c = 'abxz'
d = 'axz cabxz'
print(re.findall(a,b))
print(re.findall(a,c))
print(re.findall(a,d))
print("\n")

a = '\$e' # backslash '\' is used to escape metacharacters
b = 'Portuge$e'
print(re.findall(a,b))
print('\n')

# \A if specified characters/string is at the start
a = '\Athe'
b = 'the power'
c = 'in the kingdom'
print(re.findall(a,b))
print(re.findall(a,c))
print("\n")

# \b - Matches if the specified characters are at the beginning or end of a string.
a = '\\bfoot'
b = 'footballfoot'
c = 'big foot'
d = 'afootball'
print(re.findall(a,b))
print(re.findall(a,c))
print(re.findall(a,d))
print('\n')

# \B - Matches if the specified characters are  not at the beginning or end of a string.
a = '\Bfoot'
b = 'football'
c = 'big foot'
d = 'afootball'
print(re.findall(a,b))
print(re.findall(a,c))
print(re.findall(a,d))
print('\n')

# \d -  Matches any decimal digit. Equivalent to [0-9]
# \D -  Matches any non-decimal digit. Equivalent to [^0-9]
a = '\d'
b = '\D'
c = 'ab 12'
print(re.findall(a,c))
print(re.findall(b,c))
print("\n")

# \s - Matches where a string contains any whitespace character. Equivalent to [ \t\n\r\f\v].
# \S - Matches where a string contains any non-whitespace character. Equivalent to [^ \t\n\r\f\v]
# \w - matches alphabets and digits and '_'
# \W - matches non alphabets and non digits

# \Z - Matches if the specified characters are at the end of a string
a = 'Python\Z'
b = 'Pyhton is good'
c = 'it is a Python'
print(re.findall(a,b))
print(re.findall(a,c))
print('\n')

# r or R means raw string. '\n' is a new line whereas r'\n' means 2 characters a backslash '\' followed by n
# lookahead, lookbehind, negative lookahead, negative lookbehind









