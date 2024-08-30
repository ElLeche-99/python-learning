import textwrap

minutes = int(input())
inveted_people = 1

for x in range(minutes):
    inveted_people = inveted_people * 2

substring = textwrap.wrap(str(inveted_people), width=50)

for lines in substring:
    print(lines)
