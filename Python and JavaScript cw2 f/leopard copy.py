"""
Please write your name
@author:

"""

# Reminder: You are only allowed to import the csv module (done it for you).
# OTHER MODULES ARE NOT ALLOWED (NO OTHER IMPORT!!!).

import csv


class Leopard:
    def __init__(self, filepath: str) -> None:
        self.data = []  # Sets up an instance variable to hold the data (corresponding to a header)
        self.header = []  # Sets up an instance variable to hold the headers
        try:  # Sets up a try to try and read in the data
            with open(filepath, "r") as data:
                # Opens the file in read mode
                    reader = csv.reader(data)
                    # Allocates reader to hold the data read in
                    i = 0  # Sets up a count which will identify if the current row consists of headers or data
                    for row in reader:
                        # Loops for the rows in the read in data
                        if(i == 0):  # Checks to see if i == 0 and therefore it is a header
                            self.header = row  # Allocates the row to the header variable
                            i = i + 1  # Increments the count
                        else:
                            self.data.append(row)  # Allocates the row to the data variable
                            i = i + 1  # Increments the count
            if not self.header:  # Checks if the header variable is empty and therefore possibly there was an error
                if not self.data:  # Checks if the data variable is empty and therefore possibly there was an error
                    print("empty file.")  # As both header and data were empty the user is notified the file is empty
        except FileNotFoundError:  # Catches the exception that the file doesn't exist
            print("file not found.")  # Alerts the user that the file doesn't exist

    def get_header(self) -> list:
        if not self.header:  # Checks to see if header is empty
            return("None")   # Returns none as header is empty
        else:
            return(self.header)  # Returns the header as it is not empty

    def get_data(self) -> list:
        if not self.data:  # Checks to see if data is empty
            return("None")  # Returns none as data is empty
        else:
            return(self.data)  # Returns the data as it is not empty

    def stats(self) -> dict:
        columns = {}  # Sets up a new variable to hold the data
        header_length = len(self.header)  # Retrives the length of the header list
        for i in range(header_length):  # Loops for the length of the header list
            total = 0  # Sets up total to gather the number of data used
            mean = 0  # Sets up mean to hold the mean
            count = 0
            integer_value = False  # Holds whether the column is an integer column (or float)
            minimum = 0  # Holds the minimum value of a column
            maximum = 0  # Holds the maximum value of a column
            for k in range(len(self.data)):  # Loops for the length of the data list
                count = count + 1  # Increments the count
                if(self.data[k][i].isnumeric()):  # Checks to see if data is a number
                    integer_value = True  # Sets integer value to true as it is a number
                    total = total + 1  # Increases the total
                    data = int(self.data[k][i])  # Allocates the data
                    mean = mean + data  # Adds the data to the sum of numbers to be involved in the mean
                    if(minimum == 0):  # Checks to see if minimum hasn't changed as this would mean this is the first loop and therefore the first data is automatically the minimum
                        minimum = data  # Allocates the starting minimum
                    else:
                        if(int(minimum) > data):  # Checks to see if there is a new minimum
                            minimum = data  # Allocates the new minimum
                    if(maximum == 0): # Checks to see if maximum hasn't changed as this would mean this is the first loop and therefore the first data is automatically the maximum
                        maximum = data  # Allocates the starting maximum
                    else:
                        if(maximum < data):  # Checks to see if there is a new maximum
                            maximum = data  # Allocates the new maximum
                # The following elifs check for data that is still applicable
                # but that will not be counted in the calculations (e.g. mean)
                elif(self.data[k][i] == "NA"):
                    integer_value = True
                elif(self.data[k][i] == ""):
                    integer_value = True
                elif(self.data[k][i] == "-"):
                    integer_value = True
                else:
                    integer_value = False  # The data is not an integer value
                    break  # Exit the loop as a non integer has been found
            if(integer_value is True):
                mean = mean/total  # Calculates the mean
                mean = round(mean, 2)  # Rounds the mean
                columns[self.header[i]] = {"count": total, "mean": mean, "min": minimum, "max": maximum}
                # Adds the data to the columns dictionary
        return(columns)  # Returns columns

    def html_stats(self, stats: dict, filepath: str) -> None:
        with open(filepath, "w") as html:
            html.write("<html>\n")
            html.write("<head>\n")
            html.write("<meta charset=\"UTF-8\">\n")
            html.write("<style>\n")
            html.write("table, th, td {\n")
            html.write("border: 1px solid black;\n")
            html.write("border-radius: 6px; \n")
            html.write("border-collapse: collapse;\n")
            html.write("font-family: Arial; \n")
            #html.write("background-color: #0000FF; \n")
            html.write("box-shadow: 0 0 20px rgba(0, 0, 0, 0.15); \n")
            html.write("}\n")
            html.write("tr:nth-child(even){\n")
            html.write("background-color: #C6E2E9; \n")
            html.write("}\n")
            html.write("</style>\n")
            html.write("</head>\n")
            html.write("<body>\n")
            html.write("<h2>Table of values:</h2>\n")
            html.write("<table>\n")
            html.write("<tr>\n <th>")
            html.write(" ")
            html.write("</th>\n")
             
            header_count = 0
            iteration_count = 0
            for key in stats:
                header_key = key;
                values = stats[key]
                if(header_count == 0):
                    for key in values:
                        html.write("<th> ") 
                        html.write(key)
                        html.write(" </th>\n")
                        header_count = header_count + 1
                    html.write("<tr>\n")
                html.write("<td> \n")
                html.write(header_key)
                html.write(" </td>\n")
                iteration_count = iteration_count + 1
                for key in values:
                    html.write("<td>")
                    html.write(str(values[key]))
                    html.write("</td>\n")
                html.write("</tr>\n")
            html.write("</tr>\n")
            html.write("</table>\n")
            html.write("</body>\n")
            html.write("</html>\n")
    
    def retrieve_criteria(self) -> None:

        criterias = {}  # Sets up a dictionary to hold the criteria values
        for i in range(len(self.header)):  # Loops for the length of
            # The header list
            header = str(self.header[i])  # Allocates the header
            criteria = input("What criteria would you like to check for " + header + " (NA for no criteria): ")
            # Retrieves the input from the user (the criteria)
            criterias.update({self.header[i]: criteria})  # Adds the criteria
            # to the dictionary
        return(criterias)  # Returns the criterias
          
    def count_instances(self, criteria: dict) -> int:
        """
        This method takes a dicitonary (criteria) which holds
        all the criteria data each with corresponding keys which
        will be the headers associated with the data.
        Users can input the data by using the retrieve_criteria
        -> test?.count_instances(test?.retrieve_criteria())
        method which will ask for an input for each header.
        Users can allocate criterias to as many headers as they want
        (the number of headers available) and if they do not want to
        allocate a criteria to a header the user must input NA,
        any other value will be used as criteria
        """
        instances = 0  # Sets up a count for the number of instances
        for k in range(len(self.data)):  # Loops for the length of the
            # data list
            criteria_matched = False  # Sets up a boolean value
            # To identify if the criteria is matched
            if(criteria[self.header[0]] == self.data[k][0]):
                # Checks to see if the data matches
                for j in range(len(self.header)-1):
                    # Loops for the length of the header list -1
                    if(criteria[self.header[j+1]] == self.data[k][j+1]):
                        criteria_matched = True
                        # Assigns true as the criteria has been satisfied
                    elif(criteria[self.header[j+1]] == "NA"):
                        criteria_matched = True
                        # Assigns true as this header is not
                        # included within the criteria checking
                    else:
                        criteria_matched = False
                        break
                        # If criteria matched remains false this means
                        # data has not been found that matches all the
                        # criteria and therefore the loop should be
                        # exited
                if(criteria_matched is True):
                    instances = instances + 1
                    # Increaese the instances as a match has been found
            elif(criteria[self.header[0]] == "NA"):
                # Repeats the above however, the use of NA is checked
                # first so that if a user didn't want any criteria associated
                # with the first header the rest could still be checked
                for j in range(len(self.header)-1):
                    if(criteria[self.header[j+1]] == self.data[k][j+1]):
                        criteria_matched = True
                    elif(criteria[self.header[j+1]] == "NA"):
                        criteria_matched = True
                    else:
                        criteria_matched = False
                        break
                if(criteria_matched is True):
                    instances = instances + 1
        return instances  # Returns instances
    

if __name__ == "__main__":
    # DO NOT COMMENT ALL WHEN SUBMIT YOUR FILE, cannot have an if statement
    # with nothing afterwards.

    # test diabetes_data.csv
    test = Leopard("diabetes_data.csv") #diabetes_data.csv
    print(test.get_header())
    print(test.get_data())
    stats = test.stats()
    print(stats)
    test.html_stats(stats, "diabetes.html")
    print()


    # test fide2021.csv
    test2 = Leopard("fide2021.csv")
    #print(test2.get_header())
    #print(test2.get_data())
    stats2 = test2.stats()
    print(stats2)
    test2.html_stats(stats2, "fide2021.html")
    print()
    criteria = {"Rank":"2", "Name":"NA", "Title":"g", "Country":"USA", "Rating":"NA", "Games":"0", "B-Year":"NA"}
    test2.count_instances(test2.retrieve_criteria())

    # test student.csv
    '''test3 = Leopard("student.csv")
    print(test3.get_header())
    print(test3.get_data())
    stats3 = test3.stats()
    print(stats3)
    test3.html_stats(stats3, "student.html")
    test3.count_instances(test3.retrieve_criteria())'''