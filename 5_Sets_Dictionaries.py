# 1. Board of directors: Benny, Hans, Tine, Mille, Torben, Troels, Søren
#Management: Tine, Trunte, Rane
#Employees: Niels, Anna, Tine, Ole, Trunte, Bent, Rane, Allan, Stine, Claus, James, Lars

directors = {'Benny', 'Hans', 'Tine', 'Mille', 'Torben', 'Troels', 'Søren'}
management = {'Tine', 'Trunte', 'Rane'}
employees = {'Niels', 'Anna', 'Tine', 'Ole', 'Trunte', 'Bent', 'Rane', 'Allan', 'Stine', 'Claus', 'James', 'Lars'}

# who in the board of directors is not an employee?
# difference() method or '-' operator
not_employees = directors.difference(employees)
not_employees = directors - employees
print(not_employees)

# who in the board of directors is also an employee?
# intersection() method or '&' operator
employees_and_directors = directors.intersection(employees)
employees_and_directors = directors & employees
print(employees_and_directors)

#how many of the management is also member of the board?

management_board = management & directors
print(len(management_board))

#All members of the managent also an employee

management_employee = management & employees
print(management_employee == management)

#All members of the management also in the board?
print(management_board == management)

#Who is an employee, member of the management, and a member of the board?
man_board_emp = directors & employees & management
print(man_board_emp)

#Who of the employee is neither a memeber or the board or management?
emp = employees - directors - management
print(emp)

#######################################################################################
# 2. Using a list comprehension create a list of tuples from the folowing datastructure
# {‘a’: ‘Alpha’, ‘b’ : ‘Beta’, ‘g’: ‘Gamma’}

dict = {'a': 'Alpha', 'b' : 'Beta', 'g': 'Gamma'}

list = [(key, value) for key, value in dict.items()]
print(list)

#######################################################################################
# 3. From these 2 sets:
set1 = {'a', 'e', 'i', 'o', 'u', 'y'}

set2 = {'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}

# UNION
union = set1.union(set2)
union = set1 | set2
print(union)

# SYMMETRIC DIFFERENCE

symmetric_difference = set1.symmetric_difference(set2)
symmetric_difference = set1 ^ set2
print(symmetric_difference)

# DIFFERENCE

difference = set1.difference(set2)
difference = set1 - set2
print(difference)

# DISJOINT
are_disjoint = set1.isdisjoint(set2)
print(are_disjoint)

##########################################################################
# 4. DATE DECODER

months = {'JAN': '01',
              'FEB': '02',
              'MAR': '03',
              'APR': '04',
              'MAY': '05',
              'JUN': '06',
              'JUL': '07',
              'AUG': '08',
              'SEP': '09',
              'OCT': '10',
              'NOV': '11',
              'DEC': '12'}


def decode_date(date_str):
    day, month_str, year = date_str.split('-')
    month = months[month_str.upper()]
    
    if int(year) < 30:
        year = '20' + year
    else:
        year = '19' + year
    
    return (int(year), int(month), int(day))

print(decode_date('21-MAR-23'))