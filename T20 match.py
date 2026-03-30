#coding
import random
team1 = ' England '
team2 = ' Australia '

ch = [0,1,2,3,4,6,'wd','b','lb',nd','w']
prob = [0.4,0.5,0.2,0.01,0.1,0.09,0.05,0.01,0.01,0.03,0.01]

ball1 = 0
team1_run = 0
team1_wicket = 0
while ball1 < 120:
    run1 = random.choices(ch,prob)[0]
    if run1 == 'w':
        ball1 += 1
        team1_wicket += 1
    elif run1 == 'wd' or run1 == 'nb' or run1 == 'b' or run1 == 'lb':
        team1_run += 1
    else:
        ball2 += 1
        team1_run += run1
    # To stop innings after allout
    if team1_wicket == 10:
        break
#final scorecard    
print(f'{team1} : {team1_run}-{team1_wicket}({ball1//6}.{ball1%6})')

# chasing
ball2 = 0
team2_run = 0
team2_wicket = 0
while ball2 < 120:
    run2 = random.choices(ch,prob)[0]
    if run2 == 'w':
        ball2 += 1
        team2_wicket += 1
    elif run2 == 'wd' or run2 == 'nb' or run2 == 'b' or run2 == 'lb':
        team2_run += 1
    else:
        ball2 += 1
        team2_run += run2
    # to stop innings after all out or Target chased
    if team2_wicket ==10 or team2_run > team1_run:
        break
   
print(f'{team2} : {team2_run}-{team2_wicket}({ball2//6}.{ball2%6})')
print()
print()
#result
if team1_run > team2_run:
    print(f'{team1} won by {team1_run - team2_run} runs ')
elif team2_run > team1_run:
    print(f'{team2} won by {10- team2_wicket} wickets ')
else:
    print(f' Match tied!')
