from random import randrange
from pathlib import Path
from ast import literal_eval


# Reinforcement Learning Algorithm
class ReinforcementAlgo:
    '''
    The Reinforcement Learning Algorithm class
    '''

    # Suplying all of the possible game options
    def __init__(self, options):
        self.options = options

    # Main function for the use of this algorithm by terminal and files
    def play(self):
        '''
        The main function for using the reinforcement learning algorithm
        '''

        # info
        print('''
For input, you will be asked "All current game options: ", for this type all the CURRENT POSSIBLE game options,
but when the game ends,
you will need to type LOSS/DRAW/WIN (to "All current game options: ") as a result of the game
after setting the result of the game, you will be asked if you want to save the knowledge and end the program.

IMPORTANT:
Don't modify/delete or change the location of the Knowledge.txt file, the file is only safe to look at,
you are free to delete the Knowledge.txt file ONLY if you want to reset the option values \n''')

        history_of_actions = []
        saved_history_of_actions = {}

        save_file = Path('Knowledge.txt')

        if save_file.exists():

            # Reading previous option values from the Knowledge.txt file
            option_values = self.read_previous_ov(save_file)

            # More games loop
            count = 0
            while True:

                # Setting the current game options
                input_options = input(
                    'All current game options (example: option option option): ')
                current_options = input_options.split(' ')

                if 'LOSS' in current_options or 'DRAW' in current_options or 'WIN' in current_options:

                    # Checking if the game was valid
                    if len(history_of_actions.copy()) == 0:
                        print('A game with no action is invalid')
                        print('Try again')

                    else:
                        # Updating option values using game results, saving the game results and saving updated option values
                        count += 1
                        result = current_options.copy()
                        actions = history_of_actions.copy()
                        saved_history_of_actions[count] = actions, result
                        option_values = self.consistant_learning(
                            result, history_of_actions, option_values)
                        print(f'Updated option values: {option_values}')
                        history_of_actions.clear()

                        usr_choice = input(
                            'Do you want to end the program? (Y/n) ')

                        if usr_choice.upper() == 'Y':

                            # Save the knowledge
                            print('Saving learned knowledge..')

                            text = save_file.read_text()
                            for game in saved_history_of_actions:
                                text += 'Game ' + \
                                    str(game) + ' = ' + \
                                    str(saved_history_of_actions.get(
                                        game)) + '.\n'
                            text += 'The option values of games is = ' + \
                                str(option_values) + '\n' + '\n'

                            save_file.write_text(text)

                            # End the program
                            print('Program ended')
                            break
                else:

                    # Choosing the best option from the option values
                    option = self.choose_option(option_values, current_options)

                    # Restart the game if the option is invalid
                    if option == 'END':
                        end_program = input('''
Are you sure you want to end the program now? (Your games and option values will not be saved,
try doing this after finishing a game with a result)
(Y/n)? ''')
                        if end_program.upper() == 'Y':
                            print('Program ended without saving progress')
                            return 'Program ended without save'

                        else:
                            pass

                    elif 'ERROR: Option not in options' in option:
                        print('Invalid Option')
                        print('Try again')

                    else:
                        print(f'Choosen option = {option}')
                        history_of_actions.append(option)

        else:

            # Firs game
            end = 0
            count = 1
            while True:

                # Setting the current game options
                input_options = input(
                    'All current game options (example: option option option): ')
                current_options = input_options.split(' ')

                if 'LOSS' in current_options or 'DRAW' in current_options or 'WIN' in current_options:

                    # Checking if the game was valid
                    if len(history_of_actions.copy()) == 0:
                        print('A game with no action is invalid')
                        print('Try again')

                    else:
                        # Creating the first option values using game results, saving the game results and saving new option values
                        result = current_options.copy()
                        actions = history_of_actions.copy()
                        saved_history_of_actions[count] = actions, result
                        option_values = self.learning(
                            result, history_of_actions)
                        print(f'Updated option values: {option_values}')
                        history_of_actions.clear()

                        usr_choice = input(
                            'Do you want to end the program? (Y/n) ')

                        if usr_choice.upper() == 'Y':

                            # Save the knowledge
                            print('Saving learned knowledge..')

                            text = ''
                            for game in saved_history_of_actions:
                                text += 'Game ' + \
                                    str(game) + ' = ' + \
                                    str(saved_history_of_actions.get(
                                        game)) + '.\n'
                            text += 'The option values of games is = ' + \
                                str(option_values) + '\n' + '\n'

                            save_file.write_text(text)

                            # End the program
                            print('Program ended')
                            end += 1
                            break

                else:
                    # Choosing a random option because there are no option values yet
                    option = self.first_learning(current_options)

                    # Restart the game if the option is invalid
                    if option == 'END':
                        end_program = input('''
Are you sure you want to end the program now?
(Y/n)? ''')
                        if end_program.upper() == 'Y':
                            print('Program ended')
                            return 'Program ended'

                        else:
                            pass

                    elif option == 'Option Invalid':
                        print('Try again')

                    else:
                        print(f'Choosen option = {option}')
                        history_of_actions.append(option)

            if end >= 1:
                return ''

            # More games loop
            while True:

                # Setting the current game options
                input_options = input(
                    'All current game options (example: option option option): ')
                current_options = input_options.split(' ')

                if 'LOSS' in current_options or 'DRAW' in current_options or 'WIN' in current_options:

                    # Checking if the game was valid
                    if len(history_of_actions.copy()) == 0:
                        print('A game with no action is invalid')
                        print('Try again')

                    else:
                        # Updating option values using game results, saving the game results and saving updated option values
                        count += 1
                        result = current_options.copy()
                        actions = history_of_actions.copy()
                        saved_history_of_actions[count] = actions, result
                        option_values = self.consistant_learning(
                            result, history_of_actions, option_values)
                        print(f'Updated option values: {option_values}')
                        history_of_actions.clear()

                        usr_choice = input(
                            'Do you want to end the program? (Y/n) ')

                        if usr_choice.upper() == 'Y':

                            # Save the knowledge
                            print('Saving learned knowledge..')

                            text = ''
                            for game in saved_history_of_actions:
                                text += 'Game ' + \
                                    str(game) + ' = ' + \
                                    str(saved_history_of_actions.get(
                                        game)) + '.\n'
                            text += 'The option values of games is = ' + \
                                str(option_values) + '\n' + '\n'

                            save_file.write_text(text)

                            # Ending the program
                            print('Program ended')
                            break

                else:
                    # Choosing the best option from the option values
                    option = self.choose_option(option_values, current_options)

                    # Restarting the game if the option is invalid
                    if option == 'END':
                        end_program = input('''
Are you sure you want to end the program now? (Your games and option values will not be saved,
try doing this after finishing a game with a result)
(Y/n)? ''')
                        if end_program.upper() == 'Y':
                            print('Program ended without saving progress')
                            return 'Program ended without save'

                        else:
                            pass

                    elif 'ERROR: Option not in options' in option:
                        print('Invalid Option')
                        print('Try again')

                    else:
                        print(f'Choosen option = {option}')
                        history_of_actions.append(option)

    def read_previous_ov(self, path: Path):
        '''
        Read the previous option values from a given path containing a .txt file

        The previous options values in the file must be stored as a dictionary:
        Example: {g1: 1000003, g2: 999998}
        '''

        print('Reading previous knowledge')

        # Setting previous option values
        option_values_options = []

        previous_data = path.read_text()

        # Spliting and changing the data
        first_split_data = previous_data.split('{')
        splited_data = []
        [splited_data.append(f_data.split('}'))
            for f_data in first_split_data]

        strsplit = str(splited_data)
        a = strsplit.replace('[', '')
        b = a.replace(']', '')
        c = b.replace('"', '')
        splited_data = c.split(',')

        for data in splited_data:
            if ':' in data:
                option_values_options.append(data)

            else:
                pass

        print('Values identified..')
        option_values_options = str(option_values_options)
        a = option_values_options.replace('[', '{')
        b = a.replace(']', '}')
        almost_finished_dict = b.replace('"', '')

        # Converting the dict data to a dict
        option_values = literal_eval(almost_finished_dict)

        print(f'Previous data: {option_values}')
        return option_values

    def first_learning(self, current_options: list):
        '''
        Pick a valid random option from all the current options
        '''

        # Checking if the option is valid
        for option in current_options:
            if option == 'END':
                return 'END'

            elif option in self.options:
                pass

            else:
                print('Invalid Option')
                return 'Option Invalid'

        # Picking a random option
        randindex = randrange(0, len(current_options))
        return current_options[randindex]

    def learning(self, result: list, history_of_actions: list):  # action = used option
        '''
        Create the first option values and update the option values according to the result of the previous game

        If the result of the previous game was:
        WIN = option value +2
        DRAW = option value +1
        LOSS = option value -2
        '''

        # Defie new option values
        option_values = {}
        for option in self.options:
            option_values[option] = option_values.get(option, 1000000)

        # Make the necessary changes to the values by the result
        if 'WIN' in result:
            for option in history_of_actions:
                option_values[option] = option_values.get(option, 1000000) + 2

        elif 'DRAW' in result:
            for option in history_of_actions:
                option_values[option] = option_values.get(option, 1000000) + 1

        elif 'LOSS' in result:
            for option in history_of_actions:
                option_values[option] = option_values.get(option, 1000000) - 1

        else:
            pass

        return option_values

    def consistant_learning(self, result: list, history_of_actions: list, option_values: dict):
        '''
        Update the option values according to the result of the previous game

        If the result of the previous game was:
        WIN = option value +2
        DRAW = option value +1
        LOSS = option value -2
        '''

        # Defie new and existing option values
        for option in self.options:
            option_values[option] = option_values.get(option)

        # Make the necessary changes to the values by the result
        if 'WIN' in result:
            for option in history_of_actions:
                option_values[option] = option_values.get(option) + 2

        elif 'DRAW' in result:
            for option in history_of_actions:
                option_values[option] = option_values.get(option) + 1

        elif 'LOSS' in result:
            for option in history_of_actions:
                option_values[option] = option_values.get(option) - 1

        else:
            pass

        return option_values

    def choose_option(self, option_values: dict, current_options: list):
        '''
        Choose the option from all the current options that have the highest option value,
        if there are options with the same highest option value, one of them will be randomly picked
        '''

        # Choose the options with the highest values
        max = 0

        # Getting highest option value
        for option in current_options:
            if 'END' in option:
                return 'END'

            elif option in option_values:
                value = option_values.get(option)

                if value > max:
                    max = value

                else:
                    pass

            else:
                print('Option is not in all options')
                return 'ERROR: Option not in options'

        # Setting high-value options
        best_options = []
        for option in current_options:
            if option_values.get(option) == max:
                best_options.append(option)

            else:
                pass

        # Picking the option/s
        if len(best_options) > 1:
            randindex = randrange(0, len(best_options))
            return best_options[randindex]

        else:
            return best_options[0]

# The main function for using the ReinforcementAlgo class is the play() function
# The class has multiple functions which can be used separately,
# I highly encourage you to use the other functions of the ReinforcementAlgo class in your own applications
