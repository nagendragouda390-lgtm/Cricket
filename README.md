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
def simulate_cricket_match():
    total_runs = 0
    wickets = 0
    balls_played = 0
    total_balls = 120  # 20 overs × 6 balls per over
    
    for i in range(total_balls):
        # Random outcome for each ball
        outcome = random.randint(0, 6)
        
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
        elif outcome == 5:
            # Six runs
            total_runs += 6
            balls_played += 1
        elif outcome == 6:
            # Wicket
            wickets += 1
            balls_played += 1
            if wickets == 10:
                break
    
    print(f"Final Score: {total_runs}/{wickets}")
    print(f"Balls Played: {balls_played}")

simulate_cricket_match()
```

## Usage
Run the script to simulate a 20 over cricket match with random ball-by-ball outcomes.

## License
Open source