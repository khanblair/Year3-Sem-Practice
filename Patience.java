
public class Patience {

    String staffName, staffId;
    int basicSalary, Tax;

    Patience(String name,String id,int salary, int tax){
        staffName = name;
        staffId = id;
        basicSalary = salary;
        Tax = tax;
    }

    void display(){
        System.out.println("Staff Name   : " + staffName);
        System.out.println("Staff Id     : " + staffId);
        System.out.println("Basic Salary : " + basicSalary);
        System.out.println("Tax          : " + Tax);
        System.out.println(" ");
    }

    public static void main(String[] args){

        Patience pat1 = new Patience("Tumwine Andrea", "MMU001", 1200000, 5000);
        Patience pat2 = new Patience("Karungi Mary", "MMU009", 5000000, 10000);
        Patience pat3 = new Patience("Bossa Ssejjoba", "MMU010", 400000, 1200);

        pat1.display();
        pat2.display();
        pat3.display();
    }

}