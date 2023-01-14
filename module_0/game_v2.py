"""Number guessing game.
In this game, the computer thinks of a random number between 1 and 100.
The computer then guesses the number.
"""

import numpy as np


def bisection_predict(number: int = 1) -> int:
    """guess the number using dichotomy

    Args:
        number (int, optional): Hidden number. Defaults to 1.

    Returns:
        int: Number of attempts
    """
    count = 0
    up_boarder = 101
    down_boarder = 1
     
    while True:
        count += 1
        # estimated number
        predict_number = int(np.median(range(down_boarder,up_boarder)))
        
        if number > predict_number:
            down_boarder = predict_number + 1            
        elif number < predict_number:  
            up_boarder = predict_number  
        elif number == predict_number:
            break  # exit from the loop if guessed right

    return count


def threesection_predict(number: int = 1) -> int:
    '''The number of predictions is taken into account arbitrarily.
       The search diapason is divided by three. 
       The algorithm checks in what range the hidden number is.
       Then the prediction number is set as the average of the diapason.
       The search diapason is divided by three, and so on. 
       
    Args:
        number (int, optional): Hidden number. Defaults to 1.
        
    Returns:
        int: Number of attempts
    '''
    count=1
    top = 101
    bottom = 0
    predict = np.random.randint(1,101)
    while number != predict:        
        count+=1
        diapason = top - bottom
        if number in range(bottom, diapason//3 + bottom): 
            top = diapason//3 + bottom             
        elif number in range(diapason//3 + bottom, diapason//3*2 + bottom): 
            top = diapason//3*2 + bottom
            bottom = diapason//3 + bottom             
        else:
            bottom = diapason//3*2 + bottom
        predict = (top - bottom)//2 + bottom
    
    return(count) # Exit from the cycle, if guess right.


def tensection_predict(number: int = 1) -> int: # cheating version
    '''The number of predictions is taken into account arbitrarily.
       The search diapason is divided by ten. 
       The algorithm checks in what range the hidden number is.
       Then the prediction number is set as at least of the diapason.
       The search diapason is divided by ten, and so on.
       
    Args:
        number (int, optional): Hidden number. Defaults to 1.
        
    Returns:
        int: Number of attempts
    '''
    count=1
    top = 101
    bottom = 1
    predict = np.random.randint(1,101)
    while number != predict:        
        count+=1
        diapason = top - bottom
        if number in range(bottom, diapason//10 + bottom): 
            top = diapason//10 + bottom             
        elif number in range(diapason//10 + bottom, diapason//10*2 + bottom):
            top = diapason//10*2 + bottom
            bottom = diapason//10 + bottom
        elif number in range(diapason//10*2 + bottom, diapason//10*3 + bottom):
            top = diapason//10*3 + bottom
            bottom = diapason//10*2 + bottom
        elif number in range(diapason//10*3 + bottom, diapason//10*4 + bottom):
            top = diapason//10*4 + bottom
            bottom = diapason//10*3 + bottom
        elif number in range(diapason//10*4 + bottom, diapason//10*5 + bottom):
            top = diapason//10*5 + bottom
            bottom = diapason//10*4 + bottom 
        elif number in range(diapason//10*5 + bottom, diapason//10*6 + bottom): 
            top = diapason//10*6 + bottom
            bottom = diapason//10*5 + bottom
        elif number in range(diapason//10*6 + bottom, diapason//10*7 + bottom): 
            top = diapason//10*7 + bottom
            bottom = diapason//10*6 + bottom
        elif number in range(diapason//10*7 + bottom, diapason//10*8 + bottom): 
            top = diapason//10*8 + bottom
            bottom = diapason//10*7 + bottom
        elif number in range(diapason//10*8 + bottom, diapason//10*9 + bottom): 
            top = diapason//10*9 + bottom
            bottom = diapason//10*8 + bottom
        else:
            bottom = diapason//10*9 + bottom
        predict = bottom
    
    return(count) # Exit from the cycle, if guess right.


def score_game(guess_func) -> int:
    """For how many attempts on average for 1000 approaches our algorithm guesses

    Args:
        rguess_func ([type]): guess function

    Returns:
        int: average number of tries
    """
    count_ls = []
    np.random.seed(42)  # fix seed for reproducibility
    random_array = np.random.randint(1, 101, size=(1000)) # made a list of numbers
    
    for number in random_array:
        count_ls.append(guess_func(number))

    score = int(np.mean(count_ls))
    print(f"Your algorithm guesses the number on average in: {score} tries")
    return score


if __name__ == "__main__":
    # RUN
    score_game(bisection_predict)
    score_game(threesection_predict)
    score_game(tensection_predict)