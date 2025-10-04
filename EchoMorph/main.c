/*
  EchoMorph: Reforge your name into new forms.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <time.h>

//function Definition:
/*1*/void DisplayMenu() ;
/*2*/char* getName() ;

int main()
{
    srand(time(NULL)) ;  //set random seed using current time so results change each run

    printf("Welcome to EchoMorph :) \nwhere every name has another face!\n\n");

    int x ;
    int c ;

    char* Name ;

    char T[6][10] = {"PRIME" , "BLADE" , "GEAR" , "TRON" , "BOT" , "MECH"} ;

    c = 1 ;

    while(c == 1)
    {
        DisplayMenu() ;

        scanf("%d" , &x) ;

        if(x == 1)
        {
            //transformer name
            Name = getName() ;
            //printf("%s\n" , Name) ;  //to check getName function

            int index = rand() % 6 ;  //pick random number between 0 and 6
            int p = rand() % 2 ;  //pick randomly between 0 and 1

            if(p == 0)
            {
                printf("your transformer name is %s%s\n" , Name , T[index]) ;
            }
            else
            {
                printf("your transformer name is %s%s\n" , T[index] , Name) ;
            }

            printf("-----------------------------------\n") ;
        }
        else if(x == 2)
        {
            //reverse name
            Name = getName() ;
            //printf("%s\n" , Name) ; //to check getName function

            Name = strrev(Name) ;  //strrev() function used to reverse a string
            printf("your name is reversed : %s\n" , Name) ;

            printf("-----------------------------------\n") ;
        }
        else if(x == 3)
        {
            //shuffle name
            Name = getName() ;
            //printf("%s\n" , Name) ;  //to check getName function

            int S = strlen(Name) ;  //find name length

            char shuffle ;

            for(int i = (S - 1) ; i > 0 ; i--)  //loop from end
            {
                int j = rand() % (i + 1) ;  //pick random number between 0 and i

                //swap ...
                shuffle = Name[i] ;
                Name[i] = Name[j] ;
                Name[j] = shuffle ;
            }

            printf("your name is shuffled: %s\n" , Name) ;

            printf("-----------------------------------\n") ;
        }
        else if(x == 4)
        {
            //exit program
            printf("thank u for using EchoMorph :)\nBye!\n") ;
            break ;
        }
        else
        {
            printf("invalid option!!!\n") ;
            printf("try again :)\n") ;
        }
    }

    return 0;
}

void DisplayMenu()
{
    printf("please select an option(1-4):\n") ;
    printf("1- convert to Transformer name\n") ;
    printf("2- reverse name\n") ;
    printf("3- shuffle name\n") ;
    printf("4- Exit\n") ;
}

char* getName()
{
    static char N[20] ;  //static keeps this array in memory even after the function ends, so the pointer we return will still point to valid data. and without it the array would disappear when the function finishes.
    int i ;

    printf("please enter your name\n") ;
    scanf("%s" , N) ;  //get user input

    for(i = 0 ; i < strlen(N) ; i++)
    {
        N[i] = toupper(N[i]) ;  //convert the whole name to uppercase
    }

    return N ;
}


//worst-case time complexity = O(n) where n = length of the name
