# Aula sobre SETS

# s1 = set() #vazio
# s1 = {'Luiz', 1,2,3}  # com dados

# print(s1)

# s1 = {1,2,3}
# print(4 in s1)

s1 = set()
s1.add('Guilherme')
s1.add(500)
s1.update(('Santos FC', 2))
s1.discard(500)
# print(s1)

s1 = {1,2,3}
s2 = {2,3,4}
s3 = s1 | s2
s3 = s1 & s2
s3 = s1 - s2

print(s3)