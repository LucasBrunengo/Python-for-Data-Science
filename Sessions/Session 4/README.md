# Python Class 3

## Table of contents

---

## Table of Contents

**[Session 4](#session-4)**
- **[Exercise 1: Counting Files in a Directory](#exercise-1-counting-files-in-a-directory)**
- **[Exercise 2: Validating File Names Against a Pattern](#exercise-2-validating-file-names-against-a-pattern)**
- **[Exercise 3: Counting Annotations per Month](#exercise-3-counting-annotations-per-month)**
- **[Exercise 4: Organizing Files into Monthly Folders](#exercise-4-organizing-files-into-monthly-folders)**
- **[Exercise 5: Sorting Annotations](#exercise-5-sorting-annotations)**
- **[Exercise 6: Identifying the Most Recent Annotation Satellite](#exercise-6-identifying-the-most-recent-annotation-satellite)**
- **[Exercise 7: Counting Unique Regions](#exercise-7-counting-unique-regions)**

---

# **Session 4** 

In Session 4, I explored object-oriented programming concepts in Python. This session focused on defining classes, managing attributes, and implementing methods. The exercises revolved around creating a simple course registration system that allows students to enroll in courses and manage their registrations.

## **List of exercises:** 

### **Exercise 1: Counting files in a directory**

      - How many files the annotations folder has.

* Description: This exercise counts the total number of files in a specified annotations directory and prints the count.

* Input:

![Course_gpa_Output](../../Screenshots/Session%204/Inputs/Session4_Ex1_Inp.png)

* Output:

![Course_gpa_Output](../../Screenshots/Session%204/Outputs/Session4_Ex1_Out.png)

---

### **Exercise 2: Validating File Names Against a Pattern**
      - {DATE}_{TIME}_SN{SATELLITE_NUMBER}_QUICKVIEW_VISUAL_{VERSION}_{UNIQUE_REGION}.txt

         where:

            - DATE expressed as YYYYMMDD (year, month and day), e.g. 20241201, 20230321 ...
            - TIME expressed as HHMMSS (hour, minutes and seconds), e.g. 2134307
            - SATELLITE_NUMBER an integer that represents the satellite number.
            - VERSION provides the version of the pipeline, e.g. "0_1_2", "1_3_1" ...
            - UNIQUE_REGION provides a unique location in the form of a string, e.g SATL-2KM-10N_552_4164
            
      - How many of them follow the name convention expressed above. 

* Description: This exercise filters files based on a specific naming convention, counts valid and invalid files, and prints the results.

* Input:

![Course_gpa_Output](../../Screenshots/Session%204/Inputs/Session4_Ex2_Inp.png)

* Output:

![Course_gpa_Output](../../Screenshots/Session%204/Outputs/Session4_Ex2_Out.png)

---

### **Exercise 3: Counting Annotations per Month**

      - How many of annotations you have per month and year. Which month has more annotation files.

* Description: This exercise counts the number of annotations per month from valid files, tracks satellite counts, and finds the month with the most annotations.

* Input:

![Course_gpa_Output](../../Screenshots/Session%204/Inputs/Session4_Ex3_Inp.png)

![Course_gpa_Output](../../Screenshots/Session%204/Inputs/Session4_Ex3_Inp1.png)
* Output:

![Course_gpa_Output](../../Screenshots/Session%204/Outputs/Session4_Ex3_Out.png)

---

### **Exercise 4: Organizing Files into Monthly Folders**

      - Create a new annotations folder with multiple folders corresponding to a month.

* Description: This exercise organizes valid annotation files into subfolders based on their respective months.

* Input:

![Course_gpa_Output](../../Screenshots/Session%204/Inputs/Session4_Ex4_Inp.png)

* Output:

![Course_gpa_Output](../../Screenshots/Session%204/Outputs/Session4_Ex4_Out.png)

![Course_gpa_Output](../../Screenshots/Session%204/Outputs/Session4_Ex4_Out1.png)

---

### **Exercise 5: Sorting Annotations**

      - Print all the annotations from the most recent to the oldest one. 

* Description: This exercise sorts valid annotation files by date and time in descending order and prints them.

* Input:

![Course_gpa_Output](../../Screenshots/Session%204/Inputs/Session4_Ex5_Inp.png)

* Output:

![Course_gpa_Output](../../Screenshots/Session%204/Outputs/Session4_Ex5_Out.png)

---

### **Exercise 6: Identifying the Most Recent Annotation Satellite**

      - How many different satellites there are, how many annotations we have per satellite number, and which one was used in the most recent annotation file. 

* Description: This exercise identifies the satellite of the most recent annotation and prints the result.

* Input:

![Course_gpa_Output](../../Screenshots/Session%204/Inputs/Session4_Ex6_Inp.png)

* Output:

![Course_gpa_Output](../../Screenshots/Session%204/Outputs/Session4_Ex6_Out.png)

---

### **Exercise 7: Counting Unique Regions**

      - How many unique regions there are.

* Description: This exercise counts the number of unique regions identified from the valid annotation files.

* Input:

![Course_gpa_Output](../../Screenshots/Session%204/Inputs/Session4_Ex7_Inp.png)

* Output:

![Course_gpa_Output](../../Screenshots/Session%204/Outputs/Session4_Ex7_Out.png)
