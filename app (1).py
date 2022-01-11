from mysql.connector import connect
from flask import Flask, redirect, render_template, request, url_for, session
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.secret_key = "cisco"
bcrypt = Bcrypt(app)
#app = application
@app.route('/')
def hello_world():
	return '<p>Hello, World!</p>'
  
@app.route('/login', methods=['GET', 'POST'])
def login():
  #return render_template("loginForm.html", title="Olympic Database Login")
  #user = ["Test", "Test", "3"]
  if request.method == 'POST':
    pass
    email = request.form['email']
    session["email"] = email
    password = request.form['password']
    if email == 'Jillian' and password == 'Jillian':
       session["email"] = email
       #return "<h1>Test</h1>"
       return redirect(url_for("athlete"))
    elif email == 'Ajay' and password == 'Ajay':
       session["email"] = email
       return redirect(url_for("coach"))
    elif email == 'Jack' and password == 'Jack':
       session["email"] = email
       return redirect(url_for("official"))
#    else:
#      return render_template("loginForm.html", title="Olympic Database Login")
      #return  render_template("spectator.html", title="Olympic Spectator Page")
    #cnx = connect(user='????????', password='?????', database='???????')
    #cursor = cnx.cursor(prepared=True)
    #query = 'SELECT * FROM Member WHERE EmailAddress = %s;'  #update table names
    #cursor.execute(query, [request.form['email']])
    #result = cursor.fetchall()
    #cnx.close()
    #if len(result) > 0:          # Make sure we found a user
     # user = result[0]           # Get first (only!) user from results
      # user looks like [Email, LastName, FirstName, IsAdmin, hash]
      #if bcrypt.check_password_hash(user[4], request.form['password']):
       # return f"<h1>Welcome, {user[2]}!</h1>"
    #return render_template("loginForm.html", title="Login failed.")
  return render_template("loginForm.html", title="Olympic Database Login")

@app.route('/spectator', methods=['GET', 'POST'])
def spectator():
 
  if request.method == 'POST':
    #pass
    type = request.form['queryType']
    if type == '8':
      return redirect(url_for('USE8'))
    elif type == '9':
      return redirect(url_for('USE9'))
    elif type == '10':
      return redirect(url_for('USE10'))
    #elif type == '11':
    #  return redirect(url_for('USE11'))
    #elif type == '12':
    #  return redirect(url_for('USE12'))
    elif type == '13':
      return redirect(url_for('USE13'))
  return render_template("spectator.html", title="Olympic Spectator Page")


@app.route('/athlete', methods=['GET', 'POST'])
def athlete():
  if "email" in session:
    email = session["email"]
    if request.method == 'POST':
      #pass
      
      type = request.form['queryType']
      if type == '1':
        return redirect(url_for('USE1'))
      elif type == '2':
        return redirect(url_for('USE2'))
    return render_template("athlete.html", title="Olympic Athlete Page")
  else:
    return redirect(url_for("login"))

@app.route('/coach', methods=['GET', 'POST'])
def coach():
  if "email" in session:
    email = session["email"]
    if request.method == 'POST':
      #pass

      type = request.form['queryType']
      if type == '1':
        return redirect(url_for('USE3a'))
      elif type == '2':
        return redirect(url_for('USE3b'))
    return render_template("coach.html", title="Olympic Coach Page")
  else:
    return redirect(url_for("login"))

@app.route('/official', methods=['GET', 'POST'])
def official():
  if "email" in session:
    email = session["email"]
    if request.method == 'POST':
      #pass

      type = request.form['queryType']
      if type == '1':
        return redirect(url_for('USE1'))
      elif type == '2':
        return redirect(url_for('USE2'))
      elif type == '3a':
        return redirect(url_for('USE3a'))
      elif type == '3b':
        return redirect(url_for('USE3b'))
      elif type == '4':
        return redirect(url_for('USE4'))
      elif type == '5':
        return redirect(url_for('USE5'))
      elif type == '6':
        return redirect(url_for('USE6'))
      elif type == '7':
        return redirect(url_for('USE7'))
      elif type == '8':
        return redirect(url_for('USE8'))
      elif type == '9':
        return redirect(url_for('USE9'))
      elif type == '10':
        return redirect(url_for('USE10'))
      #elif type == '11':
        #return redirect(url_for('USE11'))
      #elif type == '12':
        return redirect(url_for('USE12'))
      elif type == '13':
        return redirect(url_for('USE13'))

    return render_template("official.html", title="Olympic Official Page")
  else:
    return redirect(url_for("login"))
#Use cases:

@app.route('/USE1', methods=['GET', 'POST'])
# use case 1, branch of athlete.
def USE1():
  if 'email' in session:
    email = session["email"]
    if request.method == 'POST':
      pass
      sport = request.form['sport']
      first = request.form['first']
      last = request.form['last']
      country = request.form['country']
      gender = request.form['gender']
      if sport != 'swim':
        query1 = '''INSERT INTO Player (AthleteFirstName, AthleteLastName, Country, Gender, TeamID) VALUES
        (%(first)s, %(last)s, %(country)s, %(gender)s,(SELECT TeamID FROM Team WHERE Country = %(country)s AND SportName = %(sport)s));'''
        params1 = {'sport': sport, 'first': first, 'last': last, 'country': country, 'gender': gender}
        cnx = connect(user='admin', password='4242', database='TokyoOlympics')
        cursor = cnx.cursor()
        cursor.execute(query1, params1)
        cnx.commit()
        cnx.close()

      else:
        query2 = '''INSERT INTO Competitor (AthleteFirstName, AthleteLastName, Country, Gender, SportName) VALUES
        (%(first)s, %(last)s, %(country)s, %(gender)s, %(sport)s);'''
        params2 = {'sport': sport, 'first': first, 'last': last, 'country': country, 'gender': gender}
        cnx = connect(user='admin', password='4242', database='TokyoOlympics')
        cursor = cnx.cursor()
        cursor.execute(query2, params2)
        cnx.commit()
        cnx.close()

    return render_template('USE1.html', title="Enter Personal Information")

@app.route('/USE2', methods = ['GET', 'POST'])
def USE2():
  #use case 2, branch of athlete
  if 'email' in session:
    email = session['email']
    if request.method == 'POST':
      #U = updated name, O = old name
      sport = request.form['sport']
      Ofirst = request.form['Ofirst']
      Ufirst = request.form['Ufirst']
      Olast = request.form['Olast']
      Ulast = request.form['Ulast']
      Ocountry = request.form['Ocountry']
      Ucountry = request.form['Ucountry']
      Ogender = request.form['Ogender']
      Ugender = request.form['Ugender']
      if sport != 'swim':
        query1 = '''UPDATE Player SET AthleteFirstName = %(Ufirst)s, AthleteLastName = %(Ulast)s, Country = %(Ucountry)s, Gender = %(Ugender)s
        WHERE AthleteFirstName = %(Ofirst)s AND AthleteLastName = %(Olast)s AND Country = %(Ocountry)s AND Gender = %(Ogender)s;'''
        params1 = {'sport': sport, 'Ofirst': Ofirst, 'Ufirst': Ufirst, 'Olast': Olast, 'Ulast': Ulast, 'Ocountry': Ocountry, 'Ucountry': Ucountry, 'Ogender': Ogender, 'Ugender': Ugender}
        cnx = connect(user='admin', password='4242', database='TokyoOlympics')
        cursor = cnx.cursor()
        cursor.execute(query1, params1)
        cnx.commit()
        cnx.close()
      else:
        query2 = '''UPDATE Competitor SET AthleteFirstName = %(Ufirst)s, AthleteLastName = %(Ulast)s, Country = %(Ucountry)s, Gender = %(Ugender)s
        WHERE AthleteFirstName = %(Ofirst)s AND AthleteLastName = %(Olast)s AND Country = %(Ocountry)s AND Gender = %(Ogender)s ;'''
        params2 = {'sport': sport, 'Ofirst': Ofirst, 'Ufirst': Ufirst, 'Olast': Olast, 'Ulast': Ulast, 'Ocountry': Ocountry, 'Ucountry': Ucountry, 'Ogender': Ogender, 'Ugender': Ugender}
        cnx = connect(user='admin', password='4242', database='TokyoOlympics')
        cursor = cnx.cursor()
        cursor.execute(query2, params2)
        cnx.commit()
        cnx.close()

    return render_template('USE2.html', title = 'Update Athlete Profile')

@app.route('/USE3a', methods=['GET', 'POST'])
# use case 3a, branch of coach.
def USE3a():
  if 'email' in session:
    email = session["email"]
    if request.method == 'POST':
      pass
      sport = request.form['sport']
      first = request.form['first']
      last = request.form['last']
      country = request.form['country']
      gender = request.form['gender']
      if sport != 'swim':
        query1 = '''INSERT INTO Player (AthleteFirstName, AthleteLastName, Country, Gender, TeamID) VALUES
        (%(first)s, %(last)s, %(country)s, %(gender)s,(SELECT TeamID FROM Team WHERE Country = %(country)s AND SportName = %(sport)s));'''
        params1 = {'sport': sport, 'first': first, 'last': last, 'country': country, 'gender': gender}
        cnx = connect(user='admin', password='4242', database='TokyoOlympics')
        cursor = cnx.cursor()
        cursor.execute(query1, params1)
        cnx.commit()
        cnx.close()
      else:
        query2 = '''INSERT INTO Competitor (AthleteFirstName, AthleteLastName, Country, Gender, SportName) VALUES
        (%(first)s, %(last)s, %(country)s, %(gender)s, %(sport)s);'''
        params2 = {'sport': sport, 'first': first, 'last': last, 'country': country, 'gender': gender}
        cnx = connect(user='admin', password='4242', database='TokyoOlympics')
        cursor = cnx.cursor()
        cursor.execute(query2, params2)
        cnx.commit()
        cnx.close()

    return render_template('USE3a.html', title="Add Player To Roster")

@app.route('/USE3b', methods=['GET', 'POST'])
# use case 3b, branch of coach.
def USE3b():
  if 'email' in session:
    email = session["email"]
    if request.method == 'POST':
      
      sport = request.form['sport']
      first = request.form['first']
      last = request.form['last']
      country = request.form['country']
      gender = request.form['gender']
      if sport != 'swim':
        query1 = '''Delete FROM Player WHERE AthleteFirstName = %(first)s AND AthleteLastName = %(last)s AND Country = %(country)s AND Gender = %(gender)s;'''
        params1 = {'sport': sport, 'first': first, 'last': last, 'country': country, 'gender': gender}
        cnx = connect(user='admin', password='4242', database='TokyoOlympics')
        cursor = cnx.cursor()
        cursor.execute(query1, params1)
        cnx.commit()
        cnx.close()
      else:
        query2 = '''Delete FROM Competitor WHERE AthleteFirstName = %(first)s AND AthleteLastName = %(last)s AND Country =  %(country)s
        AND Gender =  %(gender)s AND SportName =  %(sport)s;'''
        params2 = {'sport': sport, 'first': first, 'last': last, 'country': country, 'gender': gender}
        cnx = connect(user='admin', password='4242', database='TokyoOlympics')
        cursor = cnx.cursor()
        cursor.execute(query2, params2)
        cnx.commit()
        cnx.close()

    return render_template('USE3b.html', title="Delete Player From Roster")

@app.route('/USE4', methods=['GET', 'POST'])
# use case 4, branch of official.
def USE4():
  if 'email' in session:
    email = session["email"]
    if request.method == 'POST':
      
      sport = request.form['sport']
      medal = request.form['medal']
      country = request.form['country']
      first = request.form['first']
      last = request.form['last']
      if sport != 'swim':
        query1 = '''UPDATE Team SET MedalWon = %(medal)s WHERE Country = %(country)s AND SportName = %(sport)s;'''
        params1 = {'sport': sport, 'medal': medal, 'country': country}
        cnx = connect(user='admin', password='4242', database='TokyoOlympics')
        cursor = cnx.cursor()
        cursor.execute(query1, params1)
        cnx.commit()
        cnx.close()
      else:
        query2 = '''UPDATE EventCompetition SET MedalWon = %(medal)s WHERE AthleteID = 
        (SELECT AthleteID FROM Competitor WHERE AthleteFirstName = %(first)s AND AthleteLastName = %(last)s AND Country = %(country)s);'''
        params2 = {'sport': sport, 'first': first, 'last': last, 'country': country, 'medal': medal}
        cnx = connect(user='admin', password='4242', database='TokyoOlympics')
        cursor = cnx.cursor()
        cursor.execute(query2, params2)
        cnx.commit()
        cnx.close()

    return render_template('USE4.html', title="Enter Medal Results")

@app.route('/USE5', methods=['GET', 'POST'])
# use case 5, branch of official.                                           
def USE5():
  if 'email' in session:
    email = session["email"]
    if request.method == 'POST':
      
      event = request.form['event'] #100m Backstroke
      time = request.form['time']  #format 00:00:00
      country = request.form['country'] #USA
      first = request.form['first']
      last = request.form['last']
      
      query1 = '''UPDATE EventCompetition SET Time = %(time)s WHERE AthleteID IN (SELECT AthleteID FROM Competitor WHERE AthleteFirstName = %(first)s AND AthleteLastName = %(last)s AND
      Country = %(country)s) AND EventName = %(event)s;'''
      params1 = {'event': event, 'time': time, 'country': country, 'first': first, 'last': last}
      cnx = connect(user='admin', password='4242', database='TokyoOlympics')
      cursor = cnx.cursor()
      cursor.execute(query1, params1)
      cnx.commit()
      cnx.close()

    return render_template('USE5.html', title="Enter Times")


@app.route('/USE6', methods=['GET', 'POST'])
# use case 6, branch of official.
def USE6():
  if 'email' in session:
    email = session["email"]
    if request.method == 'POST':
      
      sport = request.form['sport']
      country = request.form['country']
      medal = request.form['medal']
      gender = request.form['gender']
      query1 = '''INSERT INTO Team (SportName, Country, MedalWon, Gender) VALUES (%(sport)s, %(country)s, %(medal)s, %(gender)s);'''
      params1 = {'sport': sport, 'medal': medal, 'country': country, 'gender': gender}
      cnx = connect(user='admin', password='4242', database='TokyoOlympics')
      cursor = cnx.cursor()
      cursor.execute(query1, params1)
      cnx.commit()
      cnx.close()

    return render_template('USE6.html', title="Create Team")

@app.route('/USE7', methods=['GET', 'POST'])
# use case 7, branch of official.
def USE7():
  if 'email' in session:
    email = session["email"]
    if request.method == 'POST':
      
      sport = request.form['sport']
      country = request.form['country']
      query1 = '''DELETE FROM Team WHERE SportName = %(sport)s AND Country = %(country)s;'''
      params1 = {'sport': sport, 'country': country}
      cnx = connect(user='admin', password='4242', database='TokyoOlympics')
      cursor = cnx.cursor()
      cursor.execute(query1, params1)
      cnx.commit()
      cnx.close()

    return render_template('USE7.html', title="Delete Teams")

@app.route('/USE8', methods=['GET', 'POST'])
def USE8():
  
  #use case 8, branch of spectator.  
  if request.method == 'POST':
    
    sport = request.form['sport']
    if sport != 'swim':
      query1 = 'SELECT TeamID, Country, MedalWon FROM Team WHERE SportName = %(sport)s' # GROUP BY Country ORDER BY Country;'
      params1 = {'sport': request.form['sport']}
      cnx = connect(user='admin', password='4242', database='TokyoOlympics')
      cursor = cnx.cursor()
      cursor.execute(query1, params1)
      response = 'TeamID, Country, MedalWon' + '<br />\n'
      for result in cursor.fetchall():
        response += ' '.join(str(result)) + '<br />\n'
      cnx.close()
      return response
      
    else: 
      query2 = 'SELECT EventName, AthleteID, AthleteFirstName, AthleteLastname, Time, MedalWon FROM EventCompetition NATURAL JOIN Competitor;'
      cnx = connect(user='admin', password='4242', database='TokyoOlympics')
      cursor = cnx.cursor()
      cursor.execute(query2)
      response = 'EventName, AthleteID, AthleteFirstName, AthleteLastname, Time, MedalWon' + '<br />\n'
      for result in cursor.fetchall():
        response += ' '.join(str(result)) + '<br />\n'
      cnx.close()
      return response

  return render_template('USE8.html', title="View All Results")
  

@app.route('/USE9', methods=['GET', 'POST'])
def USE9():

  #use case 9, branch of spectator.
  if request.method == 'POST':
    pass
    sport = request.form['sport']
    if sport != 'swim':
      query1 = 'SELECT AthleteID, AthleteFirstName, AthleteLastName, Gender, Country FROM Player NATURAL JOIN Team WHERE SportName = %(sport)s;'
      params1 = {'sport': request.form['sport']}
      cnx = connect(user='admin', password='4242', database='TokyoOlympics')
      cursor = cnx.cursor()
      cursor.execute(query1, params1)
      response = 'AthleteID, AthleteFirstName, AthleteLastName, Gender, Country' + '<br />\n'
      for result in cursor.fetchall():
        response += ' '.join(str(result)) + '<br />\n'
      cnx.close()
      return response
    else:
      query2 = 'SELECT AthleteID, AthleteFirstName, AthleteLastName, Gender, Country FROM Competitor;' #GROUP BY Country ORDER BY Country;'
      cnx = connect(user='admin', password='4242', database='TokyoOlympics')
      cursor = cnx.cursor()
      cursor.execute(query2)
      response = 'AthleteID, AthleteFirstName, AthleteLastName, Gender, Country' + '<br />\n'
      for result in cursor.fetchall():
        response += ' '.join(str(result)) + '<br />\n'
      cnx.close()
      return response
  return render_template('USE9.html', title="View Rosters")

@app.route('/USE10', methods=['GET', 'POST'])
def USE10():

  #use case 10, branch of spectator.
  if request.method == 'POST':
    pass
    medal = request.form['medal']
    sport = request.form['sport']
    country = request.form['country']
    if sport != 'swim':
      query1 = 'SELECT AthleteID, AthleteFirstName, AthleteLastName, Gender FROM Player NATURAL JOIN Team WHERE SportName = %(sport)s AND MedalWon = %(medal)s AND Country = %(country)s;' #GROUP BY Country ORDER BY Country;'
      params1 = {'sport': request.form['sport'], 'country': request.form['country'], 'medal': request.form['medal']}
      cnx = connect(user='admin', password='4242', database='TokyoOlympics')
      cursor = cnx.cursor()
      cursor.execute(query1, params1)
      response = 'AthleteID, AthleteFirstName, AthleteLastName, Gender' + '<br />\n'
      for result in cursor.fetchall():
        response += ' '.join(str(result)) + '<br />\n'
      cnx.close()
      return response
    else:
      query2 = 'SELECT AthleteID, AthleteFirstName, AthleteLastName, Gender FROM Competitor NATURAL JOIN EventCompetition WHERE SportName = %(sport)s AND MedalWon = %(medal)s AND Country = %(country)s;' #GROUP BY Country ORDER BY Country;'
      param2 = {'sport': request.form['sport'], 'country': request.form['country'], 'medal': request.form['medal']}
      cnx = connect(user='admin', password='4242', database='TokyoOlympics')
      cursor = cnx.cursor()
      cursor.execute(query2, param2)
      response = 'AthleteID, AthleteFirstName, AthleteLastName, Gender' + '<br />\n'
      for result in cursor.fetchall():
        response += ' '.join(str(result)) + '<br />\n'
      cnx.close()
      return response
  return render_template('USE10.html', title="Player or Team by Medal")

#@app.route('/USE11', methods=['GET', 'POST'])
#def USE11():                                       #do not use

  #use case 11, branch of spectator.
#  if request.method == 'POST':
#    pass
#  return render_template('USE11.html', title="Rosters by Country")

#@app.route('/USE12', methods=['GET', 'POST'])
#def USE12():                                      #do not use

  #use case 12, branch of spectator.
# if request.method == 'POST':
#    pass
    
#  return render_template('USE12.html', title="Athlete by Sport")

@app.route('/USE13', methods=['GET', 'POST'])
def USE13():

  #use case 13, branch of spectator.
  if request.method == 'POST':
    
    time = request.form['time']    #format 00:00:00
    query1 = 'SELECT AthleteID, AthleteFirstName, AthleteLastName, Gender, Time FROM Competitor NATURAL JOIN EventCompetition WHERE EventName = %(event)s AND Time = %(time)s;' #AND Country = %(country)s;' #GROUP BY Country ORDER BY Country;'
    param1 = {'event': request.form['event'], 'time': time} #'country': request.form['country'], 
    cnx = connect(user='admin', password='4242', database='TokyoOlympics') 
    cursor = cnx.cursor()
    #cursor.execute("SELECT * FROM EventCompetition WHERE Time = '00:00:10';")
    cursor.execute(query1, param1)
    response = ''
    for result in cursor.fetchall():
      response += ' '.join(str(result)) + '<br />\n'
    cnx.close()
    return response
  return render_template('USE13.html', title="Competitors by Time")