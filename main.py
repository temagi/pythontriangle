import shlex
from triangle.calculate_triangle import triangle


print('Enter triangle sides with a `,` separator')

while True:
    cmd, *args = shlex.split(input('> '))
    # TODO: Add normal filtration of input data
    shell = cmd.split(',')

    print(triangle(int(shell[0]), int(shell[1]), int(shell[2])))
