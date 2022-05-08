
# INTRODUCTION
In this project we did a attendance automation system which is nothing but the maintenance of the employee’s attendance details. our main goal is to generates the attendance of the employee on basis of data which is in our input excel file. It is maintained on the daily basis of their attendance . The input of the program is the information of person like Mail ID, PS Number, Student Name. 
- The people who are eligible to access course then there ps number should be match with course Id by the  attendance is calculated.


# Research:-
https://www.youtube.com/watch?v=vmEHCJofslg
https://www.youtube.com/watch?v=C2O3O_GydV4
https://www.youtube.com/watch?v=7YS6YDQKFh0
https://www.youtube.com/watch?v=nsKNPHJ9iPc
This is a simple project which simply provide easy contents on python programming to the user after taking input from the user.


# ADVANTAGES

- Improve time and attendance accuracy
- Track employee leaves
- Maintain fully-staffed work shifts
- Improve employee morale
- Access employee time-off trends

# RESEARCH

This is a simple project which simply provide easy contents on python programming to the user after taking input from the user.

# FEATURES

 - Accurately track clock-in and out.  
 - Flexible customer scheduling.  
 - Absence management.  
 - Elimination of miss punch.  
 - Automate the whole process with full security
 
 # SWOT analysis

## Strengths:

  An automated time and attendance system accurately captures all employee time off requests and call-ins, creating a reliable digital 
  
  paper trail of employee/student absences year after year.
    
  Access employee time-off trends.

## Weaknesses:

  When you rely on punched cards or time sheets, there is always a risk of human error.
  
  The use of obsolete systems carries the risk of system crashes, security issues and loss of valuable information.
 
## Opportunities:

   Attendance Management Systems allow you to calculate the hours for which employees/students work accurately. This is especially beneficial 
   
   if you have employees working on an hourly basis. You need to be able to calculate the exact wages you owe to your employees/students.
   
   And, you need to know if you owe overtime wages to any employees/students.

## Threats:

   When you suffer data loss due to various incidents such as mechanical damage, power failure, software crash, disasters or loss of your 
   
   laptops and mobile devices, it is another way of inadvertent data exposure.


# 4W's and 1H's

## Who

   Attendance Automation system is crucial for any organization.

## What

   It is the system you use to document the time your employees work and the time they take off
  
## When

   Attendance Automation system keeps track of your employee hours.


## Where

  Attendance Management can be done by recording employee hours on paper, using spreadsheets.


## How

  It can be used in a mobile app easily or can login in a PC. 


 # Test plan

## High Level Requirements:

| ID | Description |Expected O/P |Expected I/P|Actual Output|Type of Test|
|:---:|:---:|:---:|:---:|:---:|:---:|
|HLR_01| System shall be able to read the excel sheet.|System  will read the file and get the required data entered in the code|Datas should be entered in the spreadsheet|System prints the output|Requirement Based|
|HLR_02| The system shall able to store the output |The output is of the form of spreadsheet|Enter the file name|The final output content will display|Requirement Based|
|HLR_03|The system shall able to identify whether the student(s) is present for the day.|The system should able to read the data|The user should mark the attendence for the particular day |The systems reads the data given by  the user in the spreadsheet|Scenario Based||


##  Low level Requirements:

| ID | Description |Expected O/P |Expected I/P|Actual Output|Type of Test|
|:---:|:---:|:---:|:---:|:---:|:---:|
|LLR_01| System shall be able to read the total number of students/days given in the spreadsheet|The system should able to count the number of students/days|User will enter the data in the spreadsheet|The system reads the data |Requirement Based|
|LLR_02| User shall be able to view the output |The outout is stored in the spreadsheet once the program is executed|The system reads the spreadsheet |The system creates new entries int the excel sheet as programmed by the programmer|Requirement Based|
|LLR_03|The system should able to mark TRUE if the student is Present |the system should return TRUE|The data given in the spreadsheet is of "P(2/2)" which states that student is present  |The system returns TRUE|Scenario Based|
|LLR_04|The system should able to mark FALSE if the student is Present |the system should return FALSE|The data given in the spreadsheet is of "?" which states that student is absent  |The system returns FALSE|Scenario Based|
