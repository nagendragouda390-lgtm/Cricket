# Cricket
Cricket score card - 20 Over Match

## Overview
This project simulates a 20 over cricket match with random ball-by-ball outcomes.

## Features
- Random ball-by-ball simulation
- Realistic cricket scoring (runs, wickets, boundaries)
- 20 over format
- Match statistics and scorecard

## Code
```python
import random

# 20 Over Cricket Match Simulation
def simulate_cricket_match(team):
    total_runs = 0
    wickets = 0
    balls_played = 0
    total_balls = 120  # 20 overs × 6 balls per over
    
    for i in range(total_balls):
        # Random outcome for each ball
        ch = [0,1,2,3,4,6,'w']
        prob = [0.4,0.4,0.2,0.01,0.1,0.09,0.01]
        outcome = random.choices(ch,prob)[0]
        
        if outcome == 0:
            # Dot ball
            balls_played += 1
        elif outcome == 1:
            # Single run
            total_runs += 1
            balls_played += 1
        elif outcome == 2:
            # Double runs
            total_runs += 2
            balls_played += 1
        elif outcome == 3:
            # Triple runs
            total_runs += 3
            balls_played += 1
        elif outcome == 4:
            # Four runs
            total_runs += 4
            balls_played += 1
        elif outcome == 6:
            # Six runs
            total_runs += 6
            balls_played += 1
        elif outcome == 'w':
            # Wicket
            wickets += 1
            balls_played += 1
            if wickets == 10:
                break
    return total_runs
    
    print(f"{team}\nFinal Score: {total_runs}/{wickets}")
    print(f"Balls Played: {balls_played}")

first = simulate_cricket_match('srilanka')
second = simulate_cricket_match('england')

if first > second:
    print('SRI LANKA won the match by ',first - second,' runs')
else :
    print('England won ')
```

## Usage
Run the script to simulate a 20 over cricket match with random ball-by-ball outcomes.

## License
Open source