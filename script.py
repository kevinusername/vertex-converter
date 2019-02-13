import sys

f = open(sys.argv[1], 'r')

output = f'vector<Vertex> {sys.argv[1][2:len(sys.argv[1])-4]} = {{'

for line in f:
    comma = line.find(',')
    x_cord = str((int(line[0:comma]) / 500) - .5)[:6] + 'f'
    y_cord = str((1-(int(line[comma + 1:]) / 500)) - 0.5)[:6] + 'f'
    output += f"Vertex({x_cord},{y_cord}),"

output += f"}};\ndraw_curve({sys.argv[1][2:len(sys.argv[1])-4]}, 5);"

print(output)
