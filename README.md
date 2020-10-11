# InnoClubs
InnoClubs project for Fundamentals of Software Engineering course (Fall 2020, group 02) at Innopolis University

# Get ready for launch
Before starting the server you need to add django key to your environmental variables.

## Linux
* Open `~/.bashrc`
* Add command `export FSE_DJANGO_KEY='(your_key)'` with actual key instead of `(your_key)`
* Restart the system or write bash command `source ~/.bashrc` to apply changes

## Windows
* Open properties by right-clicking **Computer** and choosing corresponding option or click on **System** in Windows Control Panel
* Switch to **Advanced** tab
* Press **Environment Variables...** button
* Use **New** to create a new variable with name `FSE_DJANGO_KEY` and corresponding value
* Click **Apply** and **OK** to save changes