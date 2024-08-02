package algorithms;
public class fourth{
    public static void main(String args[]){
        WaitingTicket wt = new WaitingTicket("Blore","Chennai");
        System.out.println(wt.source);
    }
}

class Ticket{
    String source;
    String destination;
}
class WaitingTicket extends Ticket{
    String status;

    public WaitingTicket(String source, String destination) {
        this.source=source;
        this.destination=destination;
        this.status="Waiting";
    }    
}