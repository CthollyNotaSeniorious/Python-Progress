# Exercise 14 - Stats Report
# Given three numbers that represent the number of wins, losses, and draws of a football team,
# write a program that generates a report with the following information:
# 1- The total number of games played.
# 2- The percentage of games won.
# 3- The percentage of games lost.
# 4- The percentage of games drawn.
# The function should return a string with the report.
# For example, given the numbers 3, 2, and 1, the function should return:
# "The team played 6 games. They won 50.0% of the games, lost 33.3% of the games, and drew 16.7% of the games."
# Note: The percentages should be rounded to one decimal place.
# You can assume that the input numbers are > 0.


def generate_stats_report(wins, losses, draws):
    total_games = None
    wins_percentage = None
    losses_percentage = None
    draws_percentage = None
    # Your code should go here.

    return f"The team played {total_games} games. They won {wins_percentage}% of the games, lost {losses_percentage}% of the games, and drew {draws_percentage}% of the games."  # noqa
