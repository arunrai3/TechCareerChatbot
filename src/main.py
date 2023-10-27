import sys
import introductions
import strengths_weaknesses
import score_counter_system
import question_generator
import positive_negative_sentiment

#----------------
#main
#----------------

condition_to_exit = False
score_counter_system.resetCounters()
questions = [
    ("1. Which class did you enjoy the most in your Undergraduate Computer Science Program?\n", ["Software 1 and/or 2", "Computer Architecture", "Fundamentals of Information Security", "Data Structures and Algorithms 1 and/or 2", "Business of IT - Project Management", "Exit Program", "Restart program"]),
    ("2. What kind of impact do you aspire to make in the technology industry?\n", ["Designing a very appealing and user-friendly front-end", "Working on computer hardware to handle software demands", "Protecting customer and business data", "Creating the most efficient software that is fast and responsive for users", "Leading a team of developers to meet consumer demand", "Exit Program", "Restart program"]),
    ("3. Which class did you receive the best grade in your Undergraduate Computer Science Program (if two or more classes received the same grade, select which one naturally came most easy to you):\n", ["Software 1 and/or 2", "Computer Architecture", "Fundamentals of Information Security", "Data Structures and Algorithms 1 and/or 2", "Business of IT - Project Management", "Exit Program", "Restart program"]),
    ("4. What type of projects excite you the most?\n", ["Developing visually stunning websites or applications.", "Building complex computer systems and networks.", "Conducting security audits and penetration testing.", "Working with large datasets and implementing data pipelines.", "Leading cross-functional teams and delivering successful projects.", "Exit Program", "Restart program"]),
    ("5. Which career path aligns with your long-term goals?\n", ["Becoming a full-stack web developer or UI/UX designer.", "Advancing into system architecture or infrastructure management.", "Specializing in cybersecurity or information security management.", "Pursuing a career in data engineering or data science.", "Transitioning into project management or team leadership roles.", "Exit Program", "Restart program"]),
    ("6. What kind of problems do you enjoy solving?\n", ["Design challenges and user experience optimization.", "System performance tuning and optimization.", "Identifying and mitigating potential cybersecurity threats.", "Developing efficient algorithms for data processing.", "Overcoming project constraints and achieving goals within deadlines.", "Exit Program", "Restart program"]),
    ("7. Which skills do you value the most?\n", ["Proficiency in HTML, CSS, and JavaScript.", "In-depth knowledge of computer architecture and system design.", "Expertise in network security and vulnerability assessment.", "Strong programming skills in languages like Python or Java.", "Excellent communication and project management abilities.", "Exit Program", "Restart program"]),
    ("8. What excites you about the future of technology?\n", ["The endless possibilities to create intuitive and immersive experiences.", "The advancements in computer systems and artificial intelligence.", "The constant battle against evolving cyber threats and vulnerabilities.", "The transformative power of data-driven decision-making.", "The increasing demand for effective project management and leadership.", "Exit Program", "Restart program"]),
    ("9. What kind of work environment do you prefer?\n", ["Creative and visually appealing", "Technical and logical", "Highly secure and focused on risk mitigation", "Data-driven and analytical", "Dynamic and collaborative", "Exit Program", "Restart program"]),
    ("10. Which area of technology interests you the most?\n", ["Web development and front-end technologies.", "Computer hardware and system architecture.", "Network security and ethical hacking.", "Data analysis and database management.", "Project planning and management.", "Exit Program", "Restart program"]),
    ("11. Which role in a team do you find most appealing?\n", ["Front-end developer or user interface designer.", "Computer architect or systems engineer.", "Cybersecurity specialist or ethical hacker.", "Data engineer or database administrator.", "Project manager or team leader.", "Exit Program", "Restart program"])
]


while True:
  answer1 = introductions.introduction()
  if answer1 == "Yes":
    answer2 = introductions.introduction2()
    if answer2 == "Start":
      strengthWords = strengths_weaknesses.strengths()
      if strengthWords == "Exit Program":
        condition_to_exit = True
      elif strengthWords == "Restart Program":
        score_counter_system.resetCounters()
      else:
        weakWords = strengths_weaknesses.weaknesses()
        if weakWords == "Exit Program":
          condition_to_exit = True
        elif weakWords == "Restart Program":
          score_counter_system.resetCounters()
        else:
          for question, answers in questions:
            answer = question_generator.questionGenerator(question, answers)
            if answer == "Exit Program":
              condition_to_exit = True
              break
            elif answer == "Restart program":           
              score_counter_system.resetCounters()
              break
            elif question == "11. Which role in a team do you find most appealing?\n":
              answerFromSentiment, positiveOrNegative, career = positive_negative_sentiment.positiveNegativeSentiment()
              if answerFromSentiment == "Exit Program":
                condition_to_exit = True
                break
              elif answerFromSentiment == "Restart Program":
                score_counter_system.resetCounters()
                break
              elif positiveOrNegative == "positive":
                resultAnswer = positive_negative_sentiment.handlingPositiveSentiment(career)
                if resultAnswer == "Exit Program":
                  condition_to_exit = True
                  break
                elif resultAnswer == "Restart Program":
                  score_counter_system.resetCounters()
                  break            
              elif positiveOrNegative == "negative":
                negativeResponse = positive_negative_sentiment.handlingNegativeSentiment()
                if negativeResponse == "Exit Program":
                  condition_to_exit = True
                  break
                elif negativeResponse == "Restart Program":
                  score_counter_system.resetCounters()
                  break            
            
    else:
      condition_to_exit = True
  else:
    condition_to_exit = True

  if condition_to_exit:
    break
  else:
    score_counter_system.resetCounters()

sys.exit()