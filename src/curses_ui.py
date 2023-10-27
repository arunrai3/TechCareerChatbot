import curses
import resources_from_chatgpt

#------------------
#curses_ui
#------------------

def selectAnswer(stdscr, question, answers):
    """
    Display a question and multiple-choice answers to the user as well as handling custom user input.


    :param stdscr(curses.window): The main curses window.
    :param question (str): The question to display to the user.
    :param answers (list): A list of possible multiple-choice answers.

    :return: The area of the rectangle.
    :rtype: float


    Note: The function uses the curses library for text-based user interface.

    """
    curses.curs_set(0)  
    stdscr.clear()

    selected_item = 0
    top_item = 0
    max_visible_items = curses.LINES - 2  

    user_input = ""  

    while True:
        stdscr.clear()

        stdscr.addstr(question)

        for i in range(top_item, min(top_item + max_visible_items, len(answers))):
            item = answers[i]
            if i == selected_item:
                if question == "What are your strengths and areas of expertise, in the field of technology and computer science?\n" or question == "What are your weaknesses and areas you need improvement, in the field of technology and computer science?\n" or "How would you feel" in question:
                  if i == top_item:  
                      stdscr.addstr(f"> {user_input}\n", curses.A_BOLD)
                  else:
                      stdscr.addstr(f"> {item}\n", curses.A_BOLD)
                else:
                   stdscr.addstr(f"> {item}\n", curses.A_BOLD)
            else:
                if question == "What are your strengths and areas of expertise, in the field of technology and computer science?\n" or question == "What are your weaknesses and areas you need improvement, in the field of technology and computer science?\n" or "How would you feel" in question:
                  if i == top_item:  
                      stdscr.addstr(f"> {user_input}\n")
                  else:
                      stdscr.addstr(f"> {item}\n")
                else:
                  stdscr.addstr(f"  {item}\n")

                
        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP:
            selected_item = max(selected_item - 1, 0)
            if selected_item < top_item:
                top_item = selected_item
        elif key == curses.KEY_DOWN:
            selected_item = min(selected_item + 1, len(answers) - 1)
            if selected_item >= top_item + max_visible_items:
                top_item = selected_item - max_visible_items + 1
        elif key == curses.KEY_BACKSPACE or key == 8:  
            user_input = user_input[:-1]
        elif key == 10:  
            if question == "What are your strengths and areas of expertise, in the field of technology and computer science?\n" or question == "What are your weaknesses and areas you need improvement, in the field of technology and computer science?\n" or "How would you feel" in question:
              if selected_item == top_item:                  
                  return user_input
              else:
                  return answers[selected_item]
            else:
              return answers[selected_item]

        else:
            if selected_item == top_item:                
                user_input += chr(key)
    
def loadingScreen(stdscr, career):
    """
    Display a loading screen and fetch resources from the ChatGPT API. The `career` parameter specifies the user's career for resource retrieval, and the fetched content is returned.

    :param stdscr (curses.window): The main curses window.
    :param career (str): The user's career that ChatGPT will fetch resources for.

    :return: Fetched content from the ChatGPT API.
    :rtype: str        
        
    """
    curses.curs_set(0)  

    selected_item = 0
    top_item = 0
    max_visible_items = curses.LINES - 2  

    stdscr.clear()
    stdscr.addstr("Loading...")
    stdscr.refresh()

    resources = resources_from_chatgpt.resourcesAtTheEnd(career)
    content_value = resources["content"]
    return content_value