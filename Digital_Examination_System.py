print("Instructions:")
print("\n1) This test consists of 2 parts MCQS and Subjective.")
print("\n2) Each MCQ is of 1 mark and each subjective question is of 2.5 marks.")
print("\n3) There will be no negative marking for incorrect MCQS.")
print("\n4) If any candidate is found using unfair means, they will be disqualified from the examination and strict disciplinary action will be taken. \n")

MCQ_SCORE = 0


MCQ_Questions = ['''Who is the father of Computers?
a) James Gosling
b) Charles Babbage
c) Dennis Ritchie
d) Bjarne Stroustrup''', 

'''\nWhich of the following is the correct abbreviation of COMPUTER?
a) Commonly Occupied Machines Used in Technical and Educational Research
b) Commonly Operated Machines Used in Technical and Environmental Research
c) Commonly Oriented Machines Used in Technical and Educational Research
d) Commonly Operated Machines Used in Technical and Educational Research''',

'''\nWhich of the following language does the computer understand?
a) Computer understands only C Language
b) Computer understands only Assembly Language
c) Computer understands only Binary Language
d) Computer understands only BASIC''', 

'''\nWhich of the following computer language is written in binary codes only?
a) pascal
b) machine language
c) C
d) C#''',

'''\nWhich of the following is the smallest unit of data in a computer?
a) Bit
b) KB
c) Nibble
d) Byte'''
]

MCQ_Answers = ["b", "d", "c", "b", "a"]
Maximum_MCQ = len(MCQ_Questions)

Subjective_Score = 0.0

Subjective_Questions = ["Differentiate between Primary Memory and Secondary Memory.",
                        "What is Cache Memory, and why is it crucial for system performance?",
                        "Define an Operating System (OS) and list its primary functions.",
                        "What is the difference between a LAN, MAN, and WAN",
                        "How does a computer store and process data using the Binary System?"]

Subjective_Answer = []
Maximum_Subjective = len(Subjective_Questions)*2.5

def MCQS():
    print("Section A - MCQS")
    global MCQ_SCORE    

    Wrong_question = []
    Wrong_Answer = []

    for i in range(len(MCQ_Questions)):
        print(MCQ_Questions[i])
        b = input("Enter option: ")
        if b.upper() == MCQ_Answers[i].upper():
            print("Correct")
            MCQ_SCORE += 1
        else: 
            print("Incorrect")
            Wrong_question.append(MCQ_Questions[i])
            Wrong_Answer.append(MCQ_Answers[i])
    
    print("\nWrong Attempted Questions\n")
    for j in range(len(Wrong_question)):
        print(f"\nQuestion: {Wrong_question[j]}")
        print(f"Answer: {Wrong_Answer[j]}")
    print(f"\nMCQ score = {MCQ_SCORE}/{len(MCQ_Questions)} and MCQ percentage = {(MCQ_SCORE*100)/len(MCQ_Questions)}%")
        
def Subjective():
    print("\nSection B - Subjective\n")
    global Subjective_Score
    print("Type 'exit' on a new last after completing your answer.")
    for i in range(len(Subjective_Questions)):
        print(f"\n{Subjective_Questions[i]}")
        answer = ''''''
        print("Type answer: ", end = "")
        while True:
            line = input()
            if line.lower() == "exit":
                break
            answer += line + "\n"
        Subjective_Answer.append(answer)

    # Evaluation will be done by teachers
    for i in range(len(Subjective_Questions)):
        print("\nQuestion: ",Subjective_Questions[i])
        print("Answer: ", Subjective_Answer[i])
        d = float(input("Give Marks: "))
        Subjective_Score += d
    print(f"\nSubjective score = {Subjective_Score}/{len(Subjective_Questions) * 2.5} and Subjective percentage = {(Subjective_Score*100)/(len(Subjective_Questions)*2.5)}%")

def Final_Evaluation():
    print(f"Total score = {(MCQ_SCORE + Subjective_Score)}/ {(Maximum_MCQ + Maximum_Subjective)} and total percentage = {((MCQ_SCORE + Subjective_Score) * 100 / (Maximum_MCQ + Maximum_Subjective)):.2f}%")

MCQS()
Subjective()
Final_Evaluation()