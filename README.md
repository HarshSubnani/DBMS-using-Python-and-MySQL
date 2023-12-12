This is a database management system designed for handling patient records, staff information, and appointments. The system provides a user-friendly interface for managing hospital data, offering features such as adding new patients, updating records, and scheduling appointments. This project was developed as part of my senior design project in high school. The code is designed to handle hospital records but can be adapted for other use cases with some modifications. Please note that the code might not be perfect and may have some issues. Let me know if you find errors or have suggestions for improvements.


Before running this code, please execute the following MySQL queries:
 
1) create table Patient_info (p_id int PRIMARY KEY, p_fname VARCHAR(20), p_lname VARCHAR(20),mobile_no VARCHAR(13), email_id varchar(30), disease varchar(30), d_ad date, d_dis date, dept varchar(15));

2) create table hos_staff(emp_id int PRIMARY KEY, emp_fname VARCHAR(20), emp_lname VARCHAR(20),mobile_no VARCHAR(13),prof varchar(30), speciality varchar(40));

3) create table appoint_sch (app_no int PRIMARY KEY, p_name VARCHAR(30), treatment varchar(50));


