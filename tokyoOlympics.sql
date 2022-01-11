DROP DATABASE IF EXISTS TokyoOlympics;
CREATE DATABASE TokyoOlympics;
USE TokyoOlympics;

-- CREATE TABLEs
    
CREATE TABLE Sport (
    SportName CHAR(50),
    IsTeamSport BOOL NOT NULL, 
    PRIMARY KEY (SportName)
    );
    
CREATE TABLE Event (
	EventName CHAR(50),
    PRIMARY KEY (EventName)
    );
    
CREATE TABLE Team (
	TeamID INT AUTO_INCREMENT,
    SportName CHAR(50),
    Country CHAR(50) NOT NULL,
    MedalWon CHAR(1) NOT NULL,
    Gender CHAR(1) NOT NULL,
    PRIMARY KEY (TeamID, SportName),
    FOREIGN KEY (SportName) REFERENCES Sport(SportName)
    ON DELETE CASCADE ON UPDATE CASCADE
    -- FOREIGN KEY (Country) REFERENCES Athlete(Country)
    -- ON DELETE CASCADE ON UPDATE CASCADE
    );
    
CREATE TABLE Coach (
	CoachID INT AUTO_INCREMENT,
    CoachFirstName CHAR(50),
    CoachLastName CHAR(50),
    SportName CHAR(50),
    Country CHAR(50),
    GenderCoached CHAR(1),
    Password CHAR(40),
    PRIMARY KEY (CoachID, SportName),
    FOREIGN KEY (SportName) REFERENCES Sport(SportName)
    ON DELETE CASCADE ON UPDATE CASCADE
    -- FOREIGN KEY (Country) REFERENCES Athlete(Country)
    -- ON DELETE CASCADE ON UPDATE CASCADE
	);
    
CREATE TABLE Player (
	AthleteID INT AUTO_INCREMENT,
    TeamID INT,
    AthleteFirstName CHAR(50),
    AthleteLastName CHAR(50),
    Country CHAR(50),
    Gender CHAR(1),
	PRIMARY KEY (AthleteID, TeamID),
    -- FOREIGN KEY (AthleteID) REFERENCES Athlete(AthleteID)
    -- ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (TeamID) REFERENCES Team(TeamID)
    ON DELETE CASCADE ON UPDATE CASCADE
    );
    
CREATE TABLE Competitor (
	AthleteID INT AUTO_INCREMENT,
    SportName CHAR(50),
    AthleteFirstName CHAR(50),
    AthleteLastName CHAR(50),
    Country CHAR(50),
    Gender CHAR(1),
    PRIMARY KEY (AthleteID, SportName),
    FOREIGN KEY (SportName) REFERENCES Sport (SportName)
    ON DELETE CASCADE ON UPDATE CASCADE
    );
    
CREATE TABLE EventCompetition (
	Time TIME NOT NULL,
    MedalWon CHAR(1) NOT NULL,
    EventName CHAR(50),
    AthleteID INT,
    PRIMARY KEY (EventName, AthleteID),
    FOREIGN KEY (EventName) REFERENCES Event(EventName)
    ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (AthleteID) REFERENCES Competitor (AthleteID)
    ON DELETE CASCADE ON UPDATE CASCADE
    );



-- CREATE USERS
DROP USER IF EXISTS OlympicAthlete;
DROP USER IF EXISTS OlympicCoach;
DROP USER IF EXISTS OlympicOfficial;
DROP USER IF EXISTS OlympicSpectator;
CREATE USER OlympicAthlete;
CREATE USER OlympicCoach;
CREATE USER OlympicOfficial;
CREATE USER OlympicSpectator;

-- Insert Tests

INSERT INTO Sport (SportName, IsTeamSport) VALUES 
("volleyball", "1"),
("soccer", "1"),
("waterpolo", "1"),
("swim","0");

INSERT INTO Team (SportName, Country, MedalWon, Gender) VALUES 
("volleyball", "France", "G", "M"),
("volleyball", "ROC", "S", "M"),
("volleyball","Argentina","B", "M"),
("volleyball","United States", "G", "F"),
("volleyball","Brazil", "S", "F"),
("volleyball","Serbia", "B", "F"),
("soccer","Brazil", "G", "M"),
("soccer","Spain", "S", "M"),
("soccer","Mexico", "B", "M"),
("soccer","Canada", "G", "F"),
("soccer","Sweden", "S", "F"),
("soccer","United States", "B", "F"),
("waterpolo", "Serbia", "G", "M"), 
("waterpolo", "Greece", "S", "M"), 
("waterpolo", "Hungary", "B", "M"), 
("waterpolo", "United States", "G", "F"), 
("waterpolo", "Spain", "S", "F"), 
("waterpolo", "Hungary", "B", "F"); 

INSERT INTO Coach (SportName, Country, CoachFirstName, CoachLastName, GenderCoached, Password) VALUES 
("waterpolo", "Serbia", "Dejan", "Savić", "M", "serbia"),
("waterpolo", "Greece", "Thodoris", "Vlachos","M", "greece"),
("waterpolo", "Hungary", "Tamás", "Märcz","M", "hungary"),
("waterpolo", "United States", "Adam", "Krikorian","F","unitedstates"),
("waterpolo", "Spain", "Miki", "Oca","F","spain"),
("waterpolo", "Hungary", "Attila", "Bíró","F","hungary"),
("soccer", "Brazil", "André", "Jardine","M","brazil"),
("soccer", "Spain", "Luis", "de la Fuente","M","spain"),
("soccer", "Mexico", "Jaime", "Lozano","M","mexico"),
("soccer", "Canada", "Bev", "Priestman","F","canada"),
("soccer", "Sweden", "Peter", "Gerhardsson","F","sweden"),
("soccer", "United States", "Vlatko", "Andonovski","F","unitedstates"),
("volleyball", "France", "Laurent", "Tillie","M","france"),
("volleyball", "ROC", "Tuomas", "Sammelvuo","M","roc"),
("volleyball", "Argentina", "Marcelo", "Méndez","M","argentina"),
("volleyball", "United States", "Karch", "Kiraly","F","unitedstates"),
("volleyball", "Brazil", "José", "Roberto Guimarães","F","brazil"),
("volleyball", "Serbia", "Zoran", "Terzić","F","serbia");

INSERT INTO Event (EventName) VALUES
("50 m freestyle"),
("100 m freestyle"),
("200 m freestyle"),
("400 m freestyle"),
("800 m freestyle"),
("1500 m freestyle"),
("100 m backstroke"),
("200 m backstroke"),
("100 m breaststroke"),
("200 m breaststroke"),
("100 m butterfly"),
("200 m butterfly"),
("200 m individual medley"),
("400 m individual medley");


/*
GRANT EXECUTE ON PROCEDURE EnterPersonalInformation TO OlympicAthlete, OlympicOfficial;
GRANT EXECUTE ON PROCEDURE UpdateAthleteProfile TO OlympicAthlete, OlympicOfficial;
GRANT EXECUTE ON PROCEDURE ChangeRoster TO OlympicCoach, OlympicOfficial;
GRANT EXECUTE ON PROCEDURE EnterMedalResults TO OlympicOfficial;
GRANT EXECUTE ON PROCEDURE EnterTimes TO OlympicOfficial;
GRANT EXECUTE ON PROCEDURE CreateTeam TO OlympicOfficial;
GRANT EXECUTE ON PROCEDURE DeleteTeam TO OlympicOfficial;
GRANT EXECUTE ON PROCEDURE ViewResults TO OlympicOfficial, OlympicSpectator;
GRANT EXECUTE ON PROCEDURE ViewRosters TO OlympicOfficial, OlympicSpectator;
GRANT EXECUTE ON PROCEDURE SearchPlayerByMedal TO OlympicOfficial, OlympicSpectator;
GRANT EXECUTE ON PROCEDURE SearchRosterByCountry TO OlympicOfficial, OlympicSpectator;
GRANT EXECUTE ON PROCEDURE SearchAthleteBySport TO OlympicOfficial, OlympicSpectator;
GRANT EXECUTE ON PROCEDURE SearchCompetitorByTime TO OlympicOfficial, OlympicSpectator;
GRANT EXECUTE ON PROCEDURE CreateSport TO OlympicOfficial;
GRANT EXECUTE ON PROCEDURE DesignateCoach TO OlympicOfficial;
GRANT EXECUTE ON PROCEDURE DeletePlayersFromRoster TO OlympicOfficial;
*/