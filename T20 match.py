#coding
import random 

ch = [0,1,2,3,4,6,'wd','b','lb',nd','w']
prob = [0.4,0.5,0.2,0.01,0.1,0.09,0.05,0.01,0.01,0.03,0.01]
ball1 = 0
while ball1 < 120:
    run1 = random.choices(ch,prob)[0]
   
