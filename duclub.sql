CREATE TABLE Accounts (
    MemberID int primary key AUTO_INCREMENT,
    MemberName varchar(255),
    MemberContactNo varchar(20),
    MemberPresentAdress varchar(2555),
    MemberPermanentAdress varchar(2555),
    designation varchar(100),
    department varchar(100),
    status varchar(40),
     email varchar(100),
     password varchar(2555),
     type varchar(255) 
);


CREATE TABLE Lounge (
      LoungeID int key NOT NULL AUTO_INCREMENT,
      LoungeName varchar(255)
);

CREATE TABLE FoodItem (
      FoodID int primary key NOT NULL AUTO_INCREMENT,
      FoodName varchar(2555),
      FoodPrice int,
      weekBitmask int,
      timeBitmask int
);

INSERT INTO FoodItem (FoodName, FoodPrice, weekBitMask, timeBitmask) VALUES
( 'Chitoipitha', 10, 91001001, 91010),
('Rumaliruti', 15, 91111111, 91010),
('Beef', 70, 91111111, 90101),
('Daal', 60, 91000100, 91101),
('Vegetable', 30, 91000100, 91101),
('Daalpuri', 5, 91111111, 91010),
('Alupuri', 5, 91111111, 91010),
('Sandwich', 40, 91111111, 91010),
('Bombay Toast', 10, 91111111, 91010),
('Soup', 60, 90101011, 91010),
('Lachchi', 40, 90100100, 91111),
('Vapapitha', 5, 90100000, 91010),
('Chicken fry', 50, 90100000, 91111),
('Alu chop', 5, 90001110, 91010),
('Cholapiaju', 40, 90010000, 91010),
('Chicken grill', 120, 90010010, 90101),
('Moghlaiparatha', 50, 90001001, 91010),
('Shingara', 5, 90001001, 91010),
('Shkkabab', 60, 90001001, 90101),
('Luchi', 5, 90001001, 91010),
('Sola Batura', 20, 90000100, 91010),
('Somucha', 10, 90000100, 91010),
('Paratha', 5, 90000010, 91010),
('Chicken', 100, 91111111, 91111),
('Tea', 20, 90000000, 91111),
('coffee', 20, 91111111, 91111);

CREATE TABLE GameTable (
      GameID int primary key NOT NULL AUTO_INCREMENT,
      GameName varchar(2555),
      GameFee int
);

CREATE TABLE Admin(
      MemberID int,
      AdminID int primary key NOT NULL AUTO_INCREMENT,
      adminPassword varchar(2555),
CONSTRAINT FK_MemberID FOREIGN KEY (MemberID) REFERENCES Accounts(MemberID)
);

CREATE TABLE LoungeBooking(
      LoungeID int,
      bookingID int primary key NOT NULL AUTO_INCREMENT,
      startTime datetime,
      endTime datetime,
CONSTRAINT FK_LoungeID FOREIGN KEY (LoungeID) REFERENCES Lounge(LoungeID)
);


CREATE TABLE GameBooking(
      LoungeID int,
      GameID int,
      GLID int primary key NOT NULL AUTO_INCREMENT,
      GameStartTime datetime,
      GameEndTime datetime,
CONSTRAINT FK_GameLoungeID FOREIGN KEY (LoungeID) REFERENCES Lounge(LoungeID),

CONSTRAINT GameLID FOREIGN KEY (GameID) REFERENCES GameTable(GameID)
);

CREATE TABLE BillTable(
      LoungeID int,
      FoodID int,
      BillID int primary key NOT NULL AUTO_INCREMENT,
      MemberID int,
      Quantity int,
      Discount double(10,2),
      Date date,
     Total double(10,2),
CONSTRAINT FK_BillLoungeID FOREIGN KEY (LoungeID) REFERENCES Lounge(LoungeID),

CONSTRAINT FK_BilMemberID FOREIGN KEY (MemberID) REFERENCES Accounts(MemberID),

CONSTRAINT FK_BillFoodID FOREIGN KEY (FoodID) REFERENCES FoodItem(FoodID)

);




delimiter //
CREATE PROCEDURE addM (IN param1 VARCHAR(255))
BEGIN
INSERT INTO Accounts(MemberName) VALUES (param1);
END //

delimiter ;


delimiter //
CREATE PROCEDURE addMember (IN name VARCHAR(255), IN cell_no VARCHAR(20), IN presentad VARCHAR(2555), IN permanentad VARCHAR(2555), IN designation VARCHAR(100), IN dept VARCHAR(100), IN status VARCHAR(40), mail VARCHAR(100), type VARCHAR(255))
BEGIN
INSERT INTO Accounts(MemberName, MemberContactNo, MemberPresentAdress, MemberPermanentAdress, designation, department, status, email, type) VALUES (name, cell_no, presentad, permanentad, designation, dept, status, mail, type);
END //

delimiter ;

