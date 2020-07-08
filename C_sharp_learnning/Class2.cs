using System;

public class MyDog:Mammal
{
	static void Main(string[] args)
    {
		MyDog myDog = new MyDog("コロ", 3);
		Console.WriteLine(myDog.GetNmae() + ":" + myDog.Cry());
    }
}

public class Mammal
{
	private string name;
	private int age;
	private string cry;	

	public Mammal(string name, int Cry) {
		this.name = name;
		this.age = age;

	}

	public string GetName()
    {
		return name;
    }

	public string Cry()
	{
		return name;
	}




	public string GetAge()
{
	return age;
}

}