from utils.ReinforcementAlgorithm import ReinforcementAlgo
from pathlib import Path
from ast import literal_eval
from time import sleep


# This is the runnable program
if __name__ == '__main__':

    # intro
    print('''
          
          ReinforcementAlgorithm \n
          ''')
    sleep(1.3)
    print('''
          by Code7G
          \n
          ''')
    sleep(1)

    # Seting all new game options or reading all previous game options with the use of the All_options.txt file
    all_options_file = Path('All_options.txt')
    if all_options_file.exists():
        all_options = all_options_file.read_text()
        all_options = literal_eval(all_options)

        print(f'All previous options = {all_options}')

        algo = ReinforcementAlgo(all_options)
        algo.play()
    else:
        all_options = input(
            '''To start the program for the first time you will need to configure all the possible moves in a game
          Plese enter all possible game options (> example example example) > ''')

        all_options = all_options.split(' ')
        all_options_file.write_text(str(all_options))
        print(
            f'\n All optons were saved in file All_options.txt at {all_options_file.absolute()}')
        print('''
              Do not modify/delete or change the location of this file, because it could result in an error,
              
              ONLY delete the file if you want to reset all the game options,
              and change the file if you want to change all the game options \n
              ''')
        algo = ReinforcementAlgo(all_options)
        algo.play()

# The main function for using the ReinforcementAlgo class is the play() function
# The class has multiple functions which can be used separately,
# I highly encourage you to use the other functions of the ReinforcementAlgo class in your own applications
