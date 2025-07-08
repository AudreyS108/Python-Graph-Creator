# Python Graph Creator
This project is called Python Graph Creator.  
It is my first project submission for the Athena Award.   
This project is designed to let the user create a plot/graph easily! It's simple to customize, and also simple to set up. 
This code allows the user to input their own x and y values. and create a graph with the data.
__________________________________________________________
What It Does:
-
This Python program performs a multitude of functions. They include:  
* Creating a variety of graphs (available functions: line graph, scatter plot, histograph, bar chart (numerical))  
* Creating a table using the given datapoints inputted by the user, which will appear with the created graph   
* Allowing the user to set x and y labels for their graph    
* Allowing the user to set a relevant title for their graph  
__________________________________________________________
How To Operate:
- 
1. Open the file in "releases"
2. TBC

 **Alternate operating methods (only if above method fails!)** 
<details>
<summary></summary>

1. Press the green "Code" button. Select "Local" and then "Download ZIP"
   
> ![Step1](https://github.com/user-attachments/assets/f273659e-e287-4748-b895-fa7923775d2d)

2. Unzip/extract the downloaded ZIP folder
   
3. If you use Jupyter Notebook, follow these steps:
   
> Open Jupyter Notebook, open a new terminal and input the following code:

> ```pip install pandas```

> ```pip install matplotlib```   
> ```pip install seaborn```  
> ```pip install counter ```  
> (These commands are used to install the needed Python Libraries in order for the code to run as it should.)   
> After installing all of these libraries, in Jupyter Notebook, open the unzipped/extracted folder, click in "Python-Graph-Creator-main", then "pythongraphcreator"  
>  Open the file which is of the file type *.ipynb*  
> You can now use the graph creator! Press the triangle button to start, and guided steps should show up in the output. Simply type your answers in the output to create your graph.  
> ![Screenshot_28-6-2025_173950_localhost](https://github.com/user-attachments/assets/ed29d611-568e-4449-8c92-51bb428c9864)
4. If you use VS code or other code editor, follow these steps:
> Open VS Code, then through VS Code, open the unzipped/extracted folder, click in "Python-Graph-Creator-main", then "pythongraphcreator"  
> Open the file which is of the file type *.py*
> In the terminal, input the following code:
> ```pip install pandas```    
> ```pip install matplotlib```    
> ```pip install seaborn```  
> ```pip install counter ```
> (These commands are used to install the needed Python Libraries in order for the code to run as it should.)
> You can now use the graph creator! Run the code, and guided steps should show up in the terminal. Simply type your answers in the terminal to create your graph.  
> ![Screenshot 2025-06-28 181307](https://github.com/user-attachments/assets/a3dd883a-2c20-4cae-9b2b-45c333237c36)
</details>

__________________________________________________________
Personal Project Evaluation and Reflection:
-
I decided to make this project while I was in science class. At the time, our class was learning how to create accurate graphs to represent a data set. This prompted me to think: "I wonder if I could make something that could make a graph for me, without me having to individually plot each data point?" A year ago, I was (and still am) aspiring to become a data scientist, and wanted find a career linked to data analysis. Because of this, I had begun a Python for Data Science course a few months back. At the end of the course, I felt that I should put my newly nurtured skills to practice! Luckily, I was fortunate enough to be told about the Athena Award by Hack CLub. Coding 3 projects for 30 hours, utilizing my programming skills, and possibly meeting like-minded individuals along the way? How could I possibly turn that down? After I received the message, I signed up and focused my first project on Python, data, and graphs - which became this project, Python Graph Creator.
__________________________________________________________
This project was made by using the Python libraries Matplotlib, Seaborn, Pandas and Counter. I used the code editor Jupyter Notebook when making this project.
* Matplotlib and Seaborn: Used for creating graphs with the given datapoints the user inputted.
* Pandas: Used to clean data and format dataset into a table.
* Counter: Used to determine the frequency of certain values in a dataset (used to create the histograms)
__________________________________________________________
Throughout the creation of my project, I was challenged by multiple issues.
* Issue 1: Before, the ticks on the axis of the graph would not be in ascending order. I fixed this by converting the input to a float input so that the Matplotlib library could read the inputted number and plot the graph correctly.  
* Issue 2: When testing, I would occasionally input an option which wasn't intended (e.g. entering a typo for a question which required the user to input something), which would cause the code to crash because such option would not exist and therefore the code for plotting the graph would not work. To fix this, I coded a function where if either the answers "yes" or "no" weren't given, the code would send an error to the user in the terminal or output and tell the user to re-enter their response. This provided convenience for the user. 

By overcoming these challenges, I had developed many skills. For example, I enhanced my knowldege of dataframes, and learned to handle data using libraries such as Pandas and Matplotlib. Another skill I advanced was my use of loops. This happened when I was adjusting the part which allowed a user to select yes/no to input multiple datapoints, I used while (variable) = True loops to let the user input as many data points as they wanted (until the user selected no, and the True variable would be set to False and the loop would be broken.)

Overall, creating this project has led me to enhance many of my coding skills in Python, through solving various challenges.
__________________________________________________________
Project Stats:
-
* Time spent: 10 hours 50 minutes  
* Code editor used: Jupyter Notebook
* Coding language(s): Python  
__________________________________________________________
Contact Information
-
Please email **audrey.shi108@gmail.com** for any inquiries, or message **AudreyS108** on Slack. :D
