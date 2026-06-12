'''
#Regular Expression(RegEx) : RegEx is a sequence of char that from a searching pattern.
   ---this can be used to check if a string contain a specific search pattern.
   ---python has a built-in package called "re" which can be used to work with RegEx.
#Functions in regular expression
--findall
--search
--fullmatch
'''
#Metachar:[]--->a-z,A-Z,0-9
import re
any="Reading is a transformative practice that transports us beyond the boundaries of our own lived experiences, allowing us to walk in the shoes of others and explore entirely new worlds"
print(re.findall("[a]",any))

#
import re
any="Reading is a transformative practice that transports us beyond the boundaries of our own lived experiences, allowing us to walk in the shoes of others and explore entirely new worlds"
print(re.findall("[als]",any))

#
import re
any="Reading is a transformative practice3 that transports4 us beyond the 5boundaries of our own6 lived experiences, 7allowing us to 8walk in the shoes of others and explore entirely new worlds"
print(re.findall("[0-9]",any))

#Metachar: .(dot) here each is one char
import re
any="Reading is a transformative practice that transports us beyond the boundaries of our own lived experiences, allowing us to walk in the shoes of others and explore entirely new worlds"
print(re.findall("b.u.d..i..",any))


#Metachar: ^  it look for the string is starting with specified sequence or not.
import re
any="Reading is a transformative practice that transports us beyond the boundaries of our own lived experiences, allowing us to walk in the shoes of others and explore entirely new worlds"
print(re.findall("^Reading",any))

#
import re
any="Reading is a transformative practice that transports us beyond the boundaries of our own lived experiences, allowing us to walk in the shoes of others and explore entirely new worlds"
print(re.search("^Reading",any))


#Metachar: $it look for the string is ending with specified sequence or not.

import re
any="Reading is a transformative practice that transports us beyond the boundaries of our own lived experiences"
print(re.findall("es$",any))

#
import re
any="Reading is a transformative practice that transports us beyond the boundaries of our own lived experiences"
print(re.findall("e.*nces",any))


#Metachar: * zero or more
#metachar: ?zero or more
#Metachar: +one or more
#Metachar:{}
import re
any="Reading is a transformative practice that transports us beyond the boundaries of our own lived experiences"
print(re.findall("^R.{6}",any))


#import re
any="Reading is a transformative practice that transports us beyond the boundaries of our own lived experiences, allowing us to walk in the shoes of others and explore entirely new worlds"
print(re.search("^Reading",any))

import re
any="Reading is a transformative practice that transports us beyond the boundaries of our own lived experiences"
print(re.findall("p.{5}",any))


#special sequence: \S--no space, \s--only space , \D--non digit, \d--only digits,\w--match any word char(letters,digits,underscore),\W--Non-words
import re
any="Reading is a transformative practice that transports us beyond the boundaries of our own lived experiences"
print(re.findall("\S",any))

import re
any="Reading is a transformative practice that transports us beyond the boundaries of our own lived experiences"
print(re.findall("\s",any))

import re
any="Reading is a transformative practice4536 that transports us beyond the boundaries of our own lived experiences"
print(re.findall("\D",any))

import re
any="Reading is a transformative practice that67534 transports us beyond the boundaries of our own lived experiences"
print(re.findall("\d",any))

import re
any="Reading is a transformative practice that transports 987756 us beyond the boundaries of our own lived experiences"
print(re.findall("\w",any))

import re
any="Reading is a transformative@ & practice that transports 987756 us beyond the boundaries of our own lived experiences"
print(re.findall("\W",any))


#program
import re
mobile=input("Enter 10 digit mobile num: ")
how =re.fullmatch("[6-9][0-9]{9}",mobile)
if how:
    print(f"{mobile} this is Indian number")
else:
    print(f"{mobile} this is not Indian number")








