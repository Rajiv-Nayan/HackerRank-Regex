Regex_Pattern = r"(\S)(?!\1)"	

import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))
