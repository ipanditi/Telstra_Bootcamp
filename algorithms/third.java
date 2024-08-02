package algorithms;

public class third {
    public static void main(String args[]){
        Item i1 = new Item("Coffee",24,10);
        Item i2 = new Item("Tea",24,10);
        Item i3 = new Item("Dosa",24,10);
        System.out.println(i1.itemName);
        System.out.println(i2.itemName);
        System.out.println(i3.itemName);
    }
}
class Item{
    String itemName;
    int price;
    int quantity;
    Item(String itemName, int price, int quantity){
        this.itemName=itemName;
        this.price=price;
        this.quantity=quantity;
    } 
}