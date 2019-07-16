Regex_Pattern = r'^[^0-9][^aeiou][^bcDF][^\r\n\t\f\s][^AEIOU][^.,]$'

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
