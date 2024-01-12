''' This module provides a reusable byline for the author's services. '''

#import directories
import math
import statistics

#define variables
company_name: str = "Bearcat Strategic Inc."
count_active_projects: int = 4
has_international_presence: bool = True
average_client_satisfaction: float = 4.9
services_offered: list = ["Governance", "Planning", "AI","Visualization"]
satisfaction_scores: list = [4.3, 4.9, 4.8, 5.0, 4.8]

#define formatted strings
active_projects_string: str = f"Projects in Pipeline: {count_active_projects}"
international_presence_string: str = f"International: {has_international_presence}"
client_satisfaction_string: str = f"Client Satisfaction - Average: {average_client_satisfaction}"

#calculations
smallest= min(satisfaction_scores)
largest= max(satisfaction_scores)
total= sum(satisfaction_scores)
count= len(satisfaction_scores)
mean= statistics.mean(satisfaction_scores)
mode= statistics.mode(satisfaction_scores)
median= statistics.median(satisfaction_scores)
standard_deviation=statistics.stdev(satisfaction_scores)

stats_string: str = f"""
Descriptive Statistics for Our Satisfaction Scores:
  Smallest: {smallest}
  Largest: {largest}
  Total: {total}
  Count: {count}
  Mean: {mean}
  Mode: {mode}
  Median: {median}
  Standard Deviation: {standard_deviation}
"""

#byline string
byline: str = f"""
{company_name}
{active_projects_string}
{international_presence_string}
{client_satisfaction_string}
{services_offered}
{stats_string}
"""

def main():
  ''' Display all output'''
  print(company_name)
  print(active_projects_string)
  print(international_presence_string)
  print(client_satisfaction_string)
  print(services_offered)
  print(stats_string)

  print(byline)
if __name__ == "__main__":
    main()
