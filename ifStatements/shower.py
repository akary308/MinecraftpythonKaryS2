from mcpi.minecraft import Minecraft
mc = Minecraft.create()

shwrX = 109.5
shwrY = 0.0
shwrZ = 86.5

width = 5
height = 5
length = 5

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

if shwrX <= x < shwrX + width and mc.setBlocks(shwrX, shwrY + height, shwrZ,shwrX + width, shwrY + height, shwrZ + length, 8)
    
else:
    mc.setBlocks(shwrX, shwrY + height, shwrZ,shwrX + width, shwrY + height, shwrZ + length, 0)
