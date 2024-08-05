class Employee:
    def __init__(self,employeeName,department):
        self._employeeName=employeeName
        self._department=department
        
    @property
    def employeeName(self):
        return self._employeeName
    
    @employeeName.setter
    def employeeName(self,value):
        self._employeeName=value
        
    @property
    def department(self):
        return self._department
    
    @department.setter
    def department(self,value):
        self._department=value

e=Employee("Peter","Sales")
print(e.employeeName)
print(e.department)
    
    