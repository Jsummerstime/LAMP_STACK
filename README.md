# LAMP_STACK
A website where users can interact with a database. The information was scraped from wikipedia.
#################################################################################################
CREATED BY: Jack Summers, Ajay Hariharan, and Jillian Walsh

The application is a python file that utilizes the flask module to create a website.
The sql database is filled with information on the following olympic events: swimming, waterpolo, soccer, volleyball.
The spider file is a web scrapping program that fills the sql database.

All of the code was run on a virtual linux machine.

Finally, there were several more html files for the entirety of the website, however this singular file is provided as an example.


Objective:

The Olympic Games are one of the most watched sporting events in the world. This database will manage and store information about the 2020 Tokyo Olympic Games medalists, such as scores, players, teams and event information, with a specific focus on water polo, volleyball, soccer and swimming.

 Situation:

	The parties involved in the Olympic Games are athletes, coaches, officials and spectators. Athletes' information, such as their first name, last name and gender are recorded. Additionally, each Athlete is assigned an Athlete ID number by the system. All of this data is entered into the database by either the athlete or an International Olympic Committee (IOC) official. If at any point the information changes, either Athletes or Officials can update their profile. Each sport is entered and is designated as a team or individual sport. 

	If the sport is not a team sport, all of the competitors for a certain event are entered into the database. They will have their Athlete ID, first name, last name, and gender inherited from the Athlete table, as well as the country they are representing. There are many competitors in one event, and a single competitor can compete in many different events. Team-based events in individual sports (like Swimming) will be recorded using the same Event ID with multiple players holding the same overall team time from the same country. Individual competitors are not assigned coaches. 

	If the sport is a team sport, the athletes are listed by teams. Each team is assigned a team ID by the system. Other information listed for each team is the country they are competing for and which medal they won. Each team has a coach that is also entered into the database by officials. Coaches are able to enter and update their team rosters. Spectators of the Olympic Games have the ability to view rosters, player information and results. Additionally, spectators can look up players/competitors by medal, country, sport or time. Athletes may not be members of multiple teams, nor can a team player also be an individual competitor.

	IOC officials will act as an admin to this system and have many privileges. In addition to being able to do everything that athletes, coaches and spectators can do, officials can create a new sport into the database. After a game/event, they will enter the medal results and times that the competitors got. In case a player/competitor must leave the competition, they can delete players or delete a team. Likewise, they can create a new team if a new country decides to enter their team. An IOC official can designate a coach at any time, which gives that person coaching rights.
  
  Discussion of External Data Source:


In order to collect data to fill our database, we will scrape the web for information. Specifically, wikipedia will be the main source of information for the 2020 olympics. Water polo, soccer, volleyball and swimming are the sports that will be entered into the database. The following wikipedia sites will be used: https://en.wikipedia.org/wiki/Water_polo_at_the_2020_Summer_Olympics

https://en.wikipedia.org/wiki/Football_at_the_2020_Summer_Olympics

https://en.wikipedia.org/wiki/Volleyball_at_the_2020_Summer_Olympics

https://en.wikipedia.org/wiki/Swimming_at_the_2020_Summer_Olympics 

