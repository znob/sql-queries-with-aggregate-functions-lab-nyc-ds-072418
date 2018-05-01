import unittest, sqlite3
from select import *

connection = sqlite3.connect('../babe_ruth.db')
cursor = connection.cursor()

class TestAggregateFunctions(unittest.TestCase):

    file = open("../select.py", "r")
    file.read()

    def test_total_seasons(self):
        result = [(22,)]
        self.assertEqual(cursor.execute(total_seasons()).fetchall(), result)

    def test_total_seasons_with_ny(self):
        result = [(15,)]
        self.assertEqual(cursor.execute(total_seasons_with_ny()).fetchall(), result)

    def test_most_hr(self):
        result = [(60,)]
        self.assertEqual(cursor.execute(most_hr()).fetchall(), result)

    def test_least_hr(self):
        result = [(0,)]
        self.assertEqual(cursor.execute(least_hr()).fetchall(), result)

    def test_year_and_games_with_least_hr(self):
        result = [(1914, 5)]
        self.assertEqual(cursor.execute(year_and_games_with_least_hr()).fetchall(), result)

    def test_select_yr_and_min_hr_with_at_least_100_games(self):
        result = [(1934, 22)]
        self.assertEqual(cursor.execute(select_yr_and_min_hr_with_at_least_100_games()).fetchall(), result)

    def test_total_hr(self):
        result = [(714,)]
        self.assertEqual(cursor.execute(total_hr()).fetchall(), result)

    def test_average_hr_per_year(self):
        def test_range(result, val1, val2):
            if val1 < result < val2:
                return True
            else:
                return False

        result = cursor.execute(average_hr_per_year()).fetchall()[0][0]
        self.assertTrue(test_range(result, 32.4, 32.5))

    def test_avg_batting_avg_aliased_as_career_average(self):
        def test_range(result, val1, val2):
            if val1 < result < val2:
                return True
            else:
                return False

        result = cursor.execute(avg_batting_avg_aliased_as_career_average()).fetchall()[0][0]
        self.assertTrue(test_range(result, 0.3228, 0.3229))

        def test_alias():
            query_str = avg_batting_avg_aliased_as_career_average()
            if "career_average" in query_str:
                return True
            else:
                return False

        self.assertTrue(test_alias(), "alias should be 'career_average'")

    def test_total_years_and_hits_per_team(self):
        result = [('BOS', 7, 355), ('NY', 15, 2518)]
        self.assertEqual(cursor.execute(total_years_and_hits_per_team()).fetchall(), result)

    def test_total_years_and_hr_per_team_ordered_by_hr(self):
        result = [('NY', 15, 659), ('BOS', 7, 55)]
        self.assertEqual(cursor.execute(total_years_and_hr_per_team_ordered_by_hr()).fetchall(), result)
