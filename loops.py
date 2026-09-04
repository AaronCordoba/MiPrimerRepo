Games = ["Call of Duty", "Fortnite", "Minecraft", "Roblox"]

for Game in Games:
    if Game == "Minecraft":
        break # This means that the loop will stop when it reaches "Minecraft"
    print(Game)

for Game in Games:
    if Game == "Minecraft":
        continue # This means that the loop will skip "Minecraft" and continue with the next iteration
    print(Game)

for letter in "Valeria":
    print(letter)

for number in range(1, 11): # Range start at 1 and ends one before 11 
    print(number)
    
count = 5

while count <= 10:
    print(count)
    count = count + 1 
# The loop will stop when count is less or equal to 10



