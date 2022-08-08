#!/usr/bin/env python
# coding: utf-8

# In[9]:


import sqlite3


# In[3]:


import sqlite3
sq = sqlite3.connect('tcs-final-assignment.db')
curs = sq.cursor()


# In[12]:


import sqlite3 as sq
import pandas as pd

connection = sq.connect('tcs-final-assignment.db')
curs = connection.cursor()
 
curs.execute('''CREATE TABLE IF NOT EXISTS users  (
	"UserID"	INTEGER NOT NULL UNIQUE,
	"EmployerNumber"	INTEGER NOT NULL,
	"CreationDate(user)"	NUMERIC NOT NULL,
	"Username"	TEXT NOT NULL UNIQUE,
	"Password"	TEXT NOT NULL UNIQUE,
	"Level"	TEXT NOT NULL
) ;''' ) 
users = pd.read_csv('user.csv')
users.to_sql('users', connection, if_exists='replace', index=False)


# In[11]:


import sqlite3 as sq
import pandas as pd

connection = sq.connect('tcs-final-assignment.db')
 
curs = connection.cursor()
curs.execute('''CREATE TABLE IF NOT EXISTS "Certification" (
	"Certification_ID"	INTEGER NOT NULL UNIQUE,
	"User ID"	INTEGER NOT NULL UNIQUE,
	"Course ID"	INTEGER NOT NULL UNIQUE,
	"Completion Duration(minutes)"	INTEGER NOT NULL,
	"Completion Date"	NUMERIC NOT NULL
);''' )
 
Certification = pd.read_csv('certification.csv')
Certification.to_sql('Certification', connection, if_exists='replace', index=False)


# In[13]:


import sqlite3 as sq
import pandas as pd

connection = sq.connect('tcs-final-assignment.db')
curs = connection.cursor()
 
curs.execute('''CREATE TABLE IF NOT EXISTS "OngoingTraining" (
	"Training ID"	INTEGER NOT NULL UNIQUE,
	"User ID"	INTEGER NOT NULL UNIQUE,
	"Course ID"	INTEGER NOT NULL UNIQUE,
	"Status"	TEXT NOT NULL,
	"Completion Percentage"	INTEGER NOT NULL,
	"Start Date"	NUMERIC NOT NULL,
	"Finish Date"	NUMERIC NOT NULL,
	"Last Updated"	NUMERIC NOT NULL
);''' )
 
OngoingTraining = pd.read_csv('ongoingtraining.csv')
OngoingTraining.to_sql('OngoingTraining', connection, if_exists='replace', index=False)


# In[14]:


import sqlite3 as sq
import pandas as pd

connection = sq.connect('tcs-final-assignment.db')
curs = connection.cursor()
 
curs.execute('''CREATE TABLE IF NOT EXISTS "Pictures" (
	"Course ID"	INTEGER NOT NULL UNIQUE,
	"Platform ID"	INTEGER NOT NULL UNIQUE,
	"Image Object"	BLOB NOT NULL,
	"Photo ID"	INTEGER NOT NULL
);''' )
 
Pictures = pd.read_csv('pictures.csv')
Pictures.to_sql('Pictures', connection, if_exists='replace', index=False)


# In[15]:


import sqlite3 as sq
import pandas as pd

connection = sq.connect('tcs-final-assignment.db')
curs = connection.cursor()
 
curs.execute('''CREATE TABLE IF NOT EXISTS "Platform" (
	"Platform ID"	INTEGER NOT NULL UNIQUE,
	"Courses"	TEXT NOT NULL,
	"Platform Name"	TEXT NOT NULL,
	"Hyperlink Path"	TEXT NOT NULL UNIQUE
);''' )
 
Platform = pd.read_csv('platform.csv')
Platform.to_sql('Platform', connection, if_exists='replace', index=False)


# In[16]:


import sqlite3 as sq
import pandas as pd

connection = sq.connect('tcs-final-assignment.db')
curs = connection.cursor()

curs.execute('''CREATE TABLE IF NOT EXISTS "Review" (
	"User ID"	INTEGER NOT NULL UNIQUE,
	"Course ID"	INTEGER NOT NULL UNIQUE,
	"Like/Dislike"	TEXT NOT NULL,
	"Feedback"	TEXT NOT NULL,
	"Ranking Score out of 5"	NUMERIC NOT NULL
);''' )
 
Review = pd.read_csv('review.csv')
Review.to_sql('Review', connection, if_exists='replace', index=False)


# In[17]:


import sqlite3 as sq
import pandas as pd

connection = sq.connect('tcs-final-assignment.db')
curs = connection.cursor()

curs.execute('''CREATE TABLE IF NOT EXISTS "Course" (
	"Course ID"	INTEGER NOT NULL UNIQUE,
	"Course Name"	TEXT NOT NULL,
	"Platform ID"	INTEGER NOT NULL UNIQUE,
	"Duration(in minutes)"	INTEGER NOT NULL,
	"Creation Date(course)"	NUMERIC NOT NULL,
	"Tags"	TEXT NOT NULL,
	"Photo"	BLOB NOT NULL
);''' )
 
Course = pd.read_csv('course.csv')
Course.to_sql('Course', connection, if_exists='replace', index=False)


# In[9]:


#SELECT FUNCTION
for row in curs.execute('SELECT * FROM user WHERE "Employer Number" = 8186958215'):
        print(row)


# In[6]:


#INSERT FUNCTION
import sqlite3

conn = sqlite3.connect('tcs-final-assignment.db')
print ("Opened database successfully");

conn.execute("INSERT INTO users ('Employer Number','Creation Date(user)',Username,Password,Level)       VALUES  (81869582152,'11-11-2020','mfishwick11','x7MSSUgdnc55','Jr')")
conn.commit()
print ("Records created successfully");


# In[11]:


#DELETE FUNCTION
curs.execute('''
               DELETE FROM users WHERE "Employer Number" = 81869582152
                ''')


# In[5]:


#UPDATE FUNCTION

curs.execute('''UPDATE users SET Level = "3" WHERE "User ID" = 1;''')
print('\nAfter Updating...\n') 


# In[ ]:




