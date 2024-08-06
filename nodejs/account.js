class BalanceException extends Error{
    constructor(message){
        super(message);
        this.name = "BalanceException";
    }
}

class Account{
    constructor(name,type,balance){
        this.name=name;
        this.type=type;
        this.balance=balance;
    }
    withdrawAmount(wamt){
        if(wamt>this.balance){
            throw new BalanceException("Balance is low");
        }
        else{
            this.balance-=wamt;
            console.log(`Withdrawn. Your available balance is ${this.balance}`);
        }
    }
    depositAmount(dep){
        if(dep<=0){
            throw new BalanceException("Deposit low");
        }
        else{
            this.balance+=dep;
            console.log(`Deposited. Your available balance is ${this.balance}`);
        }
    }
    checkBalance(){
        if(this.balance<=0){
            throw new BalanceException("Low Balance");
        }
        else{
            console.log(`Your available balance is ${this.balance}`);
        }
    }
}
try{
    let a = new Account("Vivek","Savings",100);
    a.checkBalance();
    a.depositAmount(240);
    a.withdrawAmount(250);
}
catch(e){
    if(e instanceof BalanceException){
        console.error(`BalanceException: ${e.message}`);
    } else{
        console.error(`Unexpected error: ${e.message}`);
    }
}