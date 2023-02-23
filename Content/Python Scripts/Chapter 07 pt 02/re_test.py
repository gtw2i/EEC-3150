import re

text = "If you know Python,    then\nyou're power level is over 9000"
print(text)

# find all words (no contractions)
pattern = r"\w+"
print(re.findall(pattern, text))

# find all words (with contractions)
pattern = re.compile(r"[\w']+")
print(re.findall(pattern, text))

# find all numbers
pattern = re.compile(r"\d+")
print(re.findall(pattern, text))



# find phone numbers
text = "my number is (615) 555-1234. her number is (012) 345-6789"
pattern = r"\(\d{3}\) \d{3}-\d{4}"
print(re.findall(pattern, text))



# find dates
text = "I made $12.21 she made $4,001.99 he made $1,033,080.01"
pattern = r"\$[\d,]+[\.\d{2}]*"
print(re.findall(pattern, text))




