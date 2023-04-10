# Exception Handling. 
'''
When scraping data from the web, you will often encounter errors that will cause your program to crash.
An example will be when scraping data that has mixed data types. We see in `new_list` that we have a string and integers.
When we run this code, it will execute for the first three elements in the list but then throw and error on the str and 
crash the program. This will end the operation, the scraper will not be able to continue and will not be able to export
the data to a CSV file.
'''
new_list = [2,4,6, 'California', 8, 'Oregon', 9, 10]

for element in new_list:
    try:
        print(element/2)
    except:
        print("The element is not a number!")
    
# While-Break
n = 4
while n > 0: 
    print(n)
    n = n-1
    if n==2:
        break
    
print('Loop ended')   