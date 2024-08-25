'''Python section'''

# 1. What is decorator , write a decorator?
'''Decorater is a function which can take a function as argument 
and extend its functionality and return modified function with extend functionality.'''


def decor(greetings):
    def inner(name):
        if name == "Prasad":
            print("its morning, dont be lazy")
        else:
            greetings(name)

    return inner


@decor
def greetings(name):
    print("Hello", name, "Good morning")


greetings('Pranesh')
greetings('Prasad')

# 2. What is lambda expression, write a lambda expression?
'''
Sometime we can declare a function without any name
such type of nameless function are called Lambda Function or anonymous function.
'''
sum = lambda a, b: a + b
print(sum(10, 20))

# 3. WAF, S = ‘Hello everyone’, count the occurrence of each char, return those
# repetitive character , without using any inbuilt function.

s = 'hello everyone'

# 4. WAF , Reverse a string words.
# > Input = ‘hello world’ > output:- ‘world hello’, without using inbuilt function

# 5. WAF, input= ‘aaabbaacd’ output= ‘3a2b2a1c1d’

# 6. Sort a list integer element without using inbuilt function?

# 7. Li = [1,2,3,4], Li2 = [10,20,30]
# Result = {1:10,2:20,3:30}
# Take a two list a parameter, return dictionary, look like above result.

Li = [1, 2, 3, 4]
Li2 = [10, 20, 30]


def convertdict(keys, values):
    return dict(zip(keys, values))


Li = [1, 2, 3, 4]
Li2 = [10, 20, 30]
result = convertdict(Li, Li2)
print(result)

# 8. Handel a csv file, write first_name , email, phn_no, insert 5 data in this csv, then read
# the csv and print in console bar

import csv

data = [{"first_name": "Pranesh", "email": "Pranesh@xyz.com", "phn_no": "1234567890"},
        {"first_name": "Ashish", "email": "Ashish@xyz.com", "phn_no": "2345678901"},
        {"first_name": "John", "email": "John@xyz.com", "phn_no": "3456789012"},
        {"first_name": "Prasad", "email": "Prasad@xyz.com", "phn_no": "4567890123"},
        {"first_name": "Nishi", "email": "nishi@xyz.com", "phn_no": "5678901234"}]

file_path = 'contacts.csv'
with open('contacts.csv', 'r') as file:
    read = csv.reader(file)
    for row in read:
        print(row)

# 9. What is exception handling , how handel the exception in python , explain with each block

'''An unwanted and unexcepted event that distrubs normal flow of program is called  Exception.
We have to define alternative way to continue rest of the program normally.
The main objective of exception handeling is graceful Termination of the program.

1. TRY block:- Code that may cause an exception
2. EXCEPT block :- It means code will if the exception occurs in the try block
3. ELSE block:- Code will run if no exception occurred and this is optional block 
4. FINALLY block:- this block will execute no matter if exception occures or not.'''

# 10. Difference between Module and Packages (3 diff)

'''
Module: Module is a single file with Python code. 
        It can define functions, classes, and variables.
        it is imported by filename.

Package: A directory containing multiple modules and __init__.py file.
        It’s like a folder that contains multiple modules.
        it is imported by directory name, and modules in it are visible
'''

# 11. Difference between List vs tuple vs set vs dictionary?

'''
List:   it is a mutable data type. 
        You can modify, add, or remove elements in the list
        Can contain duplicate items.


Tuple:  It is immutable data type. 
        its elements cannot be changed.
        Can contain duplicate items.

Dictionary: It is mutable data type
            Keys are unique and used to access values.

set:    No duplicate items are allowed.
        Items can be added or removed, but not modified.
'''

# 12. What is Garbage Collection?
'''Garbage collection is like cleaning up a extra occupied space.
It removes items that are no longer needed, so they don’t take up space.

for e.g:

list =[1,2,3,4,5]

list = [Pranesh, Prasad, Nishi]

so it will automatically detects the unwanted memory and puts it into garbage which is list= [1,2,3,4,5]
'''

# 13. What is list comprehension , write code in list comprehension?

'''
List comprehension offers a shorter syntax when you want to create 
a new list based on the values of an existing list
'''

li = [i ** 2 for i in range(1, 6)]

# 14. Difference between Shallow copy vs Deep Copy?
'''
Shallow copy:- Copies the outer object and references to inner objects 
and changes to inner objects affect both the original and the copy.

Deep copy: It Copies both the outer object and all inner objects and
changes to any part of the copy do not affect the original.
'''

# 15. Explain break, continue, pass with code?
'''
break: it exits the loop immediately .
continue: it skips the rest of the current iteration and moves to the next iteration.
pass: it is a placeholder that does nothing but it is used to fulfill syntax requirements or as a placeholder.
'''

'''Selenium Section'''

# 1. What is webdriver?
'''
WebDriver is a tool that allows you to automate web browsers. 
It allows you to programmatically interact with a browser, perform actions like clicking buttons, filling out forms,
and navigating between pages, which is useful for tasks such as testing web applications.
For example, you can use webDriver to:
open a web page
click on buttons
fill out forms
check the content on a page
'''

# 2. How to handel selective dropdown, write a snippet for it?
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('https://xyz.com')

dropdown_element = driver.find_element(By.ID, 'dropdown')

select = Select(dropdown_element)

select.select_by_visible_text('Option Text')
driver.quit()

# 3. How to handel auto suggestive dropdown, write a snippet for it.?
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://xyz.com')

input_field = driver.find_element(By.ID, 'input-anything')
input_field.send_keys('searchanything')
time.sleep(2)

suggestion = driver.find_element(By.XPATH, '//ukajsi36rr823yor')
suggestion.click()
driver.quit()

# 4. How to handel multiple windows and back to current window?
'''Handling multiple windows or tabs can be done by using switching between them 
like for example their is specific method called switch_to.window'''

driver.switch_to.window(window_handles[0])

# 5. What StaleElementException?
'''StaleElementException is an error in Selenium that occurs when a web element you’re trying 
to interact with is no longer present in the DOM of the page.'''

# 6. Explain the wait mechanism, write syntax and snippet for it.
'''
In selenium, the wait mechanism is used to handle where elements on a web page take time to appear.
there are  tyopes of waits:
1. implicit wait: it automatically waits for a set time for all elements to appear. 
if you set it once and it applies to all searches.
syntax: driver.implicitly_wait(time_in_seconds)
2. explicit wait: it waits for specific conditions or elements with more control
and you can define how long to wait.

wait = WebDriverWait(driver, 10)  
element = wait.until(EC.element_to_be_clickable((By.ID, 'element-id')))
'''

# 7. How to handle dynamic web element, (write at least 3 point)

# 8. How many locators in selenium
'''
1. ID
2. NAME
3. CLASS NAME
4. TAG NAME
5. LINK  TEXT
6. PARTIAL LINK TEXT
7. XPATH
8. CSS SELECTOR
'''

# 9. In web table want to fetch 3rd Column , 3rd row data, write a xpath for it.
'''XPATH = '//table/tbody/tr[3]/td[3]
 driver.find_element(By.XPATH, '//table/tbody/tr[3]/td[3]')'''

# 10. Write xpath
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.nseindia.com/')
path = driver.find_element(By.XPATH, '//')
driver.quit()

'''SQL section'''
# 1. Explain about the DML,DDL,TCL,DQL commands?
'''
DQL -Data Query language -- its used retrieve/fetch/display/view/read - SELECT
DDL -Data definition language -- its used (create,alter,drop, truncate, Rename)
DML -data manupulation language -- its used to modify the db (INSERT ,UPDATE, DELETE)
TCL -tranction control language (commit , rollback, savepoint)
'''
# 2. What is join, explain about the all joins?
'''Inner join:
Inner join return only matching records from the table.

Left join:
It will display all records from the left table and matching records from right table 
and for non matching records it will display nulls values.

Right join:
It will display all records from the right table and matching records from left table 
and for non matching records it will display nulls values.

Full join
It will display all records from the both tables if it's matching or not matching 
and for non matching records it will display nulls values.

self join
It combines a table on itself.

equi join
If you are noy joining using join keyword while joining two tables then it's called equi join
'''
# 3. Difference between Joins vs Subquery?
'''
Joins: joins combine rows from two or more tables based on a related column between them. 
subqueries: it is nested queries used to filter or derive results n best for complex conditions and calculations.'''

# 4. Find 3rd Highest Salary Of employee table ?
'''
With cte as
(SELECT *, DENSE_RANK()OVER(PARTITION BY DEPT ORDER BY SALARY DESC) AS RNK FROM EMPLOYEE)
select * from cte where rnk = 3;
'''
# 5. Find the top seller in this month, according to date in customer table?
'''
SELECT customer_id, SUM(sale_amount) AS total_sales
FROM customer
WHERE EXTRACT(MONTH FROM sale_date) = EXTRACT(MONTH FROM CURRENT_DATE)
  AND EXTRACT(YEAR FROM sale_date) = EXTRACT(YEAR FROM CURRENT_DATE)
GROUP BY customer_id
ORDER BY total_sales DESC
LIMIT 1;
'''

# 6. Difference between Rank vs Dense_rank?
'''
RANK(): Rank function will skip the ranking if there is a same value or number.
DENSE_RANK(): Dense_rank will not skip the ranking if there is a same value or number.
'''

'''UNIX section'''

# 1. Copy a file one directory to another directory?
'''cp [source_file] [destination_directory]'''

# 2. How do you find the process IF(PID) of a running process.
'''ps -e | grep process_name'''

# 3. difference between chown vs chmod?
'''
chown (change owner): Changes the owner and/or group of a file or directory
chmod: Changes the permissions (read, write, execute) of a file or directory.
'''

# 5. Why we are using sed command?
'''to replace specific text patterns in a file.
To delete lines or text that match a certain pattern.'''

# 6. How to list directories in Unix?
ls -d */
