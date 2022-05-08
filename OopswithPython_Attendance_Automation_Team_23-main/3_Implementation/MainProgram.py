from numpy import newaxis
import pandas as pd
df=pd.read_excel(r"Attendance_Automation.xlsx")
dfattendence=pd.read_excel(r"Attendance_Automation.xlsx",sheet_name="attendance")
dfclass=pd.read_excel(r"Attendance_Automation.xlsx",sheet_name="class")
dfemail=pd.read_excel(r"Attendance_Automation.xlsx",sheet_name="email")
course_name=dfattendence.columns[1]
c=0
at_location=0
PS_number=[]
for i in  dfclass['Title'].values:
    if (course_name==i):
        at_location=c
    c+=1
Cus_class_id=(dfclass['Class id'][at_location])
for ii in dfattendence['Unnamed: 3'].values:
    x=0
    for iii in dfemail['email'].values:
        if iii==ii:
            PS_number.append(dfemail['ps no'][x])
        x+=1
count=0
class_list=[]
Cut_segment_id_list=[]
ps_no_list=[]
Cust_attendence=[]
for u in range(3,(len(dfattendence['Unnamed: 3'].values))):
    for uu in range(4,4+len(dfattendence.columns)-11):
        if (dfattendence.values[u][uu])=='P (2/2)':
            class_list.append(Cus_class_id)
            Cut_segment_id_list.append(uu-3)
            ps_no_list.append(PS_number[count])
            Cust_attendence.append('True')
        else:
            class_list.append(Cus_class_id)
            Cut_segment_id_list.append(uu-3)
            ps_no_list.append(PS_number[count])
            Cust_attendence.append('False')
    count+=1

NewSheet=pd.DataFrame({'Cust_class_list':class_list,'cust_Segment_Id':Cut_segment_id_list,'cust_User_Id':ps_no_list,'cust_Attendance':Cust_attendence})
NewSheet.to_csv("AttendenceOut.csv",index=False)

