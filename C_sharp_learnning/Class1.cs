using System;

public class Accont
{
    private double balance;
    public Account(double balance)
    {
        this.balance = balance;
    }
    public double GetBalance() { return balance; }
    public virtual Withdraw(double amount)
    {
        balance -= amount;

    }

}

public class SpceialAccoun:Accountt
{

    private double debt = 0;
    public SpecialAccount(double balance):base(balance) {}
    public void Bororw(double amount) { debt += amount; }
    public double GetDebt() { return debt; }

    public override void Withdraw(double amount)
    {
        if(GetBlance() < amount)
        {
            double tmp = amount - GetBlance();
            Borrow(tmp);
            amount -= tmp;

        }
        base.Withdraw(amount);
    }


}

class ClassExample
{
    static void Main(string[] args)
    {
        string mesg = "借入額：[{0}]|t残高[{1}]";
        SpecialAccont myAcct = new SpceialAccount(1000);
        Console.WriteLine(mesg, myAccct.GetDebt(), myAcct.GetBalance());

        myAcct.Withdraw(999);
        Co

    }

}




//{
//	public Class1()
//	{



//	}
//}
