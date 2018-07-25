from mcpi import minecraft

mc = minecraft.Minecraft.create()

mc.postToChat("Hello world")

pos = mc.player.getPos()

x, y, z = mc.player.getPos()
mc.player.setPos(x, y+100, z)

tnt = 46
mc.setBlocks(x+1, y+1, z+1, x+11, y+11, z+11, tnt, 1)

    
