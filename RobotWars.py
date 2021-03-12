#RobotWars

# Object for bot
class bot:
    def __init__(self,x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

        
class robotWars:
    # Method to move bot around matrix and update it's co-ordinates position
    def navigator(inputs,arena,bot):
        direction = ["N", "E", "S", "W"]
        # Points to the direction the bot is facing(in the direction array).
        pointer = direction.index(bot.direction)
        for x in inputs:
            if x == "L":
             # move pointer one to the left, if pointer is at the start of list move it to the end of the list.               
                if pointer == 0:
                    pointer = 3
                else:
                    pointer -= 1
            if x == "R":
                # move pointer one to the right, if pointer is at the end of the list move it to the start of the list.
                if pointer == 3:
                    pointer = 0
                else:
                    pointer += 1
            if x == "M":
                # when moving change bots co-ordinates and arena position accordingly.
                if direction[pointer] == "N":
                    arena[bot.x][bot.y] = 0
                    arena[bot.x][bot.y+ 1] = "x"   
                    bot.y += 1   
                if direction[pointer] == "E":
                    arena[bot.x][bot.y] = 0
                    arena[bot.x + 1][bot.y] = "x"
                    bot.x += 1 
                if direction[pointer] == "S":
                    arena[bot.x][bot.y] = 0
                    arena[bot.x][bot.y-1] = "x" 
                    bot.y -= 1
                if direction[pointer] == "W":
                    arena[bot.x][bot.y] = 0
                    arena[bot.x - 1][bot.y] = "x"
                    bot.x -= 1

        return(str(bot.x) + " " + str(bot.y) + " " +  bot.direction)


def main():
    row_col = [5+1,5+1]
    arena = [[0]*row_col[1] for i in range(row_col[0])]
    bot1 = bot(1,2,"N")
    inputs = "LMLMLMLMM"
    print(robotWars.navigator(inputs,arena,bot1))
    bot2 = bot(3,3,"E")
    inputs = "MMRMMRMRRM"
    print(robotWars.navigator(inputs,arena,bot2))
    print(arena)

if __name__ == "__main__":
    main()
