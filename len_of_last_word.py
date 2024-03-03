#Calculate the len of Last word


s = "   fly me   to   the moon  "
s1 = s.strip()
c = 0
for i in range(len(s1)-1, -1, -1):
    if s1[i] == " ":
        break
    c += 1

print(c)
