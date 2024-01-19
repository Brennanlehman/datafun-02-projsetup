"""This module which is part of Project 2 provides functions for creating a series of project folders."""

#import dependencies
import os
import pathlib
import time
import lehman_utils


#define functions for folder creations 
def create_folders_for_range(start, end): 
  #generate folders for given range
  for year in range(start, end + 1):
    pathlib.Path(str(year)).mkdir(exist_ok=True)

# define function to create folders from a list of names.
def create_folders_from_list(folder_list, to_lowercase=True, remove_spaces=True): 
    # Generate folders from list
    for item in folder_list:
        folder_name = str(item)

        # Apply options
        if to_lowercase:
            folder_name = folder_name.lower()
        if remove_spaces:
            folder_name = folder_name.replace(' ', '_')

        pathlib.Path(folder_name).mkdir(exist_ok=True)

# define function to create prefixed folders
def create_prefixed_folders(folder_list, prefix): 
    # Generate folders with prefix
    pre_res = [prefix + item for item in folder_list]
    for item in pre_res:
        if not os.path.exists(item):
            os.mkdir(item)

#function to create folders periodically
def create_folders_periodically(duration):
#while loop to generate periodically
  strategy_projects = 5  #number of projects in queue
  while strategy_projects > 0:
    strategy_projects -= 1
    time.sleep(5)
    pathlib.Path("data-strategy").mkdir(exist_ok=True)



# Create a path object
project_path = pathlib.Path.cwd()

# Define the new sub folder path
data_path = project_path.joinpath('data')

# Create new if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)

def main():
    """Main function for project 2 to demonstrate module capabilities."""

    # Print byline from imported module
    print(f"Byline: {lehman_utils.byline}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start=2020, end=2023)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs = 5  # duration in seconds
    create_folders_periodically(duration_secs)

    # Add options e.g., to force lowercase and remove spaces 
    # to one or more of your functions (e.g. function 2) 
    # Call your function and test these options
    regions = [
        "North America", 
        "South America", 
        "Europe", 
        "Asia", 
        "Africa", 
        "Oceania", 
        "Middle East"
    ]
    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)

if __name__ == '__main__':
    main()

#This project was created with my own code according to specs and assited with OpenAI for error correction/debugging
