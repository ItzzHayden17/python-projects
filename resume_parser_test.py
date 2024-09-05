#pip install resume-parser

from resume_parser import resumeparse

data = resumeparse.read_file("/Fake-Resume.pdf")

print(data)

#Not working,throws errors.