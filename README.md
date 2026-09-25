# PASSWORD-STRENGTH-CHECK-AND-GENERATOR

•Project Overview

The Password Strength Check and Generator is a Python-based command-line tool that helps users create and evaluate secure passwords. Weak passwords remain one of the most common causes of account compromise, yet many users are unaware of what makes a password strong. This project addresses that problem by giving users two simple options: check the strength of an existing password, or generate a new, random strong password.

The program check password strength based on two criteria — length, and character variety (uppercase letters, numbers, and special characters) — and reports back whether the password is strong or weak. For users who'd rather not think up a password themselves, the generator creates a strong, randomized password that satisfies all these criteria automatically.

This project was built to apply core programming and problem-solving concepts — including conditional logic, loops, functions, and string manipulation — to a small, real-world cybersecurity problem.

•Features
  The main features of this project are:
    
    1.Password Length Check
    
    2.Password Character Variety Check
    
    3.Strength Report
    
    4.Random password generator

•Technologies used

  1.Python 3
  
  2.Spyder (Anaconda)
  
  3.Git and Github

•Steps to Run project

  1.Install Python
  
  2.Clone the Github repository
  
  3.Open the project folder in your preferred Python IDE
  
  4.Open MAIN PROGRAM.py
  
  5.Run file
  
  6.Follow the program on-screen prompts

•Instructions for testing

  To test the Strength Checker (Option 1):

    Run the program and select option 1
    Try the following test cases and confirm the output matches expectations:
      abc -	Fails too short, low variety
      abcdefgh - Fails length check passes, but fails complexity 
      Password1-	Passes length,fails if missing a symbol
      Password1!- Passes — meets length and full character variety
      (empty input)-	Should not crash the program
