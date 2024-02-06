This Python code is developed using Python 3.8. 

#### Files & Folders 

It's organized into four files within the folder:
1. main.py
2. login.py
3. upload.py
4. download.py

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
+ --post   #upload a file
+ --get    #download a file

#### File Path:
+ --path    #Path of the image you want to upload 
+ --search  #Pattern you want to search

***
For example:

Upload an image to the server
> python3 main.py --post --path ./images/goats_2_fr0050.jpg

Download image from the server 
> python3 main.py --get --search goats_2_fr0094.jpg



