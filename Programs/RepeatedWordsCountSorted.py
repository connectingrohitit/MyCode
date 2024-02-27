import pandas as pd
import re


string1 = """Selenium was originally developed by Jason Huggins in 2004 as an internal tool at 
ThoughtWorks.[5] Huggins was later joined by other programmers and testers at ThoughtWorks, before Paul 
Hammant joined the team and steered the development of the second mode of operation that would later become 
"Selenium Remote Control" (RC). The tool was open sourced that year. In 2005 Dan Fabulich and Nelson Sproul 
(with help from Pat Lightbody) made an offer to accept a series of patches that would transform Selenium-RC 
into what it became best known for. In the same meeting, the steering of Selenium as a project would continue 
as a committee, with Huggins and Hammant being the ThoughtWorks representatives."""

#clean the string i.e. replace special chars with space
clean = re.sub('[^A-Za-z0-9]+', ' ', string1)
clean = clean.replace('\n', '')
print(clean)
lst = clean.split(' ')

# Solution using Pandas
count = pd.Series(lst).value_counts()
print(count.to_string())

# Solution using dictionary (without Pandas)
dict1 = {}
for item in lst:
    dict1[item] = lst.count(item)

print(sorted(dict1.items(), key=lambda x:x[1], reverse=True)) #sort the dictionary