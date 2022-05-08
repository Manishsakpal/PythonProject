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

# Simulation Project
https://user-images.githubusercontent.com/86291115/147573183-f3e41439-04ab-4003-bf62-01ca6962267d.mp4
