# Trees - Ex2: Printing a Tree Level by Level
class Organization:
    def __init__(self, ceo):
        self.ceo = ceo
        
    def print_level_by_level(self):
        queue = [self.ceo]
        while len(queue) != 0:
            for num_of_elem in range(len(queue)):
                node = queue.pop(0)
                queue += node.direct_reports
                print('Name:', node.name, 'Title:', node.title)
            print()
    
            
    class Employee:
        def __init__(self, name, title, direct_reports=[]):
            self.name = name
            self.title = title
            self.direct_reports = direct_reports
                
# Test       
k = Organization.Employee('K', 'Sales Intern')
j = Organization.Employee('J', 'Sales Representative', [k])
i = Organization.Employee('I', 'Director', [j])
h = Organization.Employee('H', 'Engineer')
g = Organization.Employee('G', 'Engineer')
f = Organization.Employee('F', 'Engineer')
e = Organization.Employee('E', 'Manager')
d = Organization.Employee('D', 'Manager', [f, g, h])
c = Organization.Employee('C', 'CTO', [d,e])
b = Organization.Employee('B', 'CFO', [i])
a = Organization.Employee('A', 'CEO',[b, c])
org = Organization(a)
org = Organization(a)
org.print_level_by_level()

'''
Output:
Name: A Title: CEO

Name: B Title: CFO
Name: C Title: CTO

Name: I Title: Director
Name: D Title: Manager
Name: E Title: Manager

Name: J Title: Sales Representative
Name: F Title: Engineer
Name: G Title: Engineer
Name: H Title: Engineer

Name: K Title: Sales Intern

'''
