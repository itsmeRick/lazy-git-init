# lazy-git-init
One script to make a project directory and all related git initializations


I only wrote this to work on my laptop running Arch Linux, so haven't tested on other systems...

Need to create a .env file as this script uses python-dotenv to load your github credentials and project paths

Installation
------------------
```
$ git clone "https://github.com/itsmeRick/lazy-git-init.git"
$ pip install PyGithub
$ pip install python-dotenv
```

.env File Format
------------------
```
user="your-username"
pass="your-password"
path="/your/project/path"
```
Starting Project
------------------
```
$ ./init.sh project_name
```
For example:
```
$ ./init.sh helloworld
```
