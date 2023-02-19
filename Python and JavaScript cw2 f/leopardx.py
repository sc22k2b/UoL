"""
Please write your name
@author:

"""

# Reminder: You are only allowed to import the csv module (done it for you).
# OTHER MODULES ARE NOT ALLOWED (NO OTHER IMPORT!!!).

import csv


class Leopard:
    def __init__(self, filepath: str) -> None:
        
        self.data = []
        self.header = []
        
        try:
            with open(filepath, "r") as data:
                    reader = csv.reader(data)
                    i = 0
                    for row in reader:
                        if(i==0):
                            self.header = row
                            i = i +1
                        else:
                            self.data.append(row)
                            i = i + 1
            if not self.header:
                if not self.data:
                    print("empty file.")
        except FileNotFoundError:
            print("file not found.")
        
 

    def get_header(self) -> list:
        
        if not self.header:
            return("None")
        else:
            return(self.header)
            

    def get_data(self) -> list:
        
        if not self.data:
            return("None")
        else:
            return(self.data)

    def stats(self) -> dict:
        
        self.columns = {}
        
        self.statistics = {}
        
        header_length = len(self.header)
        
        for i in range(header_length):
            total = 0
            print(i)
            mean = 0
            count = 0
            integer_value = False
            minimum = 0
            maximum = 0
            for k in range(len(self.data)):
                count = count + 1
                if(self.data[k][i].isnumeric()):
                    integer_value = True
                    total = total + 1
                    
                    
                    data = int(self.data[k][i])
                    
                    mean = mean + data
                    
                    if(minimum == 0):
                        minimum = data
                    else:
                        if(int(minimum) > data):
                            minimum = data
                    if(maximum == 0):
                        maximum = data
                    else:
                        if(maximum < data):
                            maximum = data
                    
            
            if(integer_value is True):
                mean = mean/total
                mean = round(mean, 2)
                
                self.statistics.update({"count" : total})
                self.statistics.update({"mean" : mean})
                self.statistics.update({"min" : minimum})
                self.statistics.update({"max" : maximum})
                
                self.columns.update({self.header[i]:self.statistics})
                print(self.columns)
                
        return(self.columns)
        
        

    def html_stats(self, stats: dict, filepath: str) -> None:
        
        with open(filepath,"w") as html:
            
             html.write("<html>\n")
             html.write("<head>\n")
             html.write("<meta charset=\"UTF-8\">\n")
             html.write("<style>\n")
             html.write("table, th, td {\n")
             html.write("border: 1px solid black;\n")
             html.write("border-collapse: collapse;\n")
             html.write("}\n")
             html.write("</style>\n")
             html.write("</head>\n")
             html.write("<body>\n")
             html.write("<h2>Table of values:</h2>\n")
             html.write("<table>\n")
             
             for key in stats:
                 html.write("<tr>\n")
                 html.write("<th> ") 
                 html.write(key)
                 html.write(" </th>\n")
                 html.write("</tr>\n")
                 values = stats[key]
                 html.write("<tr>\n")
                 for key in values:
                     html.write("<td>")
                     html.write(str(values[key]))
                     html.write("</td>\n")
                
                 html.write("</tr>\n")
                
                
             html.write("</table>\n")  
             html.write("</body>\n")
             html.write("</html>\n")
            
            
                     
        
             
    def count_instances(self, criteria) -> int:
        """
        Write your docstring to explain how to use this method.
        You are to decide what data type format is criteria or how many
        arguments to this method.
        Delete above and this comment to write your docstring.
        """
        # delete pass and this comment to write your code
        pass


if __name__ == "__main__":
    # DO NOT COMMENT ALL WHEN SUBMIT YOUR FILE, cannot have an if statement
    # with nothing afterwards.

    '''# test diabetes_data.csv
    test = Leopard("diabetes_data.csv") #diabetes_data.csv
    print(test.get_header())
    print(test.get_data())
    stats = test.stats()
    print(stats)
    test.html_stats(stats, "diabetes.html")
    print()'''

    # test fide2021.csv
    test2 = Leopard("fide2021.csv")
    #print(test2.get_header())
    #print(test2.get_data())
    stats2 = test2.stats()
    print(stats2)
    test2.html_stats(stats2, "fide2021.html")
    print()

    '''# test student.csv
    test3 = Leopard("student.csv")
    print(test3.get_header())
    print(test3.get_data())
    stats3 = test3.stats()
    print(stats3)
    test3.html_stats(stats3, "student.html")'''
    
