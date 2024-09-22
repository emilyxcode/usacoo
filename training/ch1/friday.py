"""
ID: gallenl1
LANG: PYTHON3
TASK: friday
"""

def isLeapYear(year): # year is the number for the year, e.g, 2024, 1990
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False

daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
daysInWeek = [0] * 7 #[su, mo, tu, we, th, fr, sa] to remember how many days fall info the day of week
daysPassed = 0

# read input
with open("friday.in", "r") as fIn:
    N = int(fIn.readline().strip())

# main logic here!
for y in range(1900, 1900 + N):
    leap = isLeapYear(y)
    for m in range(12):
        daysPassedOn13Th = daysPassed + 13
        wd = daysPassedOn13Th % 7
        daysInWeek[wd] += 1 
        
        daysPassed += daysInMonth[m]
        if leap and m == 1:
            daysPassed += 1
        
daysInWeek = daysInWeek[-1:] + daysInWeek[:-1]

with open("friday.out", "w") as fOut:
    fOut.write(' '.join([str(d) for d in daysInWeek]))
    fOut.write("\n")


"""
Mo Tu We Th Fr Sa Su
1  2  3  4  5  6  7
8  9  10 11 12 13

(31 + 13) % 7 = 
Fed 1: 
1900 Fed 13
G: Tu
I: Tu
M: Tu 
"""   