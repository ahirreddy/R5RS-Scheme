import re

text = open('grammar.txt').read()

while re.search(r'<([^ <>]+ )+([^ <>]+)>', text):
	pattern = re.compile(r"<([^ <>]+ )+([^ <>]+)>")
	text = pattern.sub(lambda match: match.group(0).replace(' ', '-'), text)

print text
