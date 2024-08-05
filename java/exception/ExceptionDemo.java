class ExceptionDemo{
    public static int divide(int a, int b){
        return a/b;
    }
    public static void main(String args[]){
        try{
            int div = divide(1,0);
            System.out.println(div);
        }
        catch(ArithmeticException e){
            System.out.println("Cannot be divided by zero");
        }
        finally{
            System.out.println("Finally executed");
        }
    }
}