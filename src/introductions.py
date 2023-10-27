import curses_ui
import curses

#--------------------
#introductions
#--------------------

def introduction():
    """

    This function presents an introductory message to the user and asks if they are interested
    in finding a career that matches their personality and strengths.

    :return: The user's response, which can be "Yes" to proceed with program or "Exit Program" to exit the program.
    :rtype: str          
        
    """
    introduction = "Hello! My name is Chat! I am here to help upcoming Computer Science graduates find a carrer that fits their personality and strengths. Does this sound like somthing your interested in?\n"
    answerList = ["Yes", "Exit Program"]
    answer = curses.wrapper(curses_ui.selectAnswer, introduction, answerList)
    return answer
    
def introduction2():
    """
    Display a second introduction message as confirmation and prompt the user to start or exit program.

    :return: The user's response, which can be "Start" to begin program or "Exit Program" to exit program.
    :rtype: str         
        
    """
    introduction2 = "Great! Lets get started, I am going to ask you multiple questions, answer them to the best of your ability. At the end I will shares the results!\n"
    answerList = ["Start","Exit Program"]
    answer = curses.wrapper(curses_ui.selectAnswer, introduction2, answerList)
    return answer   