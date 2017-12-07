from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random
blocks = (103, 52, 53, 101, 69)
x = 109.5
y = 0.0
z = 86.5
blockType = random
mc.setBlock(x, y, z, blockType)

