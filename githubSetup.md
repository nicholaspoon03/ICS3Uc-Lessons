# Github Setup instructions

Make sure you have a Github User account setup, and both Git and Visual Studio Code installed. 

open a terminal directed at your project folder (right click the folder and select "gitbash here" for windows users)
# One-time Configuration
The following steps will be completed once per machine.
exclude external quotes

1) Run "git config --global user.name "username"". Replace "username" with your github username.

2) Run "git config --global user.email "email@gmail.com"". 

3a) (mac only) open vscode, hit apple + shift + p, and search "shell command: Install "code" command in path". Select this option, and it will allow you to access vscode from the terminal

3b) (All Computers) Run "git config --global core.editor "code --wait"". This time, KEEP "code --wait" WITH THE QUOTES!!! 

# Repository Setup - local and remote (online)
You will follow these steps every time you create a new project repository.

Make sure you have atleast 1 file or folder inside of your project folder so that an item exists to be commited. This could be your "mailaddress.py" assignment.

Aim your terminal at the root folder of your project.
1) Run "git init". This creates a hidden folder called .git inside of your project folder. Do not touch this folder.

2) Go to github.com, log-in, and create a new repository. Give it any name. Once created, you will be presented with a repository url such as (https://github.com/username/repo-name.git) Copy this URL for step 3.

3) Run "git remote add origin URL". Replace URL with the one you copied from step 2.

4) Run "git add ." to stage all files and folders inside your root directory. You must stage files before they are committed.

4.5) You may run "git status" at any time to see what is staged or unstaged. If your .py files are green, it means they are staged.

5) Run "git commit". Assuming the one-time setup was done correctly, it will open VScode to a text file. Write a description of your first commit, save the file, then close it. Your terminal will update as soon as you close the text file. *** If the commit is aborted before you are able to edit the file, please go back to step 3) of the one-time setup.

6) Run "git push -u origin master". This command "pushes" your local repository to the remote repository (on github.com) at location origin, branch master. Enter your github username and password. If it appears nothing is typed for your password, it is because the text is hidden! Simply type your correct password and hit enter. 

Please send a message on google classroom if you need any assistance. Screenshots of your errors are greatly appreciated.
