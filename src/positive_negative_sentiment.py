import curses_ui
import curses
import score_counter_system
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#----------------------------
#positive_negative_sentiment
#----------------------------

def positiveNegativeSentiment():
    """
    Evaluate the sentiment of the user's response to the recommended career and determine its positivity or negativity. It calculates the sentiment score and categorizes it as positive or negative.

    :return: A tuple containing the user's answer, sentiment (positive/negative), and the selected career.
    :rtype: Tuple[str, str, str]
    """
    nltk.download('vader_lexicon')
    
    answers = ["", "Exit Program", "Restart Program"]
    careerSelected = score_counter_system.gettingMaxScore()

    question = "How would you feel about working in a field related to " + careerSelected + "?\n"
    answer = curses.wrapper(curses_ui.selectAnswer, question, answers)
    
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(answer)
    
    if sentiment_scores['compound'] >= 0.00:
        sentiment = 'positive'
    else:
        sentiment = 'negative'        
    return answer, sentiment, careerSelected

def handlingPositiveSentiment(career):
    """
    Handle the case of a positive sentiment response.

    This function provides a response and additional resources to the user when their sentiment is
    categorized as positive regarding a career field.

    :param career: The selected career field.
    :type career: str

    :return: The user's response to the provided information, which will be used to signal if the program should restart or exit.
    :rtype: str
    """
    answerList = ["Exit Program", "Restart Program"]
    questionString = "Based on the results the career that best matches your personality and strengths is,"
    questionString2 = "\nHere are some additional resources you may find useful\n\n"
    
    content_value = curses.wrapper(curses_ui.loadingScreen, career)
    answer = curses.wrapper(curses_ui.selectAnswer, questionString + " " + career + "!" + questionString2 + str(content_value) + "\n\n", answerList)
    return answer


def handlingNegativeSentiment():
    """
    Handle the case of a negative sentiment response.

    This function provides a response to the user when their sentiment is categorized as negative,
    indicating that a career recommendation cannot be confidently made.

    :return: The user's response to the provided information, which will be used to signal if the program should restart or exit.
    :rtype: str
    """
    answerList = ["Exit Program", "Restart Program"]
    negativeQuestion = "Based on your answers, we are not able to confidently recommend you a career. We are sorry for the inconvenience.\n" 
    answer = curses.wrapper(curses_ui.selectAnswer, negativeQuestion, answerList)
    return answer