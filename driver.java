import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.PrintWriter;
import java.util.Random;
import java.util.Scanner;

public class driver 
{
	public static void main(String[] args) throws Exception
	{		
		int			seats = 0;
		String		emails = "", previous = "";
		Person[]	attendees = null;
		
		try
		{
			seats = Integer.parseInt(args[0]);
			
			emails = args[1];
			
			previous = args[2]; 
									
			// Randomly extract a name and an email from file
			File 		emailFile = new File(emails);
			File		previousFile = new File(previous);
					
			attendees = selectAttendees(seats, emailFile, previousFile);
			
			// Output results
			if (attendees != null)
				output(attendees);
			else
				System.out.println("No attendees were selected.");
			
		}
		catch (ArrayIndexOutOfBoundsException e)
		{
			System.out.println("You made a mistake: The arguments must be an integer and two file names, respectively.");
		}
		catch (NumberFormatException e)
		{
			System.out.println("You made a mistake: The arguments must be an integer and two file names, respectively.");
		}
		catch (Exception e)
		{
			System.out.println("You made a mistake: The arguments must be an integer and two file names, respectively.");
		}
	}
	
	public static Person[] selectAttendees(int seats, File emailFile, File previousFile) throws Exception 
	{
		Person[] attendees = new Person[seats];
		
		if (emailFile.exists() && emailFile.isFile() && previousFile.exists() && previousFile.isFile())
		{				
			Scanner		emailInput, prevInput;
			FileWriter	prevOutput;
			String		last, first, email, pEmail;
			boolean		onPrev = false;
			
			
			emailInput = new Scanner(emailFile);

			// Randomly extract prospective attendee
			String prospect = new String(choose(emailFile));
			
			for (int i = 0; i < seats && emailInput.hasNext();)
			{				
				email = new String(prospect.substring(prospect.indexOf("<")));
				
				prevInput = new Scanner(previousFile);	
				prevOutput = new FileWriter(previousFile, true);
				while (prevInput.hasNext())
				{
					pEmail = prevInput.next();
					
					if (email.equals(pEmail))
					{
						onPrev = true;
						break;
					}
					else
					{
						onPrev = false;
					}					
				}
				prevInput.close();
				
				if (!onPrev)
				{
					prevOutput.write(email + "\n");
					attendees[i] = new Person(email);
					i++;
				}
				prevOutput.close();
				prospect = new String(choose(emailFile));
			}
			
			emailInput.close();
		}
		else
		{
			System.out.println("You made a mistake: The arguments must be an integer and two text files, respectively.");
			System.exit(0);
		}
		
		return attendees;
	}

	private static void output(Person[] attendees) 
	{
		for (int i = 0; i < attendees.length; i++)
			System.out.println(attendees[i].getEmail() + "\n");
		
		System.out.println("------------------------------\n");
		System.out.println("Attendees List Updated: [prev-attendees.txt]");
	}

	public static String choose(File f) throws FileNotFoundException
	{
	     String result = null;
	     Random rand = new Random();
	     int n = 0;
	     for(Scanner sc = new Scanner(f); sc.hasNext(); )
	     {
	        ++n;
	        String line = sc.nextLine();
	        if(rand.nextInt(n) == 0)
	           result = line;         
	     }

	     return result;      
	}
}