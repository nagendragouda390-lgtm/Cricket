#coding
import random

team1 = 'England'
team2 = 'Australia'

ch = [0,1,2,3,4,6,'wd','b','lb','nb','w']
prob = [0.30,0.35,0.10,0.05,0.08,0.05,0.03,0.01,0.01,0.01,0.01]

# Function to simulate innings with ball-by-ball commentary
def simulate_innings(team_name):
    ball = 0
    team_run = 0
    team_wicket = 0
    batsmen = []
    current_batsman = {'name': f'Batsman {len(batsmen) + 1}', 'runs': 0, 'balls': 0, 'status': 'not out'}
    ball_events = []  # Store each ball's event
    
    print(f"\n{'='*80}")
    print(f"{team_name} Innings - Ball by Ball Commentary")
    print(f"{'='*80}")
    print(f"{'Over.Ball':<12} {'Event':<20} {'Runs':<8} {'Batter':<20} {'Score':<20}")
    print(f"{'-'*80}")
    
    while ball < 120:
        run = random.choices(ch, prob)[0]
        overs = ball // 6
        balls_in_over = ball % 6
        over_ball = f"{overs}.{balls_in_over}"
        
        event = ""
        current_runs = 0
        
        if run == 'w':
            ball += 1
            team_wicket += 1
            event = "WICKET!"
            current_batsman['status'] = 'out'
            batsmen.append(current_batsman)
            
            print(f"{over_ball:<12} {event:<20} {'-':<8} {current_batsman['name']:<20} {team_run}/{team_wicket} ({overs}.{balls_in_over})")
            
            # New batsman comes in (if not all out)
            if team_wicket < 10:
                current_batsman = {'name': f'Batsman {len(batsmen) + 1}', 'runs': 0, 'balls': 0, 'status': 'not out'}
        
        elif run == 'wd':
            event = "Wide"
            team_run += 1
            current_runs = 1
            print(f"{over_ball:<12} {event:<20} {current_runs:<8} {current_batsman['name']:<20} {team_run}/{team_wicket}")
        
        elif run == 'nb':
            event = "No Ball"
            team_run += 1
            current_runs = 1
            print(f"{over_ball:<12} {event:<20} {current_runs:<8} {current_batsman['name']:<20} {team_run}/{team_wicket}")
        
        elif run == 'b':
            event = "Bye"
            team_run += 1
            current_runs = 1
            print(f"{over_ball:<12} {event:<20} {current_runs:<8} {current_batsman['name']:<20} {team_run}/{team_wicket}")
        
        elif run == 'lb':
            event = "Leg Bye"
            team_run += 1
            current_runs = 1
            print(f"{over_ball:<12} {event:<20} {current_runs:<8} {current_batsman['name']:<20} {team_run}/{team_wicket}")
        
        else:
            ball += 1
            team_run += run
            current_batsman['runs'] += run
            current_batsman['balls'] += 1
            
            if run == 0:
                event = "Dot ball"
            elif run == 1:
                event = "Single"
            elif run == 2:
                event = "Two"
            elif run == 3:
                event = "Three"
            elif run == 4:
                event = "FOUR!"
            elif run == 6:
                event = "SIX!!!"
            
            current_runs = run
            print(f"{over_ball:<12} {event:<20} {current_runs:<8} {current_batsman['name']:<20} {team_run}/{team_wicket}")
        
        ball_events.append({
            'over_ball': over_ball,
            'event': event,
            'runs': current_runs,
            'batter': current_batsman['name'],
            'team_score': f"{team_run}/{team_wicket}"
        })
        
        # To stop innings after all out
        if team_wicket == 10:
            print(f"{'-'*80}")
            print(f"All Out! Total: {team_run}-{team_wicket} ({overs}.{balls_in_over} overs)")
            break
    
    # Add last batsman (not out)
    if current_batsman['balls'] > 0 and current_batsman['status'] == 'not out':
        batsmen.append(current_batsman)
    
    return {
        'team': team_name,
        'total_runs': team_run,
        'total_wickets': team_wicket,
        'overs': f'{(ball//6)}.{ball%6}',
        'total_balls': ball,
        'batsmen': batsmen,
        'ball_events': ball_events
    }

# Simulate both innings
team1_innings = simulate_innings(team1)
team2_innings = simulate_innings(team2)

# Display individual batsman scorecard for team 1
print(f"\n{'='*60}")
print(f"{team1_innings['team']} - Batting Summary")
print(f"{'='*60}")
print(f"{'Batsman':<20} {'Runs':<10} {'Balls':<10} {'Status':<15}")
print(f"{'-'*60}")
for batsman in team1_innings['batsmen']:
    print(f"{batsman['name']:<20} {batsman['runs']:<10} {batsman['balls']:<10} {batsman['status']:<15}")
print(f"{'-'*60}")
print(f"Total: {team1_innings['total_runs']}-{team1_innings['total_wickets']} ({team1_innings['overs']} overs)")

# Display individual batsman scorecard for team 2
print(f"\n{'='*60}")
print(f"{team2_innings['team']} - Batting Summary")
print(f"{'='*60}")
print(f"{'Batsman':<20} {'Runs':<10} {'Balls':<10} {'Status':<15}")
print(f"{'-'*60}")
for batsman in team2_innings['batsmen']:
    print(f"{batsman['name']:<20} {batsman['runs']:<10} {batsman['balls']:<10} {batsman['status']:<15}")
print(f"{'-'*60}")
print(f"Total: {team2_innings['total_runs']}-{team2_innings['total_wickets']} ({team2_innings['overs']} overs)")

# Result
print(f"\n{'='*80}")
print("MATCH RESULT")
print(f"{'='*80}")
if team1_innings['total_runs'] > team2_innings['total_runs']:
    print(f"{team1_innings['team']} won by {team1_innings['total_runs'] - team2_innings['total_runs']} runs")
elif team2_innings['total_runs'] > team1_innings['total_runs']:
    print(f"{team2_innings['team']} won by {10 - team2_innings['total_wickets']} wickets")
else:
    print("Match tied!")
print(f"{'='*80}\n")