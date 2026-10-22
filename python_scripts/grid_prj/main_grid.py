#!/usr/bin/python3

from grid_logic import display_grid

def main():
    """
    Run the grid program using the number of grids provided by the user.
    """
    
    grid_val = instruct() #func that handles printing out the information to the user and collects necessiry info from user
    
    #the display_grid is responsible for checking if the val is +ve or not and returns False otherwise
    grid = display_grid(grid_val) 
    
    #if the check returns FALSE then abort program with a msg saying no proper +int was passed

    #runs the program if it is a +ve int
    if grid is False:
        print("exiting no proper int was passed....")
    else:
        print("Program completed successfully")

def instruct():
    msg=(
        "This program draws a grid having rows and column\n"
        "based on the data provided by you if no prominent data is provided,\n"
        "defaults to drawing just one grid.\n"
    )
    print(msg)

    grid_no=input("\tProvide number of grid:\n\t")

    #Apply defaults if the user pressed enter with nothing 
    grid_no = grid_no.strip() or "1"

    return grid_no
        


if __name__ == "__main__":
    main()

