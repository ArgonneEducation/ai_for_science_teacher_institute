# Teacher_Institute
*Sharing Materials from the Argonne National Laboratory Teacher Institute*

<div align="center">
  <a href="https://github.com/ArgonneEducation/ai_for_science_teacher_institute">
  </a>

<h2 align="center">AI For Science Teacher Institute</h2>

  <p align="center">
    This repo is intended to be a central hub for sharing materials for and from the ai for science teacher institute.  
We also hope to use it to provide tips for how to get started with python coding for new coders.
    <br />
    <a href="https://github.com/ArgonneEducation/ai_for_science_teacher_institute"><strong>Explore the docs »</strong></a>
    <br />
    <br />
  </p>

<p align="left">
This GitHub repository is set up for users to be able to access the coding materials during and after the ai for science teacher institute program.  GitHub is a platform that allows developers to store their code, and we are taking advantage of that functionality.  It also allows developers to collaborate on code – this is a functionality that we are not taking advantage of here, since we expect many of the users we send to this site to be relatively new at developing code and using it for teaching science.
</p>
<p align="left">
This ReadMe is organized in a way that you will hopefully find to be easy to follow, whether you are new to coding or more advanced.  For beginners, you may want to start with the “Getting Started” section.  In it, we’ll guide you to using GitHub codespaces for your coding.  While there are many other platforms that you could use for this purpose, codespaces will allow you to access the files you need right alongside your coding environment, with a minimal amount of setup work to be done before diving in.  
</p>
<p align="left">
The “Getting Started” section therefore starts with setting up your own GitHub account.  This is required for using codespaces, and honestly, anyone who wants more flexibility in their coding environment probably will have a GitHub account.  So it seems like a very reasonable place to start.
</p>
</div>
<br>
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#setting-up-your-github-account">Setting Up Your GitHub Account</a></li>
    <li><a href="#starting-up-a-codespace-from-the-template">Starting up a codespace from the template</a></li>
      <ul>
        <li><a href="#7-stopping-a-codespace">Stopping a codespace</a></li>
      </ul>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<div align="center">
<h3 align="center">Getting Started</h3>
</div>

<div align="left">
<h3 align="left">Setting up your GitHub Account</h3>
<p align="left">
You’ll need an account in order to use the codespaces functionality within GitHub.  You can access the files without an account, but will then need to interact with the code outside of GitHub.  We’ll provide more information about how you might do this later in this ReadMe document.

Navigate to https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github . This GitHub resource provides information about the process.  
Setup your GitHub account as described in the above link.
</p>
</div>
<br>
<br>
<div align="left">
<h3 align="left">Starting up a codespace from the template</h3>


The ai_for_science_teacher_institute repository is a template.  It is reasonably simple to start up a codespace to run the files in the repository.  Here's how.

*1 Navigate to https://github.com/ArgonneEducation/ai_for_science_teacher_institute*

*2 Opening the template in a codespace*

Near the top right hand corner of the screen, find the button that says “Use this template” and click on it.
<br>
      <img src="https://raw.githubusercontent.com/ArgonneEducation/ai_for_science_teacher_institute/refs/heads/main/imgs/use_this_template_open.png" alt="screen-grab" width="200"/>
<br>
Click on the “Open in a codespace” selection.

<br>

*3 Open a Jupyter Notebook*

<br>

To begin coding, you’ll have to open a jupyter notebook.  These are found in the navigation bar on the left of the screen.  Click on the word “notebooks” to see the files.  
<br>
<img src="https://raw.githubusercontent.com/ArgonneEducation/ai_for_science_teacher_institute/refs/heads/main/imgs/notebooks_1.png" alt="screen-grab" style ="width:300px;"/> 
<br>

Each of the files with a “.ipynb” designation is a python “jupyter” notebook that contains python code and markdown text.  If you’re just getting started, double click on the “01-jupyter_python_physics.ipynb” file.

<br>
<img src="https://raw.githubusercontent.com/ArgonneEducation/ai_for_science_teacher_institute/refs/heads/main/imgs/notebooks_2.png" alt="screen-grab" style ="width:300px;"/> 
<br>
This should open up this “notebook” in a new tab.
<br>
<br>

*4  Close the terminal - we don't need it*

<br>

The codespace automatically opens up a terminal at the *bottom* of the screen, which we are not going to use at this beginning level. Click in the bottom frame and type “exit” and "enter" to exit the terminal.  This will free up more of your screen to use for coding.
<br>
<img src="https://raw.githubusercontent.com/ArgonneEducation/ai_for_science_teacher_institute/refs/heads/main/imgs/exiting_terminal.png" alt="screen-grab" style ="width:400px;"/> 
<br>

*5 Select a Kernel (to run code)*

In order to “run” any of the code, we need to select a Kernel to use.  This essentially means we’re installing python files and setting up the particular version of python to use. Click to the “Select Kernel” button in the top right hand corner.
<br>
<div style="text-align: center;">
    <img src="https://raw.githubusercontent.com/ArgonneEducation/ai_for_science_teacher_institute/refs/heads/main/imgs/select_kernel.png" alt="screen-grab" style ="width:700px;"/>
</div>
 
<br>
Then click to Install/Enable suggested Extensions.  After a few seconds, a dialog box appears.  
<br>
<img src="https://raw.githubusercontent.com/ArgonneEducation/ai_for_science_teacher_institute/refs/heads/main/imgs/python_environments.png" alt="screen-grab" style ="width:400px;"/> 
<br>
You can click on "Python Environments" and select any one.  We don't have to be picky for this project.


*6 clear the "running in a port" dialog*

Another prompt will tell you that your application is running in a port.  You can close this dialog box.  We don’t need this functionality.

Congratulations, you are now able to create and run code in this entirely online codespace!  
The codespace is using online resources as long as it is active.  That being the case, it is a VERY good idea to stop it from running when you are no longer going to use it.  Let's practice doing this before doing anything else.  Here’s how:

*7 Stopping a Codespace*

Your codespace has a name generated by github that you can see in the address bar of your internet browser.  My codespace for developing this readme is called urban-guacamole.  I know this because it is in the address bar as shown. Check to see what your codespace is named!
<br>
<br>
<img src="https://raw.githubusercontent.com/ArgonneEducation/ai_for_science_teacher_institute/refs/heads/main/imgs/codespace_name_in_address.png" alt="screen-grab" style ="width:400px;"/> 
<br>
<br>
Simply closing out of the browser tab does not stop all activity in the codespace.  To do so, return to your GitHub home page and click on the hamburger menu (3 stacked horizontal lines) at the top left hand corner next to the cat icon. 
<br>
<br>
<img src="https://raw.githubusercontent.com/ArgonneEducation/ai_for_science_teacher_institute/refs/heads/main/imgs/codespace1.png" alt="screen-grab" style ="width:300px;"/> 
<br>
<br>
Then select “Codespaces” from the list that appears.
<br>
<img src="https://raw.githubusercontent.com/ArgonneEducation/ai_for_science_teacher_institute/refs/heads/main/imgs/codespace2.png" alt="screen-grab" style ="width:250px;"/> 
<br>
At the bottom of the page, you should see the name of your codespace.  
<br>
<img src="https://raw.githubusercontent.com/ArgonneEducation/ai_for_science_teacher_institute/refs/heads/main/imgs/codespace_name.png" alt="screen-grab" style ="width:700px;"/> 
<br>
You can shut it down by clicking on the 3 dots at the far right, and selecting “Stop codespace” . 
<br>
<div style="text-align: center;">
<img src="https://raw.githubusercontent.com/ArgonneEducation/ai_for_science_teacher_institute/refs/heads/main/imgs/codespaces_menu.png" alt="screen-grab" style ="width:250px;"/> 
</div>
<br>

 Your codespace should then no longer be Active.  You can restart your work from this page at any time.  You might also choose to open the notebooks from JupyterLab using this same menu.  JupyterLab has a different look and will match better with some of the content, as it was developed using JupyterLab!

<br>
<br>
<div align="left">
<h3 align="left">Using the Notebooks with Codespaces</h3>
<p align="left">

Our suggestion is to open the repository in JupyterLab via GitHub Codespaces as described in the Getting Started section.  Once you’ve opened the repository, you can explore the notebooks with the file explorer in the left pane of the screen.  The repository contains a folder titled “notebooks”.  This folder contains Jupyter notebooks, which are indicated with a “.ipynb” ending.  Jupyter notebooks are a mix of python code chunks and explanatory material.  There is more information about this structure in the “01-jupyter_python_physics.ipynb” notebook.

This is a good place to start exploring the repository!  
<br>
<img src="https://raw.githubusercontent.com/ArgonneEducation/ai_for_science_teacher_institute/refs/heads/main/imgs/Jupyter_file_explorer.png" alt="screen-grab" style ="width:700px;"/> 
<br>
The notebooks are in numerical order, with titles that also indicate something about the topics contained within the notebooks.
There is an additional folder titled “completed notebooks” that contains Jupyter notebooks that serve as answer keys for many of the notebooks.  Our suggestion is that you use these only after first trying to work through any questions.  You may want to try using google or potentially even an AI large language model before cross-checking with these completed notebooks.  Most coding problems can be solved this way, though it takes a bit of practice and skill to navigate this efficiently.  Therefore, it’s good to practice doing so, rather than simply relying on the provided answers.  

###Noaccount
<br>
<br>
<div align="left">
<h3 align="left">Using the Notebooks Without a GitHub Account</h3>
<p align="left">

If for some reason, you would rather access the files without having to make an account, it is possible to do so.  You will first have to download the files you would like to use from the GitHub repository (step-by-step instructions below).  Then you can access these files, stored on your machine, via the online JupyterLite tool (instructions for this are also below).  

*1a Downloading Individual GitHub Files*

To download files from the GitHub repository, navigate to https://github.com/ArgonneEducation/ai_for_science_teacher_institute, and open the notebooks folder. When you open up a file, it is displayed on the screen and some options appear in the upper right hand corner.
<br>
<br>
<img src="https://raw.githubusercontent.com/ArgonneEducation/ai_for_science_teacher_institute/refs/heads/main/imgs/download_from_repository.png" alt="screen-grab" style ="width:700px;"/> 
<br>
<br>
Simply clicking on the download button with the downward pointing arrow will download the file into your downloads folder.  From there, you could save it to a folder, perhaps titled ai_for_science_teacher_institute.  
<br>
<br>
<img src="https://raw.githubusercontent.com/ArgonneEducation/ai_for_science_teacher_institute/refs/heads/main/imgs/download_closeup.png" alt="screen-grab" style ="width:300px;"/> 
<br>
<br>
If you download the files this way, you will have to create the folder organization system on your machine.

*1b Downloading a Folder from GitHub*

It is possible to download an entire folder from a GitHub repository.  For example, to download the entire contents of the “notebooks” folder, you’ll need its URL.  https://github.com/ArgonneEducation/ai_for_science_teacher_institute/tree/main/notebooks
GitHub has a tool for downloading a zipped folder at https://download-directory.github.io
Simply paste in the URL for the notebook directory and press Enter to download a zipped folder with all of the notebooks.  Extract the files to a folder location of your choosing on your machine.

*2 Opening Files with JupyterLite*

To open your notebook file with JupyterLite, first navigate to https://jupyter.org/try-jupyter/notebooks/?path=notebooks/Intro.ipynb in your browser.  This gives an introductory notebook.
From here, click on File in the menu bar and select Open…
<br>
<br>
<img src="https://raw.githubusercontent.com/ArgonneEducation/ai_for_science_teacher_institute/refs/heads/main/imgs/open_jupyter_lite.png" alt="screen-grab" style ="width:700px;"/> 
<br>
<br>
In the new tab that appears, you’ll next want to upload the notebook that you’d like to run. The "upload" button is in the top right corner of the screen.
<br>
<br>
<img src="https://raw.githubusercontent.com/ArgonneEducation/ai_for_science_teacher_institute/refs/heads/main/imgs/jupyter_upload.png" alt="screen-grab" style ="width:300px;"/> 
<br>
<br>
If you click upload while in the main folder, your file will appear in the file list.  You may want to first open the notebooks folder and then upload the notebook you would like to use.
<br>
<br>
<img src="https://raw.githubusercontent.com/ArgonneEducation/ai_for_science_teacher_institute/refs/heads/main/imgs/jupyter_file_uploaded.png" alt="screen-grab" style ="width:700px;"/> 
<br>
<br>
If you open the file by double clicking on it, you will be prompted to Select a Kernel.
<br>
<br>
<img src="https://raw.githubusercontent.com/ArgonneEducation/ai_for_science_teacher_institute/refs/heads/main/imgs/jupyter_select_kernel.png" alt="screen-grab" style ="width:700px;"/> 
<br>
<br>
Click on Select to start the kernel.  This just means that it is activating the ability for JupyterLite to run python code. 
You are now ready to explore the notebook!
