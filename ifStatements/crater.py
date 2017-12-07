from mcpi.minecraft import Minecraft
mc = Minecraft.create()
answer = input("Create a crater? Y/N ")

password = "dogs"
attempt = input("Please enter the password: ") 
if attempt == password:
    print("Password is correct")
print("Program finished")

pos = mc.player.getPos()
mc.setBlocks(pos.x +50, pos.y +50, pos.z + 50, pos.x - 50, pos.y - 50, pos.z - 50, 0)
mc.postToChat("BOOM!!!!!!!!!!")

