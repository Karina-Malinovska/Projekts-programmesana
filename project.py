# ##############################################################################
# Lebed Anastasija Karina Malinovska project 10a form
# Spread participents to teams randomly
# ##############################################################################
import random

# Define necessary variables
teamsCounter=int(0)
participentsCounter=int(0)

# Input teams and participents quantaty
while (participentsCounter<teamsCounter) or (teamsCounter==0) or (participentsCounter==0) :
    teamsCounter=int(input("Enter teams quantaty: "))
    participentsCounter=int(input("How much are participents: "))
    if participentsCounter<teamsCounter :
        print("Impossible participents less than teams.\n Please, try again.")
        continue
    if (participentsCounter % teamsCounter)!=0 :
        reply=input("Is it possible that are unfull teams? (y/n): ")
        if reply=="y" :
            exit
        else :
            print(" There are not enought participents for teams.\n Please correct your input.")
            teamsCounter=0

# Define participents name input procedure 
participentsName = []
for participent in range(participentsCounter) :
    pName="Enter name of participent Nr. "+str(participent+1)+" "
    participentsName.append(input(pName))
    
# Define teams name input procedure
teamsName = []
for team in range(teamsCounter) :
    tName="Enter name of team Nr. "+str(team+1)+" "
    teamsName.append(input(tName))

# next strings for test proposal only
#teamsName=["First","Second","Third","Fourth"]
#teamsCounter=len(teamsName)
#participentsName=["a","b","c","d","e","f","g","h","i","j","k"]
#participentsCounter=len(participentsName)

majorQuantatyOfParticipents=int(participentsCounter//teamsCounter)
restParticipents=int(participentsCounter%teamsCounter)
# Spred participents to teams
member = []
for team in range(teamsCounter) :
    selected=random.sample(participentsName,majorQuantatyOfParticipents) # select participents from common list
    member.append([]) # add additional index to member array
    for part in range(majorQuantatyOfParticipents):
        participentsName.remove(selected[part]) # remove participent from list that was added to team
        member[team].append(selected[part]) # add participent as member to team

# Spred rest participents to teams
teamIndex=[]   # indexed teams
for i in range(teamsCounter) : teamIndex.append(i)
# Select team for rest participents
for part in range(len(participentsName)):
    team=random.choice(teamIndex) # choice team where participent will be added
    teamIndex.remove(team) # remove team index where partisipents was added
    member[team].append(participentsName[part])
    
# Output teams list
for team in range(teamsCounter):
    ls=str("Team \""+teamsName[team]+"\" members: ")
    for person in range(len(member[team])):
        ls = ls + member[team][person] + " "
    print(ls)
