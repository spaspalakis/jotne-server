This Python code is developed using Python 3.8. 

It's organized into four files within the folder:
1. main.py
2. login.py
3. upload.py
4. download.py

To execute the program, run the main.py script using the following command:
> python3 main.py 

The program supports the following command-line arguments:

## Credentials:
--group #user group
--user #user name
--pass #password

## Operations:
--post #upload a file
--get #download a file

## File Path:
--path # Path of the image you want to upload 
--search # Pattern you want to search

For example
> python3 main.py --post --path ./images/goats_2_fr0050.jpg
