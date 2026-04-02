# Cricket T20 Match Simulator

A Python-based T20 cricket match simulator that generates realistic ball-by-ball commentary and match statistics.

## Overviews
This project simulates a complete T20 cricket match between England and Australia with random ball-by-ball outcomes. It provides detailed commentary, individual batsman statistics, and match results.

## Features
- **Ball-by-Ball Commentary**: Detailed play-by-play simulation of each delivery
- **Realistic Cricket Outcomes**: Includes dots, singles, boundaries, wickets, wides, no-balls, and byes
- **Batsman Tracking**: Maintains individual statistics for each batsman (runs, balls faced, status)
- **Innings Summary**: Displays batting scorecards for both teams
- **Match Result**: Determines and displays the winner
- **Customizable Probability Distribution**: Ball outcomes are weighted based on realistic cricket probabilities
- **20 Over Format**: Full 120-ball simulation per innings

## How It Works
1. Each ball is randomly selected from a predefined set of outcomes with weighted probabilities
2. Runs, wickets, and special cricket events (wides, no-balls, byes, leg-byes) are tracked
3. After each wicket, a new batsman comes in (up to 10 wickets)
4. Innings ends after 20 overs or when all 10 wickets fall
5. Final match result is determined by comparing team scores

## Output
The simulator provides:
- Complete ball-by-ball commentary with over.ball notation
- Team batting summaries with individual batsman records
- Match result with winning margins

## Usage
Run the script to simulate a complete T20 match:

```bash
python "T20 match.py"
```

## Customization
You can easily modify:
- Team names (`team1`, `team2`)
- Ball outcomes in the `ch` list
- Outcome probabilities in the `prob` list

## License
Open source
