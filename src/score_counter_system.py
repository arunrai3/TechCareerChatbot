
#-----------------
#score_counter
#-----------------

def countingSystem(answer, answersList):
    """
    Update career choice counters based on the selected answer.

    This function updates counters for different career choices based on the user's answer to a career-related question.

    :param answer: The user's answer, representing a career choice.
    :type answer: str
    :param answersList: The list of available career choices.
    :type answersList: List[str]

    :return: None
    :rtype: None
    """
    global frontEndCounter, computerArchCounter, cyberCounter, dataEngineerCounter, projectManagerCounter
    if answer == answersList[0]:
      frontEndCounter += 1
    elif answer == answersList[1]:
      computerArchCounter += 1
    elif answer == answersList[2]:
      cyberCounter += 1
    elif answer == answersList[3]:
      dataEngineerCounter += 1
    elif answer == answersList[4]:
      projectManagerCounter += 1

def resetCounters():
    """
    Reset career choice counters to zero when user selects "Restart Program".

    This function resets the counters for different career choices to zero, preparing them for a new round of career assessment.

    :return: None
    :rtype: None
    """
    global frontEndCounter, computerArchCounter, cyberCounter, dataEngineerCounter, projectManagerCounter
    frontEndCounter = 0
    computerArchCounter = 0 
    cyberCounter = 0
    dataEngineerCounter = 0 
    projectManagerCounter = 0

def gettingMaxScore():
    """
    Determine the career choice with the highest score at the end of the assessment.

    This function calculates the career choice with the highest score based on the counters for different career choices.

    :return: The career choice with the highest score.
    :rtype: str
    """
    global frontEndCounter, computerArchCounter, cyberCounter, dataEngineerCounter, projectManagerCounter
    if frontEndCounter == max(frontEndCounter, computerArchCounter, cyberCounter, dataEngineerCounter, projectManagerCounter):
        careerSelected = "Front-End Development"
    elif computerArchCounter == max(frontEndCounter, computerArchCounter, cyberCounter, dataEngineerCounter, projectManagerCounter):
        careerSelected = "Computer Architecture"
    elif cyberCounter == max(frontEndCounter, computerArchCounter, cyberCounter, dataEngineerCounter, projectManagerCounter):
        careerSelected = "Cybersecurity"
    elif dataEngineerCounter == max(frontEndCounter, computerArchCounter, cyberCounter, dataEngineerCounter, projectManagerCounter):
        careerSelected = "Data Engineering and Data Science"
    elif projectManagerCounter == max(frontEndCounter, computerArchCounter, cyberCounter, dataEngineerCounter, projectManagerCounter):
        careerSelected = "Project Management"
    return careerSelected