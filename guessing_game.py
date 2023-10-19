# IMPORTED MODULES
import random

    # random number chosen
def get_rand_num(past_nums) :
    rand_num = random.randint(1, 10)
    past_nums.append(rand_num)
    if len(past_nums) >= 3 :
        past_nums.pop(0)
        
    print('NUMBER: {}'.format(rand_num))
    return rand_num

def handle_win(loop_count, high_score, game_count) :
    print("\n*** --- !CONGRATULATIONS - YOU'VE GUESSED CORRECTLY! --- ***\n")
    final_score = loop_count + 1
    if game_count == 1 :
        high_score = final_score
        print("You've set a new high score!")
    else :
        if final_score < high_score :
            high_score = final_score
        print("You've set a new high score!")
    print( 'STATS:\n--High Score: {}\n--Final Score: {}\n--Total Game Rounds: {}'.format(high_score, final_score, game_count) )

    win_prompt = raw_input('\nPlay again?(yes/no)  ')
    print(win_prompt)

    if win_prompt.upper() == 'YES' :
        game_count += 1
        stats_arr = [1, high_score, final_score, game_count]
        return stats_arr
    elif win_prompt.upper() == 'NO' :
        stats_arr = [0, high_score, final_score, game_count]
        return stats_arr

# continuously prompts user for a guess until win
def game_loop(rand_num, game_count, high_score) :
    print(rand_num)
    loop_count = 0

    while True :
        # provide feedback based on user input
        # try:
            user_num = int( input('Pick a number from 1 to 10:  ') )

            if user_num < 1 or user_num > 10 :
                print('Number entered is outside of range. Please enter a number from 1 to 10.')
            elif user_num > rand_num :
                print('Think Lower!')
                loop_count += 1
            elif user_num < rand_num :
                print('Think Higher!')
                loop_count += 1
            elif user_num == rand_num :
                stats_arr = handle_win(loop_count, high_score, game_count)
                return stats_arr
        # catches errors that arise from poor user input
        # except NameError:
        #     print('Input could not be read. Please enter only a whole number from 1 to 10.')
        #     continue
        # except SyntaxError as err:
        #     print('Input could not be read. Please enter only a whole number from 1 to 10.')
        #     print(err)
        #     continue

def start_game() :
    # function variables
    past_nums = []
    high_score = 0
    game_count = 1

    # game introduction
    print("""
        *** -------------------- ***
        !!!  WELCOME & HAVE FUN  !!!
        *** -------------------- ***
    """)
    if high_score == 0 :
        print('HIGH SCORE will be unlocked after first play through!')
    else :
        print( 'HIGH SCORE: {}'.format(high_score) )
        print( 'GAME COUNT: {}'.format(game_count) )
    print('\nTO PLAY:\n--Enter you guess of a number from 1-10 into the command line.\n--If you guess incorrectly you will be given a hint.\n--If you guess correctly the game will end and you can play again!')

    rand_num = get_rand_num(past_nums)
    print(rand_num)

    stats_arr = game_loop(rand_num, game_count, high_score)
    print(stats_arr)

    if stats_arr[0] == 0 :
        return stats_arr
    else :
        high_score = stats_arr[1]
        game_count = stats_arr[3]
        rand_num = get_rand_num(past_nums)
        stats_arr = game_loop(rand_num, game_count, high_score)
        print(stats_arr)
    
# calls function to start game
stats_arr = start_game()
print("""
        *** -------------------- ***
        !!!  THANKS FOR PLAYING  !!!
        *** -------------------- ***
    """)
print(stats_arr)