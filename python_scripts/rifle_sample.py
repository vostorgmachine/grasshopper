# Построение логики для автоматизации рифлёнки.

x_size = int(x_size)

# aol = amount of lines
aol = x_size // 10


step = x_size - (aol * 10) 
x_line_size = int(step) / aol 
x_line_size = x_line_size + 10

print(step)
print(x_line_size)
