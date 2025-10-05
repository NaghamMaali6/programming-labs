package application ;

import java.util.* ;

public class MindMatch 
{
	public static void main(String args[])
	{
		Scanner scanner = new Scanner(System.in) ;  //create scanner object to read user input
		
		System.out.println("Welcome to MindMatch!") ;
		
		int choice ;
		int condition = 1 ;
		
		while(condition == 1)
		{
			DisplayMenu() ;
			choice = scanner.nextInt() ;  //read user's choice
			
			if(choice == 1)  //you guess computer's number
			{
				int target ;
				int guess = -1 ;
				
				Random rand = new Random() ;
				
				target = rand.nextInt(100) + 1 ;  //computer picks a number between 1 and 100 
				
				System.out.print("I have chosen a nember between 1 and 100 :) try to guess it.\n") ;
				
				while(guess != target)  //loop until the user guesses correctly 
				{
					System.out.print("Enter your guess:\n") ;
					
					guess = scanner.nextInt() ;  //read user's guess
					
					if(guess < target)
					{
						System.out.print("low!\n") ;  //tell the user that the guess is lower than the target
					}
					else if(guess > target)
					{
						System.out.print("high!\n") ;  //tell the user that the guess is higher than the target
					}
					else 
					{
						System.out.print("Correct!\n") ;
					}
				}
				
				System.out.print("----------------------------------------------------------------------\n") ;
				
				//worst-case time complexity = O(n) where n = number of guesses
			}
			else if(choice == 2)  //computer guesses your number
			{
				int l = 1 ;
				int h = 100 ;
				int mid ;  //variable to store computer's current guess  
				char response ;
				
				System.out.print("Think of a number between 1 and 100 and I will try to guess it.\nPlease respond with H(if my guess is higher than your number) , L(if my guess is lower than your number) or C(Correct guess).\n") ;
			
				while(l <= h)
				{
					mid = (l + h) / 2 ;  //computer guesses the middle of the current range
					
					System.out.print("is your number " + mid + " ?(H/L/C)\n") ;
					response = scanner.next().toUpperCase().charAt(0) ;  //read user's input , convert to upper-case and take only the one first character
					
					if(response == 'H')  //if computer's guess is higher than the number
					{
						h = mid - 1 ;  //move the higher limit down and look at smaller numbers
					}
					else if(response == 'L')  //if computer's guess is lower than the number
					{
						l = mid + 1 ;  //move the lower limit up and look at bigger numbers  
					}
					else if(response == 'C')
					{
						System.out.print("Yay! I guessed your number :)\n") ;
						break ;
					}
					else  //if the user typed something else than H , L or C
					{
						System.out.print("Invalid response! please try again with H , L or C only.\n") ;
					}
				}
				
				System.out.print("----------------------------------------------------------------------\n") ;
				
				//worst-case time complexity = O(log(n)) where n = number of guesses
			}
			else if(choice == 3)
			{
				System.out.print("hope you enjoyed the game :)\nBye!\n") ;
				break ;
			}
			else
			{
				System.out.print("Invalid option!!! please try again.\n") ;
			}
		}
		
		scanner.close() ;  //close the scanner to free resources
	}
	
	//method to display menu options :
	static void DisplayMenu()
	{
		System.out.print("please select an option(1-3):\n") ;
		System.out.print("1- you guess computer's number.\n") ;
		System.out.print("2- computer guesses your number.\n") ;
		System.out.print("3- Exit.\n") ;
	}
}
