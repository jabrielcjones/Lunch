
public class Person 
{
	private String	last;
	private String	first;
	private String	email;
	
	public Person(String last, String first, String email)
	{		
		this.last = last;
		this.first = first;
		this.email = email;
	}
	
	public Person(String email)
	{
		this.email = email;
		this.first = null;
		this.last = null;
	}
	
	public String getLast()
	{		
		return this.last;
	}
	
	public String getFirst()
	{		
		return this.first;
	}
	
	public String getEmail()
	{		
		return this.email;
	}
	
	public void print()
	{
		System.out.println("\nLast Name: " + this.last + "\nFirst Name: " + this.first + "\nEmail: " + this.email + "\n");
	}
}
