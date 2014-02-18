import minecraft as minecraft
import block as block
import time

if __name__ == "__main__":
    time.sleep(2)
    mc = minecraft.Minecraft.create()
    mc.postToChat("Minecraft Remote Control Connected!")
    playerPos = mc.player.getPos()
    nb = raw_input('Enter a command: w - forward, s - backwards, a - left, d - right. Then press Enter')
    if nb == 'w':
        mc.player.setPos(playerPos.x + 10, playerPos.y, playerPos.z)
    if nb == 's':
        mc.player.setPos(playerPos.x - 10, playerPos.y, playerPos.z)
    if nb == 'a':
        mc.player.setPos(playerPos.x, playerPos.y, playerPos.z + 10)
    if nb == 'd':
        mc.player.setPos(playerPos.x, playerPos.y, playerPos.z - 10)
