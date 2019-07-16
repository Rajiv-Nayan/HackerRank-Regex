Regex_Pattern = r"^(12)(-?)(34)(-?)(56)(-?)(78)$"	

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
