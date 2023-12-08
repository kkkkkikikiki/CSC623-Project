import sqlite3
import pandas as pd

db_connect = sqlite3.connect('SuperMaids.db')

cursor = db_connect.cursor()
#if something wrong drop table
#query = """ DROP TABLE Employee;
#    """
#cursor.execute(query)
#query = """ DROP TABLE Requirement;
#    """
#cursor.execute(query)
#query = """ DROP TABLE Client;
#    """
#cursor.execute(query)
#query = """ DROP TABLE Equipment;
#    """
#cursor.execute(query)
#query = """ DROP TABLE Performs;
#    """
#cursor.execute(query)
#query = """ DROP TABLE Need;
#    """
#cursor.execute(query)


query = """
CREATE TABLE Employee
 (
  staffNo INT,
  fName VARCHAR(100) ,
  lName VARCHAR(100),
  salary INT, 
  address VARCHAR(100),
  telNo INT,
  PRIMARY KEY(staffNo)
);
"""
cursor.execute(query)

query = """
     INSERT INTO Employee
     VALUES 
     (101, 'John', 'Smith', 18, '123 down street', 7279877890),
     (102, ' Kevin', 'Hart', 18, '14 up street', 3235659870),
     (103, 'Eddie', 'Murphy', 18, '12 front blvd', 4342348765),
     (104, 'Kyrie', 'Irving', 18, '19 west way', 8765674567),
     (105, 'Damian', ' Lillard', 18, '24 heat way', 7673456756)    
    """
cursor.execute(query)

query = """
CREATE TABLE Requirement
 (
  requirementID INT,
  startDate DATE NOT NULL CHECK (startDate > CURRENT_DATE),
  startTime INT,
  duration INT,
  comments VARCHAR(100),
  clientNo INT,
  PRIMARY KEY(requirementID),
  FOREIGN KEY (clientNo) REFERENCES Client(clientNo) ON DELETE SET NULL
);  """ 
cursor.execute(query)
query = """
INSERT INTO Requirement
VALUES 
(001, '2024-01-01', '09:00', 6, 'No chemicals for cleaning', 012),
(002, '2024-01-02', '09:00', 4, 'Floors need industrial clean', 010),
(003, '2024-03-03', '10:00', 3, 'disinfect with antibiotic sprayer', 011),
(004, '2024-04-04', '07:00', 8, 'Walls need industrial clean', 014),
(005, '2024-05-05', '17:00', 4, 'Ceilings need industrial clean', 015)
"""

cursor.execute(query)

query = """
CREATE TABLE Client
 (
  clientNo INT,
  clientName VARCHAR(100),
  telNo INT,
  address VARCHAR(200),
  PRIMARY KEY(clientNo)
 );
    """
cursor.execute(query)
query = """
INSERT INTO Client
VALUES 
(010, 'The Cardboard Box Company', 4342344565, '602 Buttonwood Drive Braintree, MA 02184'),
(011, 'P.Nuttall', 5678909090, '64 Devon Ave. Atwater, CA 95301'),
(012, 'Rathskeller', 8786542222, '9106 Cardinal Street Culpeper, VA 22701'),
(013, 'Aviation Center', 7776665555, '50 Beaver Ridge St. Largo, FL 33771'),
(014, 'Oceans Eleven', 45433335566, '8185 High Noon Street Westbury, NY 11590'),
(015, 'Staples Center', 9899008700, '75 Railroad Road Butte, MT 59701')
"""
cursor.execute(query)

query = """
CREATE TABLE Equipment
 (
  equipmentID INT,
  description VARCHAR(200),
  usage INT,
  cost INT,
  PRIMARY KEY(equipmentID)
);
     """  
cursor.execute(query)
query = """
INSERT INTO Equipment
VALUES 
(201, 'Steam Power Wash', 2/5, 200),
(202, 'Industrial floor cleaner', 2/5, 500),
(203, 'antibiotic sprayer', 4/5, 100),
(204, 'Industrial wall cleaner', 2/5, 400),
(205, 'Industrial Ceiling cleaner', 1/5, 600)
"""
cursor.execute(query)

query = """
CREATE TABLE Perform
(
requirementID INT,
staffNo INT,
worktime INT,
PRIMARY KEY(requirementID, staffNo),
FOREIGN KEY (requirementID) REFERENCES Requirement(requirementID) ON DELETE SET NULL,
FOREIGN KEY (staffNo) REFERENCES Employee(staffNo) ON DELETE SET NULL
);
     """  
cursor.execute(query)
query = """
INSERT INTO Perform
VALUES 
(001, 101, 6),
(002, 102, 4),
(003, 103, 3),
(004, 104, 8),
(005, 105, 4)
"""

cursor.execute(query)

query = """
CREATE TABLE Need
(
requirementID INT,
equipmentID INT,
dateOfUse DATE,
PRIMARY KEY(requirementID, equipmentID),
FOREIGN KEY (requirementID) REFERENCES Service(requirementID) ON DELETE SET NULL,
FOREIGN KEY (equipmentID) REFERENCES Equipment(equipmentID) ON DELETE SET NULL
);
     """  
cursor.execute(query)
query = """
INSERT INTO Need
VALUES 
(001, 201, '2024-01-01'),
(002, 202, '2024-01-02'),
(003, 203, '2024-03-03'),
(004, 204, '2024-04-04'),
(005, 205, '2024-05-05')
"""

cursor.execute(query)

db_connect.commit()
db_connect.close()