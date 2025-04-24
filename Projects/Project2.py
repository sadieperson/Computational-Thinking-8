# Beginning: create variable
winter_points = 0 
summer_points = 0 


# Middle: Ask questions! 
answer = input ("Do you enjoy A) hot drinks, or B) cold drinks?")
if answer == "A":
    winter_points += 1
elif answer == "B":
    summer_points += 1 


answer = input ("Do you A )like going somewhere cold, or B) like going somewhere tropical?")
if answer == "A":
    winter_points += 1 
elif answer == "B":
    summer_points += 1 

answer = input ("Do you A) enjoy skiing, or b) enjoy swimming/tanning?") 
if answer == "A":
    winter_points += 1
elif answer == "B":
    summer_points += 1

answer = input ("Do you A) like snow, or b) like sand?")
if answer == "A":
    winter_points += 1
elif answer == "B":
    summer_points += 1

answer = input ("Do you a) enjoy fresh fruit, or b) no fruit?") 
if answer == "A":
    summer_points += 1
elif answer == "B":
    winter_points += 1 

# End: Determining answers 
if winter_points > summer_points:
    print ("You are a Winter person")
elif summer_points > winter_points:
    print (" You are a Summer person")