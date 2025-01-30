```markdown
# Code Explanation: Password Generator and Strength Checker

This C code is designed to both evaluate the strength of a user-provided password and generate a strong, random password. Let's break it down step-by-step:

## 1. Header Files

```c
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<time.h>
```

-   **`stdio.h`**: This header provides standard input/output functions like `printf` (for printing to the console) and `scanf` (for reading input from the console).
-   **`string.h`**: This header provides functions for working with strings, such as `strlen` (to get the length of a string).
-   **`stdlib.h`**: This header provides general utility functions, including `rand` (for generating random numbers), `srand` (for seeding the random number generator), and `system` (to execute shell commands).
-   **`time.h`**: This header provides time-related functions, which we'll use to seed the random number generator to make sure that we get a unique random password each time we run the program.

## 2. `swap` Function

```c
void swap (char *p1, char*p2)
{
    //swapping the characters
    char temp = *p1;
    *p1 = *p2; 
    *p2 = temp;
}
```

-   This function takes two character pointers (`p1` and `p2`) as input.
-   It swaps the characters that `p1` and `p2` are pointing to.
-   This is done by creating a temporary variable `temp`, storing the value of `*p1` in it, assigning the value of `*p2` to `*p1`, and finally assigning the value of `temp` to `*p2`.

## 3. `calculate_strength` Function

```c
int calculate_strength(char *password)
{
    //initialise all the counters to zero
    int num = 0;
    int lower_case = 0;
    int upper_case = 0;
    int special_char1 = 0;
    int special_char2 = 0;
    int invalid = 0;

    int count[6]; 
    //checking number of characters of each category for the entered password
    for(int i = 0; i<10; i++)
    {
        if(password[i] >= '0' && password[i]<='9') 
            num++;
        else if(password[i]>='a'&& password[i]<='z') 
            lower_case++;
        else if(password[i]>='A' && password[i]<='Z') 
            upper_case++;
        else if(password[i] == '?' || password[i] == '-' || password[i] == '+' || password[i] == '=') 
            special_char1++;
        else if(password[i] == '!' || password[i] == '@' || password[i] == '#' || password[i] == '$') 
            special_char2++;
        else 
            invalid++;
    }

    int special_char = special_char1 + special_char2;

    count[0] = num;
    count[1] = lower_case;
    count[2] = upper_case;
    count[3] = special_char1;
    count[4] = special_char2;

    int type = 0;

    for(int i = 0; i<3; i++)
    {
        if(count[i]!=0)
            type++;
    }
    if(special_char!=0) type++;

    //int has_num_twice = num >= 2;

    //returning the strength of password
    if (invalid !=0)
        return -1;
    else if (type == 1) 
        return 50;
    else if (type == 2) 
        return 65;
    else if (type == 3) 
        return 75;
    else if (special_char1 == 0 || special_char2 == 0)
        return 85;
    
    int has_two_num = (num == 2);
    int has_two_lower = (lower_case == 2); 
    int has_two_upper = (upper_case == 2);
    int has_two_char1 = (special_char1 == 2);
    int has_two_char2 = (special_char2 == 2);

    if(has_two_char1 && has_two_char2 && has_two_lower && has_two_num && has_two_upper)
        return 100;
    else 
        return 95;
}
```

-   This function takes a password string as input and determines its strength based on the types of characters it contains.
-   It initializes several counters: `num` (for digits), `lower_case`, `upper_case`, `special_char1` (for '?','-','+','='), `special_char2` (for '!','@','#','$'), and `invalid` (for any characters that are not allowed).
-   It iterates through the password, checking each character:
    -   If it's a digit (0-9), it increments `num`.
    -   If it's a lowercase letter (a-z), it increments `lower_case`.
    -   If it's an uppercase letter (A-Z), it increments `upper_case`.
    -   If it's one of '?','-','+','=', it increments `special_char1`.
    -  If it's one of '!','@','#','$', it increments `special_char2`.
    -   If it's any other character, it increments `invalid`.
-   It then calculates the total number of special characters (`special_char`).
-   It counts the number of different *types* of characters present in the password, and stores the count in variable `type`
-   Based on the character counts and the value of `type`, it assigns a strength score:
    -   If the password contains invalid characters return -1.
    -   If only 1 type of character is present, the password strength is 50.
    -   If 2 types of character is present, the password strength is 65.
    -   If 3 types of character is present, the password strength is 75.
    -   If both special char 1 and char 2 are not present, the password strength is 85.
    -   If the password has exactly two numbers, two lowercase letters, two uppercase letters, two special char 1 and two special char 2 then the strength is 100, else strength is 95.
- It then returns the calculated password strength.

## 4. `generate_password` Function

```c
void generate_password() 
{ 
    //creating arrays for different sets of characters
    char numbers[] = "0123456789"; 
	char lower_case[] = "abcdefghijklmnoqprstuvwyzx"; 
	char upper_case[] = "ABCDEFGHIJKLMNOQPRSTUYWVZX"; 
	char special_char1[] = "?-+=";
    char special_char2[] = "!@#$";


    char password[10];
    //selecting two characters from each array
    int j = 0;
    for(int i = 0; i<2; i++)
    {
        password[j++] = numbers[rand()%10];
        password[j++] = lower_case[rand()%26];
        password[j++] = upper_case[rand()%26];
        password[j++] = special_char1[rand()%4];
        password[j++] = special_char2[rand()%4];
    }

    //shuffling the array
	for (int i = 9; i > 0; i--)
	{
		int k = rand() % (i+1); // Pick a random index from 0 to i
		swap(&password[i], &password[k]);
	}

    printf("\n Suggested 100%% strong password: ");
    for(int i = 0; i<10; i++)
    {
        printf("%c", password[i]);
    }
}
```

-   This function generates a strong, random 10-character password.
-   It creates character arrays `numbers`, `lower_case`, `upper_case`, `special_char1`, and `special_char2`.
-   It initializes an empty `password` array to store the generated password.
-   It iterates two times to fill the `password` array:
    -   It adds one random digit from `numbers`, one random lowercase letter from `lower_case`, one random uppercase letter from `upper_case`, one random character from `special_char1`, and one random character from `special_char2`
-   It then shuffles the `password` array using the `swap` function, to make the password more random.
-   Finally, it prints the suggested password to the console.

## 5. `main` Function

```c
int main()
{
    system("cls");                   // used to clear the screen each time the program is run
    char user_password[10];

    printf("\n This program will tell the strength of your password, and also suggests you a randomly generated 100%% strength password. ");

    //labelled as repeat
    repeat: printf("\n The password shoud not contain the following characters:");
    printf("\n '_', '/', '*', '%%', '&', '\', ';', '|', '~'.");
    printf("\n The password should contain exactly 10 characters.");   

    printf("\n Enter your password: ");
    scanf("%s", user_password);

    if(strlen(user_password)!=10)
    {
        printf("\n Password should be 10 characters long.\n\n");
        goto repeat;    //restart from the label 'repeat'
    }


    int strength;
    strength = calculate_strength(user_password);


    if(strength != -1) 
        printf("\n Strength of your password is: %d%%\n", strength);
    else 
    {
        printf("\n Invalid password.\n\n");
        goto repeat;    //restart from the label 'repeat'
    }


    if(strength == 100) 
        printf("\n Great Work!! Your password is strong enough.");
    else
    {
        srand((unsigned int)(time(NULL))); 
        generate_password();
    }  
	return 0; 
}
```

-   This is the main function where the program execution starts.
-   `system("cls")` clears the console screen.
-   It declares a character array `user_password` to store the user's input password.
-   It prints a welcome message to the console.
-   It prompts the user to enter a password.
-   The `repeat:` label is used to allow the program to ask the user for a password again if the previous input was not valid.
-   It uses `scanf` to read the password from the user.
-   It checks if the password is exactly 10 characters long. If not, it prints an error message and restarts the process from the label 'repeat' using `goto repeat`.
-   It calls `calculate_strength` to determine the password's strength.
-   If the returned strength value is not -1, it prints the strength percentage. Else it prints invalid password message and restarts the process from the label 'repeat' using `goto repeat`.
-   If the strength is 100, a success message is printed.
-   If the strength is less than 100, the program seeds the random number generator using current time. Then it calls `generate_password` to generate and suggest a new password to the user.
-   Finally, the function returns 0, indicating successful execution.

## Summary

In essence, this C program does the following:

1.  It asks the user for a password, ensuring it has 10 characters.
2.  It evaluates the user's password based on the types of characters used and assigns a strength score.
3.  If the user's password is not considered strong enough (less than 100%), it generates a random, strong password.

This program provides a basic example of password strength assessment and generation using C.
```
