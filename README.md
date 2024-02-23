This Python code is developed using Python 3.8. 

### versions 
*version 1: 16/2/24* 

*version 2: 23/2/24*

#### Files & Folders 

It's organized into five files within the folder:
1. main.py
2. login.py
3. upload.py
4. download.py
5. create_folder

+ Folder _images_ contain the images you want to upload
+ Folder _download_folder_ is the folder where the downloaded images are stored

***

> [!NOTE]
> To execute the program, run the main.py script using the following parameters:


#### Credentials:
+ --group  #user group
+ --user   #user name
+ --pass   #password

#### Operations:
+ --post   # upload a file
+ --get    # download a file
+ --create-folder # create a new folder for a project

#### File Path:
+ --path    # Path of the image you want to upload 
+ --search  # Pattern you want to search
+ --folderName # Define the name of the folder

***
For example:

Upload an image to the server
> python3 main.py --post --path ./images/goats_2_fr0050.jpg

Download image from the server 
> python3 main.py --get --search goats_2_fr0094.jpg

Create a new folder
> python3 main.py --create-folder --folderName "ODE_Test"

