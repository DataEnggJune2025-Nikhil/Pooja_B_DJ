USE devs_practice;
-- Q.1 List the names and dates of birth of all programmers.

SELECT programmer_name, DOB FROM programmers;

-- Q.2 Display the names of programmers whose primary language is 'Python'.
SELECT programmer_name FROM programmers
WHERE Primary_Language = 'Python';

-- Q.3 Show the names of programmers who joined the company after the year 2000.

SELECT programmer_name 
FROM programmers
WHERE DOJ > '2000-12-31';

-- Q.4 List the names and salaries of all female programmers.
SELECT programmer_name
FROM programmers
WHERE GENDER = 'F';

-- Q.5 Display the names of programmers sorted by their date of birth in ascending order.
SELECT Programmer_Name, DOB
FROM programmers
ORDER BY DOB ASC;

-- Q.6 Find the names of programmers whose secondary language is 'Java'.
SELECT programmer_name 
FROM programmers
WHERE secondary_language = 'Java';

-- Q.7 Show the details of programmers who earn a salary greater than $15,000.
SELECT programmer_name
FROM programmers 
WHERE Salary > '15,000';

-- Q.8 List the names of programmers whose primary language is 'C++' and who were born before 1970.

SELECT programmer_name
FROM programmers
WHERE Primary_Language = 'C++'
AND DOB < '1970-12-31';

-- Q.9 Display the software names developed in 'Java'.
SELECT Software_Name 
FROM software
WHERE Developed_In = 'Java';

-- Q.10 List the courses studied at 'MIT'.
SELECT Course
FROM studies
WHERE Institute = 'MIT';

-- Q.11 What is the average salary of all programmers?
SELECT AVG(Salary) as Average_salary
FROM programmers;

-- Q 12.How many programmers know 'Python' as their primary language?
SElECT COUNT(*) as Python_programmers
FROM programmers
WHERE Primary_Language = 'Python';

-- Q.13 What is the highest salary paid to a programmer?
SELECT MAX(Salary) as Highest_Salary
From programmers;

-- Q.14 What is the total development cost of all software?
SELECT SUM(DEvelopment_Cost) as Total_cost
FROM software;

-- Q.15 What is the minimum course fee paid by a programmer?
SELECT MIN(Course_Fee) as Min_course_fee
From studies;

-- Q.16 How many software packages were sold in total?
SELECT SUM(Sold) as Total_sold
FROM software;

-- Q.17 What is the average cost of a course at 'Columbia'?
SELECT AVG(Course_fee) as Average_cost_columbia
FROM studies
WHERE Institute = 'Columbia';

-- Q.18 How many male programmers are in the database?
SELECT COUNT(*) as Male_programmers
FROM programmers
WHERE GENDER = 'M';

-- Q.19 What is the sum of the software costs of packages developed in 'R'?
SELECT SUM(Software_Cost) as cost_of_software
FROM software
WHERE Developed_In = 'R';

-- Q.20 What is the maximum development cost for a package?
SELECT MAX(Development_Cost) as Max_Cost 
FROM software;

-- Q.21 Display the average salary for each primary language.
SELECT primary_language, AVG(Salary) as avgSalary
From programmers
GROUP BY primary_language;

-- Q.22 How many software packages were developed by each programmer?
SELECT Programmer_Name, COUNT(Software_Name) as Software_Packages
FROM software
GROUP BY Programmer_Name;

-- Q.23 Show the number of programmers for each gender.
SELECT GENDER, COUNT(*) as No_of_programmers
FROM programmers
GROUP BY GENDER
ORDER BY GENDER;

-- Q.24 List the institutes and the number of courses offered by each.
SELECT Institute, COUNT(*) as No_of_courses
FROM studies 
GROUP BY Institute
ORDER BY Institute;

-- Q.25 Find the primary languages where the average salary is greater than $15,000.
SELECT Primary_Language, AVG(Salary) as Average_Salary
FROM programmers
GROUP BY Primary_Language
HAVING AVG(Salary) > 15000 ;

-- Q.26 Display the total sales for each software developer.
SELECT Programmer_Name, SUM(Sold) as Total_Sales
FROM software
GROUP BY Programmer_Name
ORDER BY Programmer_Name;

-- Q.27 List the software languages and the number of software packages developed in each.
SELECT Developed_In, COUNT(Software_Name) as No_of_software_Packages
FROM software
GROUP BY Developed_In
ORDER BY Developed_In;

-- Q.28 Show the average course fee for each institute.
SELECT Institute, AVG(Course_Fee) as avg_course_fee
FROM studies
GROUP BY Institute
ORDER BY Institute;

-- Q.29 Find the programmers who have developed more than one software package.
SELECT Programmer_Name, COUNT(Software_Name) as No_of_Software_Packages
FROM software
GROUP BY Programmer_Name
HAVING COUNT(Software_Name) > 1;

-- Q.30 Display the number of courses for each institute, but only for institutes with more than two courses.
SELECT Institute, COUNT(Course) as No_of_courses
FROM studies 
GROUP BY Institute
HAVING COUNT(Course) > 2;

-- Q.31 Display the names of programmers and the software they developed.
SELECT programmers.Programmer_Name, software.Software_Name
FROM programmers
INNER JOIN software ON programmers.Programmer_Name = software.Programmer_Name;

-- Q.32 List the programmers and the institutes where they studied.

SELECT programmers.Programmer_Name, studies.Institute
FROM programmers
INNER JOIN studies ON programmers.Programmer_Name = studies.Programmer_Name;

-- Q.33 Show the names of programmers and their course fees.
SELECT programmers.Programmer_Name, studies.Course_Fee
FROM programmers
RIGHT JOIN  studies ON programmers.Programmer_Name = studies.Programmer_Name;

-- Q.34 Find the software names and the institutes where the developers studied.
SELECT software.Software_Name, studies.Institute 
FROM software
RIGHT JOIN studies 


 