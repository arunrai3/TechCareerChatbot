import curses_ui
import curses
import score_counter_system

#---------------------
#question_generator
#---------------------

def questionGenerator(question, answers):
    """
    
    This function presents a question as well as multiple choice options to select from that help user select a career in tech.
    
    :param question (str): Question that is displayed to the user.
    :param answers (list): A list of strings that the user can select from.    
    
    :return: The user's answer from the multiple choice option.
    :rtype: str            
        
    """
    answer = curses.wrapper(curses_ui.selectAnswer, question, answers)
    score_counter_system.countingSystem(answer, answers)
    return answer