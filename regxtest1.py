
import re

# check if the strign kstarts with
txt = "The rain in Spain"
x = re.search("^The/.*Spain$", txt)

if (x):
    print("YES! We have a match")
else:
    print("No match")