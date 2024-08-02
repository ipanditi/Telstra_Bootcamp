package algorithms;

public class second {
    public static void main(String args[]){
        Employee emp1 = new Employee("Vivek",12);
        System.out.println(emp1.employeeId);
    }
}
class Employee{
    String employeeName;
    int employeeId;
    Employee(String employeeName, int employeeId){
        this.employeeId=employeeId;
        this.employeeName=employeeName;
    } 
}
