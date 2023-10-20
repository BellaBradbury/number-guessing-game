# IMPORTED MODULES
import random

# SELECTS AND RETURNS A FRESH RANDOM NUMBER
def get_rand_num(past_nums) :
    rand_num = random.randint(1, 10)
    past_nums.append(rand_num)
    if len(past_nums) >= 3 :
        past_nums.pop(0)
        
    print('NUMBER: {}'.format(rand_num))
    return rand_num

# CONGRATULATES THE USER ON A WIN, PROVIDES STATS, & PROMPTS TO CONTINUE
def handle_win(final_score, high_score, game_count) :
    print("\n*** --- !CONGRATULATIONS - YOU'VE GUESSED CORRECTLY! --- ***\n")
    if game_count == 1 :
        high_score = final_score
    else :
        if final_score < high_score :
            high_score = final_score
            print("You've set a NEW HIGH SCORE!")
    print( 'STATS:\n--High Score: {}\n--Final Score: {}\n--Total Game Rounds: {}'.format(high_score, final_score, game_count) )

    win_prompt = input('\nPlay again?(yes/no)  ')
    stats_arr = [3, high_score, game_count]
    if win_prompt.upper() == 'YES' :
        stats_arr[0] = 1
        print('GOING AGAIN', stats_arr)
        return stats_arr
    elif win_prompt.upper() == 'NO' :
        stats_arr[0] = 0
        print('END', stats_arr)
        return stats_arr
    
# GUESS LOOPS
def guess_loop(final_score, rand_num, game_count, high_score) :
    while True :
    # provide feedback based on user input
        # try:
            user_num = int( input('Pick a number from 1 to 10:  ') )

            if user_num < 1 or user_num > 10 :
                print('Number entered is outside of range. Please enter a number from 1 to 10.')
            elif user_num > rand_num :
                print('Think Lower!')
                final_score += 1
            elif user_num < rand_num :
                print('Think Higher!')
                final_score += 1
            elif user_num == rand_num :
                stats_arr = handle_win(final_score, high_score, game_count)
                print('STATS ARR AFTER HANDLE WIN: ', stats_arr)
                return stats_arr
            # catches errors that arise from poor user input
        # except NameError:
        #     print('Input could not be read. Please enter only a whole number from 1 to 10.')
        #     continue
        # except SyntaxError as err:
        #     print('Input could not be read. Please enter only a whole number from 1 to 10.')
        #     print(err)
        #     continue

# MANAGES VARIABLES & RUNS GAME FUNCTIONS
def start_game() :

    # game intro
    print("""
        *** -------------------- ***
        !!!  WELCOME & HAVE FUN  !!!
        *** -------------------- ***
    """)
    print('\nTO PLAY:\n--Enter a number from 1-10 into the command line to make your guess.\n--If you guess incorrectly you will be given a hint.\n--If you guess correctly the game will end and you can play again!')

    # game play
    past_nums = []
    high_score = 0
    game_count = 1

    while True : 
        print("\n*** --- NEW GAME --- ***")
        rand_num = get_rand_num(past_nums)
        final_score = 1

        if high_score == 0 :
            print('HIGH SCORE will be unlocked after first play through!\n')
        else :
            print( '\nHIGH SCORE: {}\n'.format(high_score) )

        stats_arr = guess_loop(final_score, rand_num, game_count, high_score)
        print('STATS ARR AFTER GUESS LOOP: ', stats_arr)

        if stats_arr[0] == 1 :
            game_count += 1
            high_score = stats_arr[1]
            game_count = stats_arr[2]
        else :
            break

    # game outro
    print("""
        *** -------------------- ***
        !!!  THANKS FOR PLAYING  !!!
        *** -------------------- ***
          
        Programmed by Bella Bradbury, 2023!
    """)
    
# RUNS GAME & END MSG
start_game()


























# PROGRAMMED BY BELLA BRADBURY