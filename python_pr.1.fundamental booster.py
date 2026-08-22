#======================WELCOME==============================

#=================CREAT : AYUSH JIVANI=====================


# ===========================================================
# ===========================================================


#================== PYTHON FUNDAMENTAL BOOSTER================

print("=" * 65)
print("PYTHON FUNDAMETAL BOOSTER")
print("SMART LEARNING SKILL ANALYZER")
print("=" * 65)



# input() + Variable + Data Types

name = input("Enter your name:")
age = int(input("Enter your age:"))
coding_hours = float(input("Daily codind hours:"))
python_topic = int(input("How many Python topic have you learned/"))
practies_days = int(input("Practice days this week:"))
goal = input("Your Python goal:")
height = int(input("Enter your height:"))
favourite_number = int(input("Enter your favourite number:"))



# Type casting

age_number = int(age)
hours_number = float(coding_hours)

# Operator + arithmetic Calculation

practice_score = practies_days*6
coding_score = int(hours_number*7)
topic_score = python_topic*4

total_score = practice_score + coding_score + topic_score

#Keep score between 0 and 100
if total_score > 100:
    total_score + 100


#Program Flow + Dta Processing    

if total_score >= 80:
    leval = "python Pro Booster"
elif total_score >= 60:
    leval = "Storng Learner"
elif total_score >= 40:
    leval = "Growing Coding"
else:
    leval = "Beginner Booster"


if practies_days >= 7:
    practies_message = "Excellent consistency!"
elif practies_days >= 6:
    practies_message = "Good constistency.Keep going!"
else :
    practies_message = "Practies a little every day."


    
# String Concatenation + Formatted String
profile_title = "BOOSTER PROFILE-" + name


# print() + Display Results
print("\n" + "=" * 65)
print(profile_title)
print("=" * 65)

print(f"Age    :{age_number}")
print(f"Daily Coding : {hours_number :.1f} hours")
print(f"Topic Learned : {python_topic}")
print(f"Practies Days  : {practies_days}/7")
print(f"python Goal : {goal}")
print(f"Height : {height}")
print(f"favourite Number  :{favourite_number}")

print("-" * 65)
print(f"Practice Score  :{practice_score}")
print(f"Coding Score  :{coding_score}")
print(f"Topic Score :{topic_score}")
print(f"TOTAL SCORE  :{total_score}/100")
print(f"LEVAL    :{leval}")
print(f"ADVICE  :{practies_message}")

# type() Function

print("\n" + "=" * 65)
print("DATA TYPE CHECK")
print("=" * 65)


print(f"name   :{type(name).__name__}")
print(f"age    :{type(age).__name__}")
print(f"coding_hours   :{type(coding_hours).__name__}")
print(f"python_topic   :{type(python_topic).__name__}")
print(f"goal    :{type(goal).__name__}")

# id()Function + Memory Address

print("\n" + "=" * 65)
print("MEMORY CHECK")
print("=" * 65)

print(f"name memory   :{id(name)}")
print(f"age memory    :{id(name)}")
print(f" coding_hours memory  :{id(coding_hours)}")


# Python Fundamental : collection,loop and final report

print("\n" + "=" * 65)
print("PYTHON FUNDAMENTALS REPORT")
print("=" * 65)


student_data ={
    "Name" : name,
    "Age" : age,
    "Conding Hours" : coding_hours,
    "Topic Learned" : python_topic,
    "Practies Days" : practies_days,
    "Goal" : goal
}


for key, value in student_data.items():
    print(f"{key}:{value}")


print("\n" + "=" * 65)
print(f"{name} , your Python Fundametal Booster Score is{total_score}/100!")
print("keep practicing , keep building , and become a better Python coder.")
print("=" * 65)

print("thank you")


#=====================THANK YOU======================

 





      





















    
    


























    















