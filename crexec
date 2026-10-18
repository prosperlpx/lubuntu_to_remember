#!/usr/bin/bash

#this program collects an argument of file name and makes it an executable file 

#collects user input args if none is provided

FILE_NAME="$1"
file_name_required="No file name provided please provide a file name to make an executable."
file_name_err="Error: A file name is neccessary exiting \n"

check_args(){
    if [ -z "$FILE_NAME" ]; then
        read -r -p "$file_name_required" FILE_NAME #gets the file name from user input

#if no file path is passed and an enter is returned check and return an error
        if [[ -z "$FILE_NAME" ]]; then 
            printf "$file_name_err" >&2
            exit 1
        else
            create_exec "$FILE_NAME"
            return 0
        fi
    else
        create_exec "$FILE_NAME"
        return 0
    fi
}

#this func runs the main purpose of the program making the file an executable
create_exec(){
    printf "Working on making '%s' an executable \n" "$1"
    printf "Creating the folder \n"
   > $1 && chmod u+x "$1" &> /dev/null

    printf "'%s' is now an executable and is in $(find . -type f -name $1)\n" "$1"
}

check_args "$FILE_NAME" #this is the parent func of this file

