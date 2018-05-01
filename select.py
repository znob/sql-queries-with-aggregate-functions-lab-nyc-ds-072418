# Code your solutions below:

def total_seasons():
    return "SELECT COUNT(year) FROM babe_ruth_stats;"

def total_seasons_with_ny():
    return "SELECT COUNT(year) FROM babe_ruth_stats WHERE team = 'NY';"

def most_hr():
    return "SELECT MAX(HR) FROM babe_ruth_stats;"

def least_hr():
    return "SELECT MIN(HR) FROM babe_ruth_stats;"

def year_and_games_with_least_hr():
    return "SELECT year, games FROM babe_ruth_stats WHERE HR = 0;"

def select_yr_and_min_hr_with_at_least_100_games():
    return "SELECT year, MIN(HR) FROM babe_ruth_stats WHERE games > 100;"

def total_hr():
    return "SELECT SUM(HR) FROM babe_ruth_stats;"

def average_hr_per_year():
    return "SELECT AVG(HR) FROM babe_ruth_stats;"

def avg_batting_avg_aliased_as_career_average():
    return "SELECT AVG(AVG) AS career_average FROM babe_ruth_stats;"

def total_years_and_hits_per_team():
    return "SELECT team, COUNT(year), SUM(hits) FROM babe_ruth_stats GROUP BY team;"

def total_years_and_hr_per_team_ordered_by_hr():
    return "SELECT team, COUNT(year), SUM(HR) FROM babe_ruth_stats GROUP BY team ORDER BY HR DESC"
