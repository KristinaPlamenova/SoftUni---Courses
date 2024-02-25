size = int(input())

matrix = []
position = []
bags_tea = 0
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}
for row in range(size):
    matrix.append(input().split())


    if "A" in matrix[row]:
        position = [row, matrix[row].index("A")]
        matrix[row][position[1]] = "*"


while bags_tea < 10:
    direction = input()

    row = position[0] + directions[direction][0]
    col = position[1] + directions[direction][1]

    if not (0 <= row < size and 0 <= col < size):
        break

    position = [row, col]
    element = matrix[row][col]
    matrix[row][col] = "*"

    if element == "R":
        break

    if element.isdigit():
        bags_tea += int(element)

if bags_tea < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

for row in matrix:
    print(*row)













