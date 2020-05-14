import os, re

txt = re.compile(r'(.*\.txt$)')

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+               # username
    @                               # @ symbol
    [a-zA-Z0-9.-]+                  # domain name
    (\.[a-zA-Z]{2,4})               # dot something
    )''', re.VERBOSE)

matches = []
for filename in os.listdir(os.getcwd()):
    if re.match(txt, filename):
        file = open(filename, "r")
        fileContent = file.read()
        for groups in emailRegex.findall(fileContent):
            matches.append(groups[0])

if len(matches) > 0:
    print("All email addresses:")
    print("\n".join(matches))
else:
    print("No email addresses found.")
