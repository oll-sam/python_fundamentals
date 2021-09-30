#1
x = [ [5,2,3], [10,8,9] ] 
student = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
#(1)
x[1][0] = 15
print(x)
#(2)
student[0]['last_name'] = 'Bryant'
print(student)
#(3)
sports_directory['soccer'][0] = 'Adres'
print(sports_directory)
#(4)
z[0][0] = 30
print(z)

#2
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'},
    ]

def iterateDictionary(my_list):
    for i in range(0,len(my_list)):
        list = ""
        for key, val in my_list[i].items():
            list += key + "-" + val + " "
        print(list)

iterateDictionary(students)

def iterateDictionary2(key_name, some_list):
    for i in range(0,len(some_list)):
        print(some_list[i][key_name])

iterateDictionary2('first_name', students)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for i in some_dict:
        print(len(some_dict[i]), i)
        for j in some_dict[i]:
            print(j)

printInfo(dojo)