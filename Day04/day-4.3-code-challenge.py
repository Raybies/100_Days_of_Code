# Treasure Map
row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]
# nested list
map = [row1, row2, row3]

# to print each variable on a new line 
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?  ")

#indices Row 1-2-3 and Column 1-2-3 (column then row)
# row and convert to int
horizontal = int(position[0])

# column and convert to int
vertical = int(position[1])

# convert to match indexing
selected_row = map[vertical-1]

# changes square to X
selected_row[horizontal-1] = "🏴"

# shortcut removes lines 20 & 23
map[vertical-1][horizontal-1] = "X"


print(f"{row1}\n{row2}\n{row3}")