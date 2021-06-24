# Trees - Ex3: Printing Number of Levels
class Organization:
    def __init__(self, ceo):
        self.ceo = ceo
        
    def print_num_levels(self):
        queue = [self.ceo]
        levels = 0
        while len(queue) != 0:
            for num_of_elem in range(len(queue)):
                node = queue.pop(0)
                queue += node.direct_reports
            levels += 1
        print(levels)
    
            
    class Employee:
        def __init__(self, name, title, direct_reports=[]):
            self.name = name
            self.title = title
            self.direct_reports = direct_reports
                

# Test 1            
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
org.print_num_levels()

# Test 2
I = Organization.Employee('I', 'Director')
H = Organization.Employee('H', 'Engineer')
G = Organization.Employee('G', 'Engineer')
F = Organization.Employee('F', 'Engineer')
E = Organization.Employee('E', 'Manager')
D = Organization.Employee('D', 'Manager', [F, G, H])
C = Organization.Employee('C', 'CTO', [D,E])
B = Organization.Employee('B', 'CFO', [I])
A = Organization.Employee('A', 'CEO',[B, C])
org = Organization(A)
org.print_num_levels()

'''
Output:
5
4
'''
