import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from collections import Counter

sns.set()
sns.set(style="darkgrid")

import warnings
warnings.filterwarnings("ignore")

print("Hi! This is a grapher :D")
print("Available functions: line, scatter, histogram, bargraph (numerical)")
print()
plotname = str(input("Select plot type: "))
plotnamecheck = True
while plotnamecheck == True:
    if "line" in plotname or "scatter" in plotname or "hist" in plotname or "bar" in plotname:
        plotnamecheck = False
        break
        print()     
    else: 
        print("Error! Select an option from the available functions.")
        plotname = str(input("Select plot type: "))
        print()
        



def wowdata(): 
  if "line" in plotname or "scatter" in plotname or "bar" in plotname:    
    new1 = float(input("Input " + name1 + " value (number):")) 
    new2 = float(input("Input " + name2 + " value (number):")) 
    newdict[name1].append(new1)
    newdict[name2].append(new2)
  elif "hist" in plotname:
    new1 = float(input("Input " + name1 + " value (number):")) 
    newdict[name1].append(new1)


name1 = str(input("Input X axis label: "))
name2 = str(input("Input Y axis label: "))
print()
newdict = {
    name1 : [],
    name2 : [],
}  
wowdata()

#CONT data Error bug fixed!
cont = str(input("Add new data point? (yes/no)"))
print()
contcheck = True
while contcheck == True:
    if "yes" in cont:
        wowdata()
        cont = str(input("Add new data point? (yes/no)"))
        print()  
    elif "no" in cont:
        contcheck = False
        datatypecheck = False
        print()
        break    
    else: 
        print("Error! Type either yes or no.")
        print()
        cont = str(input("Add new data point? (yes/no)"))

#checkplotname error check!


title = str(input("Input plot title: "))

tablequestion = str(input("Print table of data? (yes/no)"))
print()
tablecheck = True
while tablecheck == True:
    if "yes" in tablequestion:
        dataframe = pd.DataFrame(newdict)
        print(dataframe)
        print()  
        tablecheck = False
        break
    elif "no" in tablequestion:
        tablecheck = False
        print()
        break    
    else: 
        print("Error! Type either yes or no.")
        print()
        tablequestion =  str(input("Print table of data? (yes/no)"))

if "line" in plotname or "scatter" in plotname:
    sns.relplot(x=newdict[name1], y=newdict[name2], kind=plotname);
elif "hist" in plotname:
    binnumber = int(input("Number of bars/ranges in the histograph: "))
    frequency = Counter(newdict[name1])
    print(frequency)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.hist(newdict[name1])
    #bins are the number of bars
    sns.histplot(newdict[name1], kde=False, color="blue", bins = binnumber)
elif "bar" in plotname:
    barcolor = str(input("Input bar color:"))
    sns.barplot(x=newdict[name1], y=newdict[name2], color=barcolor);
else:
    pass
    
plt.title(title)
# ax.set_yticks(np.linspace(0, 10, 10))

plt.xlabel(name1)
plt.ylabel(name2)
plt.show()
