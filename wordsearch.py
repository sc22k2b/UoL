"""
Introduction to Programming: Coursework 1
Please write your name
@author: Kian Barry

"""

# Reminder: You are not allowed to import any modules.


def wordsearch(puzzle: list, wordlist: list) -> None:
    
    positions = [] #Sets a new list where the positions will be stored once returned from the get_positions function

    
    if(valid_puzzle(puzzle) is True): #Checks to see if the puzzle is valid 
        if(valid_wordlist(wordlist) is True): #Checks to see if the wordlist is valid
            for i in range (len(wordlist)): #Loops through the word list - This allows for each word to be checked (to see if it is in the puzzle) individually
                positions.append(get_positions(puzzle, wordlist[i].upper())) #Adds positions returned from the function to the positions list
            coloured_display(puzzle, positions) #Prints the puzzle out with the words that are in the puzzle with a green background
        else:
            return(print("ValueError, invalid puzzle or wordlist")) #Notifies the user that the puzzle or wordlist entered is not applicable
    else:
        return(print("ValueError, invalid puzzle or wordlist")) #Notifies the user that the puzzle or wordlist entered is not applicable


def valid_puzzle(puzzle: list) -> bool:

    for i in range(len(puzzle)-1): #Loops through the length of the puzzle -1 (As the final value will have nothing after it to be checked with therefore the loop doesnt loop through the entire length of the puzzle)
        valid = True #Sets valid to true which can be changed if there is an invalid line
        if(len(puzzle[i]) != len(puzzle[i+1])): #Checks to see if the row and the row following it are not of equal length and therefore invalid
            valid = False #Sets valid to false as rows of equal lengths have been found
            break #Stops the loop as an incorrect case has already been found 
        else:
            valid = True #Sets valid to true as there is no incorrect lengths (In the specific number of loop)
            
    if(valid is True): #Checks to see if valid has remained true
        return(True) #If valid has remained true the boolean value of True can be returned as the puzzle is correct
    else:
        return(False) #If valid does not equal true than this means there was a problem with the puzzle and therefore the boolean value of False is returned


def valid_wordlist(wordlist: list) -> bool:

    for i in range(len(wordlist)): #Loops through the wordlist
        valid = True #Sets valid to true which can be changed if an incorrect case is found
        if(isinstance(wordlist[i], str) is False): #Checks to see if the word in the wordlist at index i is not a string
            valid = False #As the word is not a string valid is set to false
            break #This exits the loop as there has been an incorrect case and therefore the wordlist needs to be rejected
        else:
            valid = True #This sets valid to true if the input was found to be a string (In the specific loop number)


    if(valid is True): #Checks to see if valid has remained true
        return(True) #Returns the boolean value True as no incorrect inputs have been found
    else:
        return(False) #Returns the boolean value False as an incorrect input has been found


def get_positions(puzzle: list, word: str) -> list:

    
    positions = []
    x = 0 #Number of correct items
    word = word.upper()
    
    for i in range(len(puzzle)): #Looping through the rows
        section = puzzle[i] #Grabs the string at that row
        
        for k in range(len(section)): #Runs through each character of the string
            section = puzzle[i] #Grabs the string at that row
            if(section[k] == word[0]): #If the starting character is found
                if(k<len(puzzle)-1):
                    if(section[k+1] == word[1]): #This has to be across
                        temp_positions = [] #Sets up a temporary list to hold the positions of correct characters
                        for c in range(len(word)): #Loops for the length of the word
                            if((k+c) < len(section)): #CHecks to see that k+c isnt beyond the length of the section and therefore the index wont be outside the amount of columns
                                if(section[k+c] == word[c]): #Checks to see if tthe next character along in the row matches the next character
                                    temp_positions.append((i,k+c)) #Adds the position to the list
                        if(len(temp_positions) == len(word)): #Checks to see if temp_positions has the same length as the word as this means that the correct positions have been found
                            positions.append(list(temp_positions)) #Copies the list into actual positions list
                
                if(k>(len(puzzle)-len(word))): #Checks to see if k is larger than the space needed to move backwards for each position of the word (So the index wont be out of range)      
                    if(section[k-1] == word[1]): #This has to be backwards
                       temp_positions = [] #Sets up a temporary list to hold the positions of correct characters
                       for c in range(len(word)): #Loops for the length of the word
                           if(section[k-c] == word[c]): #Checks to see if the character in the puzzle is eqaul to the charcater in the word going backwards
                               temp_positions.append((i,k-c)) #Adds the position to the list
                       if(len(temp_positions) == len(word)): #Checks to see if the list has the same amount of coordinates as there are characers in the word as this will mean the positions of the correct characters have beeen found
                            positions.append(list(temp_positions)) #Adds the temporary list to the actual list of correct positions
                        
            
                if(i<len(puzzle)):
                    section = puzzle[i-1]
                    x = 0
                
                        
                    if(section[k] == word[1]): #This has to be up
                        temp_positions = [] #Sets a new temporary list which will store all corresponding letters
                        for c in range(len(word)): #Loops for the length of the word
                            x = i - (1*c) #Updates the row to move it one up - So the program can look upwards for the letter
                            section = puzzle[x] #Sets the next row up as the section to be searched
                            if(section[k] == word[c]): #Checks to see if the character above the last is equal to the next character in the word
                                temp_positions.append((x,k)) #Adds the position to the temporary list
                        if(len(temp_positions) == len(word)): #If the list has the right amount of positions the program will enter this if statement
                            positions.append(list(temp_positions)) #Adds the contents of the tempP
                                
                    
                    if(section[k-1] == word[1]): #This has to be diagonal (upwards and to the left)
                        y = k - 1 #Moves the column one to the left
                        temp_positions = [] #Sets a new temporary list which will store all correct positions
                        temp_positions.append((i,k)) #Adds the first value to the list
                        for c in range(len(word)): #Loops for the length of the word
                            x = i - (1*c) #Moves the row one up - So the program can look upwards
                            if(x<len(puzzle)): #Checks to see that x hasnt exceeded the length of the puzzle
                                section = puzzle[x] #Gets the new row
                            if(section[y] == word[c]): #Checks to the line diagonal to the previous character mathches the next character in the list
                                temp_positions.append((x,y)) #Adds the position to the temporary list
                                y = y - 1 #Moves the column one to the left
                        if(len(temp_positions) == len(word)): #Checks that there is a correct number of positions meaning that the word has been found
                            positions.append(list(temp_positions)) #Adds the temporary list to the actual positions list  
                                
                    if(k<len(puzzle)-1): #Checks to see that k hasnt exceeded the length of the puzzle
                        if(section[k+1] == word[1]): #This has to be diagonal (Upwards and to the right)
                            y = k + 1 #Moves the column one across to the right
                            temp_positions = [] #Sets a new temporary list to store correct positions
                            temp_positions.append((i,k)) #Adds the first correct character position to the list
                            for c in range(len(word)): #Loops for the length of the word
                                x = i - (1*c) #Moves the row one up
                                if(x<len(puzzle)): #Checks to see that x hasnt exceed the lenght of the puzzle
                                    section = puzzle[x] #Gets the new row
                                if(section[y] == word[c]): #Checks to see if the new characters match (and are therefore correct)
                                    temp_positions.append((x,y)) #Adds the positions to the list
                                    y = y + 1 #Moves the column one space to the right
                            if(len(temp_positions) == len(word)): #Checks that there is a correct number of positions meaning that the word has been found
                                positions.append(list(temp_positions)) #Adds the temporary list to the actual positions list
                            
                if(i<len(puzzle)-1): #Checks to see that i hasnt exceed the length of the puzzle -1     
                    section = puzzle[i+1] #Moves the row one down
                    x = 0
                    y = 0
                
                    if(section[k] == word[1]): #This has to be downwards
                        temp_positions = [] #Sets a new temporary list to hold correct positions
                        for c in range(len(word)): #Loops for the length of the word
                            x = i + (1*c) #Moves the row index one downwards
                            if(x<len(puzzle)): #Checks to see x hasnt exceeded the length of the puzzle
                                section = puzzle[x] #Moves the row one downwards
                            if(section[k] == word[c]): #Checks to see if the characters are the same and therefore a potentially correct postition has been found
                                temp_positions.append((x,k)) #Adds the position to the list
                        if(len(temp_positions) == len(word)): #Checks that there is a correct number of positions meaning that the word has been found
                            positions.append(list(temp_positions)) #Adds the temporary list to the actual positions list
                                
                    
                    if(section[k-1] == word[1]): #This has to be diagonal (downwards and to the left)
                        y = k-1 #Moves the column one to the left
                        temp_positions = [] #Sets a new temporary list to hold potentially correct positions 
                        temp_positions.append((i,k)) #Adds the first correct position to the list
                        for c in range(len(word)): #Loops for the length of the word
                            x = i + (1*c) #Moves the row index one down
                            if(x<len(puzzle)): #Checks to see x hasnt exceed the length of the puzzle
                                section = puzzle[x] #Gets the new row
                            if(section[y] == word[c]): #Checks to see if the characters are the same and therefore a potentially correct position has been found
                                temp_positions.append((x,y)) #Adds the postiion to the list
                                y = y - 1 #Moves the row one to the left
                        if(len(temp_positions) == len(word)): #Checks that there is a correct number of positions meaning that the word has been found
                             positions.append(list(temp_positions)) #Adds the temporary list to the actual positions list
                                  
                    if(k<len(puzzle)-1): #Checks to see k hasnt exceeded the length of the puzzle
                        if(section[k+1] == word[1]): #This has to be diagonal (downwards and to the right)
                            if(y<len((section))): #Checks to see y hasnt exceeded the length of the section
                                y = k + 1 #Moves the column index one across
                            temp_positions = [] #Sets a new temporary list to hold the potentially correct positions
                            temp_positions.append((i,k)) #Adds the first correct position to the list
                            for c in range(len(word)): #Loops for the length of the word
                                x = i + (1*c) #Moves the row index one downwards
                                if(x<len(puzzle)): #Checks that x hasnt exceed the lenght of the puzzle
                                    section = puzzle[x] #Gets the next row
                                if(y<len(section)): #Checks to see y hasnt exceeded the amount of columns
                                    if(section[y] == word[c]): #Checks to see if the characters are the same and therefore a potentially correct position has been found
                                        temp_positions.append((x,y)) #Adds the position to the list
                                        y = y + 1 #Moves the column index one to the right
                            if(len(temp_positions) == len(word)): #Checks that there is a correct number of positions meaning that the word has been found
                                positions.append(list(temp_positions)) #Adds the temporary list to the actual positions list
                            
    if not positions: #Checks if the position list is empty meaning that the word could not be found in the list
        print(word, "not found") #Prints that the word entered couldnt be found in the puzzle
        
                      
    return(positions) #Returns the list of correct position(s)
         

def basic_display(grid: list) -> None:

    for i in range(len(grid)): #Loops for the length of the puzzle
        word = grid[i] #Takes the row at i as a string
        for k in range(len(word)): #Loops for the number of columns
            if(k == 0): #Checks to see if a character is the starting character of a row
                print("\n", word[k], end = "") #As the character is a starting character a new line will have to be printed first to display the puzzle correctly
            else: #Prints the charcter that is next in the list (Without a new line as it is not the start of a new row)
                print(" ", word[k], end = "")


def coloured_display(grid: list, positions: list) -> None:
    
    colour = False
    
    for i in range(len(grid)): #Loops for the length of the puzzle
        word = grid[i] #Takes the row at i as a string
        for k in range(len(word)):  #Loops for the length of the row
            if(k==0): #Checks to see if this is the first character in the row (As if it is a new line needs to be started)
                count_coordinates = (i,k) #Gets the coordinates of where the loop is in the puzzle
                for c in range(len(positions)): #Loops for the length of the positions list
                    positions2 = positions[c] #Gets the list for the position of one word from the larger list of all positions of all words
                    for d in range(len(positions2)): #Loops for the length of the positions2 list
                        coordinates = positions2[d] #Gets the coordinates from the list
                        for e in range(len(coordinates)): #Loops for the length of the coordinates list
                            if(coordinates[e] == count_coordinates): #Checks to see if the coordinates that we are currently at is equal to any positions that were found (As these need to be printed with a different colour background)
                                colour = True #Assings true to the colour value so when printed the program knows to print it with the green background
                                break #Breaks out the loop as there is no need to keep searching as it has already been found
                            else:
                                colour = False #Changes the colour to false if the coordinates do not correspond
                        if(colour is True): #Checks to see if the colour is true and if so the program will break out the loop as there is no need to keep searching
                            break
                    if(colour is True): #Checks to see if the colour is true and if so the program will break out the loop as there is no need to keep searching
                        break
                if(colour is True): #Checks to see if the colour is true so, it can be printed with a coloured background
                    print("\n", "\033[42m", word[k], " \033[0m", end = "") #Prints the character with a green background
                    colour = False #Changes the colour back to false so that the loop can start again without having incorrect values and characters being printed with incorrect backgrounds
                else: #Prints the character with no background as the coordinate currently being worked on in the loop does not correspond to a coordinate representing a character of a correct word
                    print("\n", word[k], end = "") 
            else:
                count_coordinates = (i,k) #Gets the coordinates currently being worked on
                for c in range(len(positions)): #Loops for length of positions
                    positions2 = positions[c] #Gets the list of positions from the larger list of all positions
                    for d in range(len(positions2)): #Loops for the length of the lists in positions2
                        coordinates = positions2[d] #Gets the list of coordinates of a single correct word
                        for e in range(len(coordinates)): #Loops for the length fo coordinates
                            if(coordinates[e] == count_coordinates): #Checks to see if a coordinate in the list is equal to the coordinate currently being looked at
                                colour = True #Sets the colour to true to indicate that this specific coordinate is apart of a correct word and therefore needs to be printed with a coloured background
                                break #Breaks out the loop as there is no longer a need to look at the other coordinates as the correct one has already ben found
                            else:
                                colour = False
                        if(colour is True): #Checks to see if the colour is true and if so the program will break out the loop as there is no need to keep searching
                            break
                    if(colour is True): #Checks to see if the colour is true and if so the program will break out the loop as there is no need to keep searching
                        break
                if(colour is True): #Prints the character with a coloured background if it has a coordinate that is apart of the coordinates of correct words
                    print(" ", "\033[42m", word[k], " \033[0m", end = "") 
                    colour = False #Resets colour so no other values are printed with a coloured background unless they are correct again
                else: #Prints the character without a coloured background if the coordinate did not equal a correct coordinate and therefore the position does not belong to a correct character
                    print(" ", word[k], end = "")
                    
    
   
    

# =============================================================================
# Do not remove the followings. To test your functions
# =============================================================================


def test_valid_wordlist():
    """
    Test function valid_wordlist()
    """
    good_wordlist = ["scalar", "tray", "blew", "sevruc", "testing"]
    good_wordlist2 = ["scalar", "tray", "blew", "sevruc"]
    bad_wordlist2 = ["scalar", "tray", "blew", "sevruc", 59]

    print("wordlist is", valid_wordlist(good_wordlist))
    print("wordlist is", valid_wordlist(good_wordlist2))
    print("wordlist is", valid_wordlist(bad_wordlist2))


def test_valid_puzzle():
    good_puzzle = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
                   'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
                   'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    bad_puzzle1 = ['RUNAROUNDDL', 'EDCITOAHC', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
                   'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
                   'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    bad_puzzle2 = ['RUNAROUNDDL', ['EDCITOAHCYV'], ('ZYUWSWEDZYA'),
                   'AKOTCONVOYV', 'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL',
                   'ISTREWZLCGY', 'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    print("puzzle is", valid_puzzle(good_puzzle))
    print("puzzle is", valid_puzzle(bad_puzzle1))
    print("puzzle is", valid_puzzle(bad_puzzle2))


def test_basic_display():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    basic_display(puzzle1)
    basic_display([['a', 'b', 'c', 'd', 'e'], ['h', 'l', 'j', 'k', 'l']])


def test_get_positions():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    get_positions(puzzle1, "TESTING")
    print(get_positions(puzzle1, "tray"))


def test_coloured_display():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    good_wordlist2 = ["scalar", "TRAY", "BLEW", "SEVRUC"]
    final_list = []
    for word in good_wordlist2:
        temp = get_positions(puzzle1, word)
        if temp is not None:
            final_list.append(temp)
    coloured_display(puzzle1, final_list)


def test_wordsearch():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    good_wordlist2 = ["scalar", "tray", "blew", "sevruc"]
    wordsearch(puzzle1, good_wordlist2)


if __name__ == "__main__":
    # uncomment the test function individually
    # basic solution
    # test_valid_puzzle()
    # test_valid_wordlist()
    # test_basic_display()

    # full solution
    # test_coloured_display()
    # test_get_positions()
    test_wordsearch()