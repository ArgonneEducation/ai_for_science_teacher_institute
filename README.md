# Teacher_Institute
*Sharing Materials from the Argonne National Laboratory Teacher Institute*

<div align="center">
  <a href="https://github.com/ArgonneEducation/ai_for_science_teacher_institute">
  </a>

<h3 align="center">AI For Science Teacher Institute</h3>

  <p align="center">
    This repo is intended to be a central hub for sharing materials for and from the ai for science teacher institute.  
We also hope to use it to provide tips for how to get started with python coding for new coders.
    <br />
    <a href="https://github.com/ArgonneEducation/ai_for_science_teacher_institute"><strong>Explore the docs »</strong></a>
    <br />
    <br />
  </p>
</div>

This GitHub repository is set up for users to be able to access the coding materials during and after the ai for science teacher institute program.  GitHub is a platform that allows developers to store their code, and we are taking advantage of that functionality.  It also allows developers to collaborate on code – this is a functionality that we are not taking advantage of here, since we expect many of the users we send to this site to be relatively new at developing code and using it for teaching science.

This ReadMe is organized in a way that you will hopefully find to be easy to follow, whether you are new to coding or more advanced.  For beginners, you may want to start with the “Getting Started” section.  In it, we’ll guide you to using GitHub codespaces for your coding.  While there are many other platforms that you could use for this purpose, codespaces will allow you to access the files you need right alongside your coding environment, with a minimal amount of setup work to be done before diving in.  

The “Getting Started” section therefore starts with setting up your own GitHub account.  This is required for using codespaces, and honestly, anyone who wants more flexibility in their coding environment probably will have a GitHub account.  So it seems like a very reasonable place to start.


<div align="center">
<h3 align="center">Getting Started</h3>
   <br />
</div>
Setting up your GitHub Account – you’ll need to do this in order to use the codespaces functionality within GitHub.  You can access the files without an account, but will then need to interact with the code outside of GitHub.  We’ll provide more information about how you might do this later in this ReadMe document.
Navigate to https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github . This GitHub resource provides information about the process.  
Setup your GitHub account as described in the above link.

***Starting up a codespace from the template***
The ai_for_science_teacher_institute repository is a *template*.  It is reasonably simple to start up a codespace to run the files in the repository.  Here's how.

*1 Navigate to https://github.com/ArgonneEducation/ai_for_science_teacher_institute*

*2 Opening the template in a codespace*

Near the top right hand corner of the screen, find the button that says “Use this template” and click on it.
<br>
<img src="https://raw.githubusercontent.com/ArgonneEducation/ai_for_science_teacher_institute/refs/heads/main/imgs/use_this_template_open.png" alt="screen-grab" style ="width:200px;"/> 
<br>
Click on the “Open in a codespace” selection.

*3 Open a Jupyter Notebook*

To begin coding, you’ll have to open a jupyter notebook.  These are found in the navigation bar on the left of the screen.  Click on the word “notebooks” to see the files.  
<br>
<img src="https://raw.githubusercontent.com/ArgonneEducation/ai_for_science_teacher_institute/refs/heads/main/imgs/notebooks_1.png" alt="screen-grab" style ="width:300px;"/> 
<br>
Each of the files with a “.ipynb” designation is a python “jupyter” notebook that contains python code and markdown text.  If you’re just getting started, double click on the “01-jupyter_python_physics.ipynb” file.
<br>
<img src="https://raw.githubusercontent.com/ArgonneEducation/ai_for_science_teacher_institute/refs/heads/main/imgs/notebooks_2.png" alt="screen-grab" style ="width:300px;"/> 
<br>
This should open up this “notebook” in a new tab.

*4  Close the terminal - we don't need it*

The codespace automatically opens up a terminal at the *bottom* of the screen, which we are not going to use at this beginning level. Click in the bottom frame and type “exit” and "enter" to exit the terminal.  This will free up more of your screen to use for coding.
<br>
<img src="https://raw.githubusercontent.com/ArgonneEducation/ai_for_science_teacher_institute/refs/heads/main/imgs/exiting_terminal.png" alt="screen-grab" style ="width:500px;"/> 
<br>

*5 Select a Kernel (to run code)*

In order to “run” any of the code, we need to select a Kernel to use.  This essentially means we’re installing python files and setting up the particular version of python to use. Click to the “Select Kernel” button in the top right hand corner.
<br>
<img src="https://raw.githubusercontent.com/ArgonneEducation/ai_for_science_teacher_institute/refs/heads/main/imgs/select_kernel.png" alt="screen-grab" style ="width:700px;"/> 
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
<img src="https://raw.githubusercontent.com/ArgonneEducation/ai_for_science_teacher_institute/refs/heads/main/imgs/codespace_name_in_address.png" alt="screen-grab" style ="width:500px;"/> 
<br>
Simply closing out of the browser tab does not stop all activity in the codespace.  To do so, return to your GitHub home page and click on the hamburger menu (3 stacked horizontal lines) at the top left hand corner next to the cat icon. 
<br>
<img src="https://raw.githubusercontent.com/ArgonneEducation/ai_for_science_teacher_institute/refs/heads/main/imgs/codespace1.png" alt="screen-grab" style ="width:400px;"/> 
<br>
Then select “Codespaces” from the list that appears.
<br>
<img src="https://raw.githubusercontent.com/ArgonneEducation/ai_for_science_teacher_institute/refs/heads/main/imgs/codespace2.png" alt="screen-grab" style ="width:300px;"/> 
<br>
At the bottom of the page, you should see the name of your codespace.  
<br>
<img src="https://raw.githubusercontent.com/ArgonneEducation/ai_for_science_teacher_institute/refs/heads/main/imgs/codespace_name.png" alt="screen-grab" style ="width:700px;"/> 
<br>
You can shut it down by clicking on the 3 dots at the far right, and selecting “Stop codespace” . 
<br>
<img src="https://raw.githubusercontent.com/ArgonneEducation/ai_for_science_teacher_institute/refs/heads/main/imgs/codespaces_menu.png" alt="screen-grab" style ="width:300px;"/> 
<br>

 Your codespace should then no longer be Active.  You can restart your work from this page at any time.  You might also choose to open the notebooks from JupyterLab using this same menu.  JupyterLab has a different look and will match better with some of the content, as it was developed using JupyterLab!
