# this dosent work mineflayer was a better option


from mcpi import minecraft
from time import sleep

# Connect to the Minecraft server
mc = minecraft.create(address="106.212.68.95", port=25565)

# Define the movement function
def move_forward(player_name, blocks):
    player = mc.getPlayerEntityByName(player_name)
    
    if player is None:
        print(f"Player '{player_name}' not found!")
        return
    
    player_pos = player.getTilePos()
    player_dir = player.getDirection()
    
    for i in range(blocks):
        new_x = player_pos.x + player_dir.x
        new_y = player_pos.y + player_dir.y
        new_z = player_pos.z + player_dir.z

        player.setTilePos(new_x, new_y, new_z)
        sleep(0.4)  # Delay for 1 second between each movement

# Main program
if __name__ == "__main__":
    player_name = "CODE7X"  # Specify the player name to control
    move_forward(player_name, 10)  # Move the specified player forward 10 blocks
