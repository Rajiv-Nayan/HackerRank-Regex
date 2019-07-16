Regex_Pattern = r'\b[aeiuoAEIOU][a-zA-z]*\b'

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
