
reader = open("input", "r")
writer = open("output", "w")

a_count = 0
c_count = 0
g_count = 0
t_count = 0

lines = reader.readlines()

for i in range(0, len(lines)):
    for j in range(0, len(lines[i])):
        char = lines[i][j]

        if char == 'A':
            a_count += 1
        elif char == 'C':
            c_count += 1
        elif char == 'G':
            g_count += 1
        elif char == 'T':
            t_count += 1

msg = str(a_count) + " " + str(c_count) + " " + str(g_count) + " " + str(t_count)

writer.write(msg)

reader.close()
writer.close()
