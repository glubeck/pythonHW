#!/usr/bin/env python

import re

i = 0
assignmentList = []
gradesList = []
with open("grades.txt") as f:
    for line in f:
        if line[0] == "#":
            assignmentList.append(line)
        elif line != "\n":
            gradesList.append(line)
print "Content-type: text/html"
print
print "<h1>Grades</h1>"
for assignment in assignmentList:
    print "<h2>"
    print assignment
    print "</h2>"
    for grade in gradesList:
        print "<p>"
        print grade
        print "</p>"
