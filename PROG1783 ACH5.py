import re

source = "Lorem ipsum doflor meet szit ametß, consqecytetu$r chaudhari adipibsching 8738594 elit, sed do  eiusmod tewmporα incid6kgidunt ut labq8ore et café dolore_ magna aliqua. Purus! sit{|}~\t\n\r\x0b\x0c amet volutpat cons&jequat mau7ris. Penaxtibus et"

findallEffs = re.findall("m", source)
print('Found ',len(findallEffs), 'matches of the letter m')

findallDigits = re.findall("\d", source)
print('Found',len(findallDigits), 'matches of digits')

findallAlphaNumerics = re.findall("\w", source)
print('Found',len(findallAlphaNumerics), 'matches of alphanumeric characters')

findallNonAlphaNumerics = re.findall("\W", source)
print('Found',len(findallNonAlphaNumerics), 'matches of non-alphanumeric characters')

findallSpaces = re.findall("\s", source)
print('Found',len(findallSpaces), 'matches of spaces')


