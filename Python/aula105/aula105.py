import re

txt = "O Gabriel amigo do Miguel"

x = re.search("^O.*Miguel$", txt)

if x:
    print("Sim! nos temos uma correspondencia!")
else:
    print("Nemhuma correspondecia!")