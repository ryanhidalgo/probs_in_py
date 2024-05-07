#https://edabit.com/challenge/M47FDJLjfNoZ6k6gF
#Models the cup-swapping game
#Rules: 
#There are three cups on a table: A, B, and C
#There is a ball underneath one of the cups (default Cup B)
#Cups are swapped by using a string to indicate which two
#cups are swapped i.e., "AB" or "BA" swaps cups B and A
#Goal:
#Given a list of swaps, keep track of, and report, where the ball will end up

#Input:
#In the command line, arguements are pass as a series of swaps with the
#ball's initial position being the last arguement

import sys

def swap_cups(ball_spot, swap_command):
    if (ball_spot in swap_command): #checks ball is actually being moved
        if (ball_spot != swap_command[0]):
            ball_spot = swap_command[0] #swap ball only if not in place
        else:
            ball_spot = swap_command[1]
    
    print("Ball" + ball_spot)
    return ball_spot
            
#main execution
swap_list = []
for index, arguement in enumerate(sys.argv):
    #every arguement besides first and second is a swap
    if (index == 1):
        ball_start = arguement
    elif (index != 0 and index != 1):
        swap_list.append(arguement)

new_position = ball_start    
for swap in swap_list:
    new_position = swap_cups(new_position, swap)

print("The ball is located in Cup " + new_position)
    
    
    
    