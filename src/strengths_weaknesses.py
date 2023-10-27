import nltk
import curses_ui
import curses
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#-----------------------
#strengths_weaknesses
#-----------------------

def nlprimaryWords(text):
    """
    Tokenize and filter stop words from a given text.

    This function tokenizes the input text and filters out common English stop words, returning a list of filtered words.

    :param text: The text to be tokenized and filtered.
    :type text: str

    :return: A list of filtered words from the input text.
    :rtype: List[str]
    """
    nltk.download('stopwords')
    words = word_tokenize(text)
    stop_words = set(stopwords.words('english'))    
    filtered_words = [word for word in words if word.lower() not in stop_words]    
    return filtered_words

def strengths():
    """
    Gather user's strengths and areas of expertise in technology and computer science.

    This function prompts the user to provide information about their strengths and areas of expertise in the field of technology and computer science.

    :return: A list of the user's strengths and areas of expertise.
    :rtype: List[str]
    """
    strength = "What are your strengths and areas of expertise, in the field of technology and computer science?\n"
    answers = ["", "Exit Program", "Restart Program"]
    nlpStrengthwords = curses.wrapper(curses_ui.selectAnswer, strength, answers)
    if nlpStrengthwords == "Exit Program" or nlpStrengthwords == "Restart Program":
      return nlpStrengthwords
    else:
      nlprimaryStrengthwords = nlprimaryWords(nlpStrengthwords)
      return nlprimaryStrengthwords

def weaknesses():
    """
    Gather user's weaknesses and areas in need of improvement in technology and computer science.

    This function prompts the user to provide information about their weaknesses and areas in need of improvement in the field of technology and computer science.

    :return: A list of the user's weaknesses and areas in need of improvement.
    :rtype: List[str]
    :return: If user chooses to exit the program, they can select 'Exit Program' or 'Restart Program' and that will be returned to indicate what the program should do next.
    :rtype: str    
    """    
    weakness = "What are your weaknesses and areas you need improvement, in the field of technology and computer science?\n"
    answers = ["", "Exit Program", "Restart Program"]
    nlpWeakwords = curses.wrapper(curses_ui.selectAnswer, weakness, answers)
    if nlpWeakwords == "Exit Program" or nlpWeakwords == "Restart Program":
      return nlpWeakwords
    else:
      nlprimaryWeakwords = nlprimaryWords(nlpWeakwords)
      return nlprimaryWeakwords