
# Website alerts

> ## About
>This program was made to help everbody track their website, especially if they have more then one and to make their life easier. If your website is down you will get alert via email. Don't worry even if you missed an e-mail there are logs, so you can always check what was happening when you were sleeping. I got you covered, you can sleep peacefully now. 😴🛌
> ### Author
> Kristijan Vidović

> ## Folder structure
.
└── venv/
    └── Lib/
        └── site-packages/
            └── treesource-0.0.6.dist-info/
                └── METADATA (The main readme)




> ## Prerequsites
> To get started make sure you have Python 3 installed on your system (version 3.10), if not you can download it [here.](https://www.python.org/) You have to have Python PATH set if you are using Windows to be able to use "python" command. See instructions [here.](https://www.python.org/) You need to have [Docker for Windows](https://docs.docker.com/desktop/windows/install/) installed on your PC.
> ### Optional
> Installed [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker) VS Code exstensions if you are using VS Code as you code editor.

> ## Getting started
> To get started open up your VS Code or your prefered editor and follow my instruction, feel free to drink coffe ☕ as you follow my setup along. Also to be able to send email alerts you need to configure config.yaml file with your e-mail settings.


> ## Installation and setup
> 1. **First we need to setup virtual environment** (This step is optional)\
> Type in this command to your VS Code or CMD (make sure you are in the right directory):
> ```python
> python -m venv <choose-name>
>```
>\
> Activate your virtual environment:
> ```python
> <choosen-name>\Scripts\activate.bat  or  <choosen-nam>\Scripts\activate   
>```
> 2. **Second, install all required dependencies**\
> To install all required dependencies run:
> ```python
> pip install -r requirements.txt
>```
> 3. **Build your docker image** (This step is optional)
> \
> To build your docker image type in (make sure you are in a dir where the dockerfile is located):
> ```python
> docker build -t <docker-username>/<app-name>:<app-version> .
>```
> ## Run options
> If you have done all the steps required above.\
> Now you can run your Flask application in two ways:
> 1. ### Run using Docker
> Type this command or run your image from Docker Desktop application:\
> ```python
> docker run <image-name> #You can find your image name in your Docker Desktop app
>```
> Now you can monitor Docker terminal to see the script in action
>
> 2. ### Run without Docker
> To start your Flask app you can type in this command (make sure you have activated your virtual env and that you are in the right dir):
> ```python
> python alert.py
>```
> Now you can monitor terminal to see the script in action or see logs for more detail and for easier tracking.

> ## Contact me
> Feel free to contact me on my personal email vidovic@kristijan.me or using the contact form on my [personal website.](https://kristijan.me) 😊