file = open("death_causes.csv", "r")


index = 0
length_of_column = []
column_list = [] 
list_of_data = [] 

no_of_titles = 11

for each in file:
    list_of_data.append(each)    #appends the whole data into a list
    title_of_data = list_of_data[0].split(",")  #this returns the title of the data into a variable
    no_of_titles = len(title_of_data)  #no of title returned

def no_of_columns():   #this function returns the no of column under a title
    index = 0
    for each in file:
        column_item = each.split(",")[index]    
        column_list.append(column_item)     #this place the column items in a list
    length_of_column.append(len(column_list))  #this count the no of column after listing it
    

while index < no_of_titles:   
    index += 1         #this enable the code to loop through the next column
    no_of_columns()    #running the funtion again enable the next column to be counted
print(title_of_data)        
print(length_of_column)    

title_and_columns_dict = dict(zip(title_of_data,length_of_column))
print(title_and_columns_dict)

         

