import seaborn as sns
import matplotlib.pyplot as plt
import csv

def read_csv():
    dct = {}
    with open("05-21-2021new.csv") as f:
        next(f)
        reader = csv.reader(f)
        for line in reader:
            city = line[2]
            if city in dct and line[3] == "US":
                dct[city].append(line)
            else:
                if line[3] == "US" :
                    dct[city] = [line]
        return dct     


def plot_bar(dct,states):
    if len(states) != 0:
        yvalues = []
        st= []
        for state in states:
            if state in dct:
                yvalues.append(dct[state])
                st.append(state)
        data = {'x':st,'y':yvalues}
        sns.barplot(x = 'x',y = 'y', data= data)
        plt.xlabel("US States")
        plt.ylabel("Number of deaths")
        plt.title("Number of deaths per State in the US")
        plt.savefig("death_plot.png")
    else:
        print("No state to plot the graph!")

def get_list_states():
    states = []
    print("Enter states, if you want to stop, press enter!")
    state = input()
    while state:
        states.append(state)
        state = input()
    return states


def get_nbconfirmed(dct):
    dct_new = {}
    for key in dct:
        confirmed = 0
        for i in dct[key]:
            confirmed+=int(i[7])
        dct_new[key] = confirmed
    key_max = max(dct_new, key=dct_new.get)
    key_min = min(dct_new, key=dct_new.get)
    print("The highest number of confirmed covid-19 cases is in",key_max+": "+str(dct_new[key_max])+ " cases.")
    print("The lowest number of confirmed covid-19 cases is in",key_min+": "+str(dct_new[key_min])+ " cases.")

def get_nbdead(dct):
    dct_new = {}
    for key in dct:
        dead = 0
        for i in dct[key]:
            dead+=int(i[8])
        dct_new[key] = dead
    return dct_new

def most_infect_city(dct):
    dct_new = {}
    for key in dct:
        val =  dct[key][0][7]
        val = int(val)
        for i in dct[key]:
            if int(i[7]) > val:
                val = int(i[7])
                name = i[1]
        dct_new[key] = [val,name]
    for i in sorted(dct_new):
        print("State: "+i+", City: "+dct_new[i][1]+", cases: "+str(dct_new[i][0]))

def survival_percentage(dct):
    dct_new = {}
    average = 0.0
    for key in dct:
        dead = 0
        cases = 0
        for i in dct[key]:
            dead+=int(i[8])
            cases+=int(i[7])
        dct_new[key] = [dead,cases]
    for i in sorted(dct_new):
        average = round((dct_new[i][0]/dct_new[i][1])*100,3)
        print("State: "+i+", mortality rate: "+str(average)+"%.")

def user_input():
    user_input = input("Instruction number: ")
    while user_input.isdigit()==False or int(user_input)<1 or int(user_input)>5:
        print("Wrong input! Select correct instruction numbers!!!")
        user_input = input("Instruction number: ")
    return int(user_input)

def get_answer(user,dct):
    deaths = get_nbdead(dct)
    if user == 1:
        states= get_list_states()
        plot_bar(deaths,states)
    elif user == 2:
        key_max = max(deaths, key=deaths.get)
        key_min = min(deaths, key=deaths.get)
        print("The highest number of deaths caused by covid-19 is in",key_max+": "+str(deaths[key_max])+ " deaths.")
        print("The lowest number of deaths caused by covid-19 is in",key_min+": "+str(deaths[key_min])+ " deaths.")
    elif user == 3:
        get_nbconfirmed(dct)
    elif user == 4:
        most_infect_city(dct)
    else:
        survival_percentage(dct)
    print()




def main():
    dct = read_csv()

    print("Hello, using this program, it is possible to analyse the Covid-19 Statistics in the US\n")
    name = input("What is your name? ")
    print()

    print("Dear",name,", in order to obtain the following information, select one of the instructions")

    while(True):
        print("1. The bar graph, illustrating number of deaths in the different States specified by user ")
        print("2. State with highest and lowest number of deaths in US")
        print("3. State with highest and lowest number of Covid-19 cases in the US ")
        print("4. The most infectioned city in each State in the US")
        print("5. Mortality rate of each state in the US")
        user = user_input()
        print()
        get_answer(user,dct)
        exit = input("Want to leave? Press 'y' to exit, otherwise press enter: ")
        if(exit == 'y'):
            break
        print()



if __name__ ==  "__main__":
    main()
