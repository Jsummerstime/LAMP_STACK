from bs4 import BeautifulSoup
from mysql.connector import connect
from os import path
from requests import get
import re

def VolleyballScrape(url):
    

    resp = get(url)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, 'html.parser')
        hold = []
        for items in soup.find('table', {'class':'wikitable plainrowheaders'}).find_all('tr')[1::1]:
            data = items.find_all(['th','td'])
            try:
                hold.append(data[0].text[0:-8] + " Volleyball")
                roster1 = (re.findall('[A-Z][^A-Z]*', data[1].text))
                rs1 = []
                for i in roster1:
                    if i.count(" ") > 0:
                        rs1.append(i.strip(" "))
                    elif i.count("\n") > 0:
                        rs1.append(i.strip("\n"))
                    else:
                        rs1.append(i)
                for i in rs1:
                    if i.count("\n") >0:
                        i == i.strip("\n")
                #print(rs1)
                hold.append(rs1)
                roster2 = re.findall('[A-Z][^A-Z]*', data[2].text)
                rs2 = []
                for i in roster2:
                    if i.count(" ") > 0:
                        rs2.append(i.strip(" "))
                    elif i.count("\n") > 0:
                        rs2.append(i.strip("\n"))
                    else:
                        rs2.append(i)
                hold.append(rs2)
                roster3 = re.findall('[A-Z][^A-Z]*', data[3].text)
                rs3 = []
                for i in roster3:
                    if i.count(" ") > 0:
                        rs3.append(i.strip(" "))
                    elif i.count("\n") > 0:
                        rs3.append(i.strip("\n"))
                    else:
                        rs3.append(i)
                hold.append(rs3)
            except IndexError:
                pass
        
        MensFrance = []
        WomensUS = []
        MensROC = []
        WomensBrazil = []
        MensArgentina = []
        WomensSerbia = []
        q = 1
        while q <= len(hold[1][1:-5]):
            try:
                if len(hold[1][q+1]) > 2:
                    MensFrance.append(["France",hold[1][q], hold[1][q+1], "G", "M"])
                    q+=2
                elif hold[1][q][-1+1] == "-":
                     MensFrance.append(["France",hold[1][q]," ".join(hold[1][q+1:q+3]), "G", "M"])
                     q+=3
                else:
                     MensFrance.append(["France",hold[1][q], " ".join(hold[1][q+1:q+3]), "G", "M"])
                     q+=3
            except:
                break
        MensFrance.append([hold[1][-3][0:-1],str(hold[1][-2])+" "+str(hold[1][-1])])
        q = 3
        while q <= len(hold[2][1:-5]):
            try:
                if len(hold[2][q+1]) > 2:
                    MensROC.append(["ROC", hold[2][q], hold[2][q+1], "S", "M"])
                    q+=2
                elif hold[2][q][-1+1] == "-":
                     MensROC.append(["ROC",hold[2][q]," ".join(hold[2][q+1:q+3]), "S", "M"])
                     q+=3
                else:
                     MensROC.append(["ROC",hold[2][q]," ".join(hold[2][q+1:q+3]), "S", "M"])
                     q+=3
            except:
                break
        MensROC.append([hold[2][-3][0:-1],str(hold[2][-2])+" "+str(hold[2][-1])])

        q = 1
        while q <= len(hold[3][1:-5]):
            try:
                if hold[3][q+1][-2:] == "da" or hold[3][q+1][-2:] == "de":
                    MensArgentina.append(["Argentina",hold[3][q]," ".join(hold[3][q+1:q+3]), "B", "M"])
                    q+=3
                if len(hold[3][q+1]) > 2:
                    MensArgentina.append(["Argentina",hold[3][q],hold[3][q+1], "B", "M"])
                    q+=2
                elif hold[3][q][-1+1] == "-":
                     MensArgentina.append(["Argentina",hold[3][q]," ".join(hold[3][q+1:q+3]), "B", "M"])
                     q+=3
                else:
                     MensArgentina.append(["Argentina",hold[3][q]," ".join(hold[3][q+1:q+3]), "B", "M"])
                     q+=3
            except:
                break
        MensArgentina.append([hold[3][-3][0:-1],str(hold[3][-2])+" "+str(hold[3][-1])])

        q = 2
        while q <= len(hold[5][1:-5]):
            try:
                if len(hold[5][q+1]) > 2 and hold[5][q+1][-1] != "-":
                    WomensUS.append(["United States",hold[5][q],hold[5][q+1], "G", "F"])
                    q+=2    
                elif hold[5][q+1][-1] == "-":
                     WomensUS.append(["United States",hold[5][q],"".join(hold[5][q+1:q+3]), "G", "F"])
                     q+=3
                else:
                     WomensUS.append(["United States",hold[5][q], " ".join(hold[5][q+1:q+3]), "G", "F"])
                     q+=3
            except:
                break
        WomensUS.append([hold[5][-3][0:-1],str(hold[5][-2])+" "+str(hold[5][-1])])

        q = 1
        while q <= len(hold[6][1:-5]):
            try:
                if hold[6][q+1][-2:] == "da" or hold[6][q+1][-2:] == "de":
                    WomensBrazil.append(["Brazil",hold[6][q]," ".join(hold[6][q+1:q+3]), "S", "F"])
                    q+=3
                if len(hold[6][q+1]) > 2 and hold[6][q+1][-1] != "-":
                    WomensBrazil.append(["Brazil",hold[6][q],hold[6][q+1], "S", "F"])
                    q+=2
                elif hold[6][q+1][-1] == "-":
                     WomensBrazil.append(["Brazil",hold[6][q]," ".join(hold[6][q+1:q+3]), "S", "F"])
                     q+=3
                else:
                     WomensBrazil.append(["Brazil",hold[6][q]," ".join(hold[6][q+1:q+5]), "S", "F"])
                     q+=5
            except:
                break
        WomensBrazil.append([hold[6][-3][0:-1],str(hold[6][-2])+" "+str(hold[6][-1])])

        q = 1
        while q <= len(hold[7][1:-5]):
            try:
                if len(hold[7][q+1]) > 2:
                    WomensSerbia.append(["Serbia",hold[7][q],hold[7][q+1], "B", "F"])
                    q+=2
                elif hold[7][q][-1+1] == "-":
                     WomensSerbia.append(["Serbia",hold[7][q]," ".join(hold[7][q+1:q+3]), "B", "F"])
                     q+=3
                else:
                     WomensSerbia.append(["Serbia",hold[7][q]," ".join(hold[7][q+1:q+3]), "B", "F"])
                     q+=3
            except:
                break
        WomensSerbia.append([hold[7][-3][0:-1],str(hold[7][-2])+" "+str(hold[7][-1])])
        
        hold = []
        hold.append(["Country", "FirstName","LastName"," Medal", "Gender"])
        hold.append(MensFrance)
        hold.append(MensROC)
        hold.append(MensArgentina)
        hold.append(WomensUS)
        hold.append(WomensBrazil)
        hold.append(WomensSerbia)

        return hold
def MensSwimScrape(URL):
    resp = get(URL)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, 'html.parser')
        hold = []
        tables = soup.find_all('table', {'class':'wikitable plainrowheaders'})
        for table in tables:
            table_rows = table.find_all('tr')
            for tr in table_rows:
                td = tr.find_all('td')
                row = [i.text for i in td]
                hold.append(row)

    cleanerlist1 = []
    cleanerlist2 = []

    MensSwim = []

    for i in hold:
        if i != [] and i != ['\n']:
            cleanerlist1.append(i)


    for i in cleanerlist1[0:14]:
        try:
            cleanerlist2.append([i[0][0:-8],i[1].split("\xa0"),i[2][0:-1],i[3].split("\xa0"),i[4][0:-1],i[5].split("\xa0"),i[6][0:-1]])
        except:
            pass

    
    for i in cleanerlist2:
        MensSwim.append([i[0]])
        MensSwim.append([i[0]])
        MensSwim.append([i[0]])

    q = 0
    for i in cleanerlist2:
        MensSwim[q].append(i[1][0].split(" ")[0])
        MensSwim[q].append(i[1][0].split(" ")[1])
        MensSwim[q].append(i[1][1])
        MensSwim[q].append(i[2].strip(" OR").strip(" AF").strip(" AM").strip(" SA").strip(" AS").strip(" ER").strip(" OC").strip(" WJR").strip(" WR").strip(" NR").strip(" OR,"))
        MensSwim[q].append("G")
        MensSwim[q].append("M")
        q += 3
    
    q = 1
    for i in cleanerlist2:
        MensSwim[q].append(i[3][0].split(" ")[0])
        MensSwim[q].append(i[3][0].split(" ")[1])
        MensSwim[q].append(i[3][1])
        MensSwim[q].append(i[4].strip(" OR").strip(" AF").strip(" AM").strip(" SA").strip(" AS").strip(" ER").strip(" OC").strip(" WJR").strip(" WR").strip(" NR").strip(" OR,"))
        MensSwim[q].append("S")
        MensSwim[q].append("M")
        q += 3
    
    q = 2
    for i in cleanerlist2:
        MensSwim[q].append(i[5][0].split(" ")[0])
        MensSwim[q].append(i[5][0].split(" ")[1])
        MensSwim[q].append(i[5][1])
        MensSwim[q].append(i[6].strip(" OR").strip(" AF").strip(" AM").strip(" SA").strip(" AS").strip(" ER").strip(" OC").strip(" WJR").strip(" WR").strip(" NR").strip(" OR,"))
        MensSwim[q].append("B")
        MensSwim[q].append("M")
        q += 3
    
    headers = ["Event", "FirstName","LastName", "Country", "Time", "Medal", "Gender"]
    MensSwim.insert(0,headers)
    
    return MensSwim

def WomensSwimScrape(URL):
    resp = get(URL)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, 'html.parser')
        hold = []
        tables = soup.find_all('table', {'class':'wikitable plainrowheaders'})
        for table in tables:
            table_rows = table.find_all('tr')
            for tr in table_rows:
                td = tr.find_all('td')
                row = [i.text for i in td]
                hold.append(row)
    
    cleanerlist1 = []
    cleanerlist2 = []

    WomensSwim = []

    for i in hold:
        if i != [] and i != ['\n']:
            cleanerlist1.append(i)

    
    for i in cleanerlist1[19:33]:
        try:
            cleanerlist2.append([i[0][0:-8],i[1].split("\xa0"),i[2][0:-1],i[3].split("\xa0"),i[4][0:-1],i[5].split("\xa0"),i[6][0:-1]])
        except:
            pass

    for i in cleanerlist2:
        WomensSwim.append([i[0]])
        WomensSwim.append([i[0]])
        WomensSwim.append([i[0]])

    q = 0
    for i in cleanerlist2:
        WomensSwim[q].append(i[1][0].split(" ")[0])
        WomensSwim[q].append(i[1][0].split(" ")[1])
        WomensSwim[q].append(i[1][1])
        WomensSwim[q].append(i[2].strip(" OR").strip(" AF").strip(" AM").strip(" SA").strip(" AS").strip(" ER").strip(" OC").strip(" WJR").strip(" WR").strip(" NR").strip(" OR,"))
        WomensSwim[q].append("G")
        WomensSwim[q].append("F")
        q += 3
    
    q = 1
    for i in cleanerlist2:
        WomensSwim[q].append(i[3][0].split(" ")[0])
        WomensSwim[q].append(i[3][0].split(" ")[1])
        WomensSwim[q].append(i[3][1])
        WomensSwim[q].append(i[4].strip(" OR").strip(" AF").strip(" AM").strip(" SA").strip(" AS").strip(" ER").strip(" OC").strip(" WJR").strip(" WR").strip(" NR").strip(" OR,"))
        WomensSwim[q].append("S")
        WomensSwim[q].append("F")
        q += 3
    
    q = 2
    for i in cleanerlist2:
        WomensSwim[q].append(i[5][0].split(" ")[0])
        WomensSwim[q].append(i[5][0].split(" ")[1])
        WomensSwim[q].append(i[5][1])
        WomensSwim[q].append(i[6].strip(" OR").strip(" AF").strip(" AM").strip(" SA").strip(" AS").strip(" ER").strip(" OC").strip(" WJR").strip(" WR").strip(" NR").strip(" OR,"))
        WomensSwim[q].append("B")
        WomensSwim[q].append("F")
        q += 3
    
    headers = ["Event", "FirstName","LastName", "Country", "Time", "Medal", "Gender"]
    WomensSwim.insert(0,headers)
    
    return WomensSwim

def WaterPoloScrape(url):
    resp = get(url)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, 'html.parser')
        hold = []
        for items in soup.find('table', {'class':'wikitable plainrowheaders'}).find_all('tr')[1::1]:
            data = items.find_all(['th','td'])
            try:
                hold.append(data[0].text[0:-8] + " Water Polo")
                roster1 = (re.findall('[A-Z][^A-Z]*', data[1].text))
                rs0 = []
                for i in roster1:
                    if i.count(" ") > 0:
                        rs0.append(i.strip(" "))
                    elif i.count("\n") > 0:
                        rs0.append(i.strip("\n"))
                    else:
                        rs0.append(i)
                for i in rs0:
                    if i.count("\n") >0:
                        i == i.strip("\n")
                rs1 = []
                q = 0
                while q < 8:
                    rs1.append(rs0[q])
                    q+=1
                rs1.append(rs0[8][0:6])
                rs1.append(rs0[8][6:])
                q = 9
                while q < len(rs0):
                    rs1.append(rs0[q])
                    q+=1
              
                hold.append(rs1)
                roster2 = re.findall('[A-Z][^A-Z]*', data[2].text)
                rs2 = []
                for i in roster2:
                    if i.count(" ") > 0:
                        rs2.append(i.strip(" "))
                    elif i.count("\n") > 0:
                        rs2.append(i.strip("\n"))
                    else:
                        rs2.append(i)
                hold.append(rs2)
                roster3 = re.findall('[A-Z][^A-Z]*', data[3].text)
                rs3 = []
                for i in roster3:
                    if i.count(" ") > 0:
                        rs3.append(i.strip(" "))
                    elif i.count("\n") > 0:
                        rs3.append(i.strip("\n"))
                    else:
                        rs3.append(i)
                hold.append(rs3)
            except IndexError:
                pass

        MensSerbia = []
        WomensUS = []
        MensGreece = []
        WomensSpain = []
        MensHungary = []
        WomensHungary = []
        q = 1
        while q <= len(hold[1][1:]):
            try:
                if len(hold[1][q+1]) > 2:
                    MensSerbia.append(["Serbia",hold[1][q], hold[1][q+1], "G", "M"])
                    q+=2
            except:
                break
        MensSerbia.append(["Head coach:", "Dejan Savić"])
        
        q = 1
        while q <= len(hold[2][1:]):
            try:
                if len(hold[2][q+1]) > 2:
                    MensGreece.append(["Greece", hold[2][q], hold[2][q+1], "S", "M"])
                    q+=2
            except:
                break
        MensGreece.append(["Head coach:", "Thodoris Vlachos"])

        q = 1
        while q <= len(hold[3][1:]):
            try:
                if len(hold[3][q+1]) > 2:
                    MensHungary.append(["Hungary", hold[3][q], hold[3][q+1], "B", "M"])
                    q+=2
            except:
                break
        MensHungary.append(["Head coach:", "Tamás Märcz"])
        
        q = 1
        while q <= len(hold[5][1:]):
            try:
                if len(hold[5][q+1]) > 2:
                    WomensUS.append(["United States", hold[5][q], hold[5][q+1], "G", "F"])
                    q+=2
            except:
                break
        WomensUS.append(["Head coach:", "Adam Krikorian"])
        
        q = 1
        while q <= len(hold[6][1:]):
            try:
                if len(hold[6][q+1]) > 2:
                    WomensSpain.append(["Spain", hold[6][q], hold[6][q+1], "S", "F"])
                    q+=2
            except:
                break
        WomensSpain.append(["Head coach:", "Miki Oca"])
        
        q = 1
        while q <= len(hold[7][1:]):
            try:
                if len(hold[7][q+1]) > 2:
                    WomensHungary.append(["Hungary", hold[7][q], hold[7][q+1], "B", "F"])
                    q+=2
            except:
                break
        WomensHungary.append(["Head coach:", "Attila Bíró"])

        hold = []
        hold.append(["Country", "FirstName","LastName"," Medal", "Gender"])
        hold.append(MensSerbia)
        hold.append(MensGreece)
        hold.append(MensHungary)
        hold.append(WomensUS)
        hold.append(WomensSpain)
        hold.append(WomensHungary)
        return hold
    
def SoccerScrape(url):
    
    
    
    
    

    
    resp = get(url)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, 'html.parser')
        hold = []
        for items in soup.find('table', {'class':'wikitable plainrowheaders'}).find_all('tr')[1::1]:
            data = items.find_all(['th','td'])
            try:
                hold.append(data[0].text[0:-8] + " Water Polo")
                roster1 = (re.findall('[A-Z][^A-Z]*', data[1].text))
                rs0 = []
                for i in roster1:
                    if i.count(" ") > 0:
                        rs0.append(i.strip(" "))
                    elif i.count("\n") > 0:
                        rs0.append(i.strip("\n"))
                    else:
                        rs0.append(i)
                for i in rs0:
                    if i.count("\n") >0:
                        i == i.strip("\n")
                rs1 = []
                q = 0
                while q < 8:
                    rs1.append(rs0[q])
                    q+=1
                rs1.append(rs0[8][0:6])
                rs1.append(rs0[8][6:])
                q = 9
                while q < len(rs0):
                    rs1.append(rs0[q])
                    q+=1
              
                hold.append(rs1)
                roster2 = re.findall('[A-Z][^A-Z]*', data[2].text)
                rs2 = []
                for i in roster2:
                    if i.count(" ") > 0:
                        rs2.append(i.strip(" "))
                    elif i.count("\n") > 0:
                        rs2.append(i.strip("\n"))
                    else:
                        rs2.append(i)
                hold.append(rs2)
                roster3 = re.findall('[A-Z][^A-Z]*', data[3].text)
                rs3 = []
                for i in roster3:
                    if i.count(" ") > 0:
                        rs3.append(i.strip(" "))
                    elif i.count("\n") > 0:
                        rs3.append(i.strip("\n"))
                    else:
                        rs3.append(i)
                hold.append(rs3)
            except IndexError:
                pass

        MensBrazil = []
        WomensCanada = []
        MensSpain = []
        WomensSweden = []
        MensMexico = []
        WomensUS = []
        q = 2
        MensBrazil.append(["Brazil","Aderbar", "Melo dos Santos Neto", "G", "M"])
        while q <= len(hold[1][2:8]):
            MensBrazil.append(["Brazil",hold[1][q], hold[1][q+1], "G", "M"])
            q+=2
        MensBrazil.append(["Brazil","".join(hold[1][8:10]), hold[1][10], "G", "M"])
        MensBrazil.append(["Brazil",(hold[1][11]), hold[1][12], "G", "M"])
        MensBrazil.append(["Brazil","Paulo", "Henrique", "G", "M"])
        MensBrazil.append(["Brazil","Bruno", "Guimarães", "G", "M"])
        MensBrazil.append(["Brazil","Matheus", "Cunha", "G", "M"])
        MensBrazil.append(["Brazil","Richarlison", "de Andrade", "G", "M"])
        MensBrazil.append(["Brazil","Antony", "Matheus", "G", "M"])
        MensBrazil.append(["Brazil","Brenno", "Oliveira", "G", "M"])
        MensBrazil.append(["Brazil","Dani", "Alves", "G", "M"])
        MensBrazil.append(["Brazil","Bruno", "Fuchs", "G", "M"])
        MensBrazil.append(["Brazil","Marcilio", "Florencio", "G", "M"])
        MensBrazil.append(["Brazil","Abner", "Vinícius", "G", "M"])
        MensBrazil.append(["Brazil","Malcom", "Filipe", "G", "M"])
        MensBrazil.append(["Brazil","Matheus", "Henrique", "G", "M"])
        MensBrazil.append(["Brazil","Reinier", "Jesus", "G", "M"])
        MensBrazil.append(["Brazil","Cláudio", "Luiz", "G", "M"])
        MensBrazil.append(["Brazil","Gabriel", "Martinelli", "G", "M"])
        MensBrazil.append(["Brazil","Lucas", "Alexandre", "G", "M"])
        MensBrazil.append(["Head coach:", "André Jardine"])
        
        MensSpain.append(["Spain", "Unai", "Simón", "S", "M"])
        MensSpain.append(["Spain", "Óscar", "Mingueza", "S", "M"])
        q = 4
        while q <= len(hold[2][1:22]):
            try:
                if len(hold[2][q+1]) > 2:
                    MensSpain.append(["Spain", hold[2][q], hold[2][q+1], "S", "M"])
                    q+=2
            except:
                break
        MensSpain.append(["Spain", "Eric", "García", "S", "M"])
        MensSpain.append(["Spain", "Álvaro","Fernández", "S", "M"])
        MensSpain.append(["Spain", "Carlos","Soler", "S", "M"])
        MensSpain.append(["Spain", "Jon", "Moncayola", "S", "M"])
        MensSpain.append(["Spain", "Pedro","González", "S", "M"])
        MensSpain.append(["Spain", "Javi","Puado", "S", "M"])
        MensSpain.append(["Spain", "Óscar", "Gil", "S", "M"])
        q = 33
        while q <= len(hold[2]):
            try:
                if len(hold[2][q+1]) > 2:
                    MensSpain.append(["Spain", hold[2][q], hold[2][q+1], "S", "M"])
                    q+=2
            except:
                break
        MensSpain.append(["Head coach:", "Luis de la Fuente"])

        q = 1
        while q <= len(hold[3][1:24]):
            try:
                if len(hold[3][q+1]) > 2:
                    MensMexico.append(["Mexico", hold[3][q], hold[3][q+1], "B", "M"])
                    q+=2
            except:
                break
        MensMexico.append(["Mexico", "Érick", "Aguirre", "B", "M"])
        MensMexico.append(["Mexico", "Uriel", "Antuna", "B", "M"])
        MensMexico.append(["Mexico", "José", "Joaquín Esquivel", "B", "M"])
        q = 33 
        while q <= len(hold[3]):
            try:
                if len(hold[3][q+1]) > 2:
                    MensMexico.append(["Mexico", hold[3][q], hold[3][q+1], "B", "M"])
                    q+=2
            except:
                break
        MensMexico.append(["Head coach:", "Jaime Lozano"])
        
        q = 1
        while q <= len(hold[5][1:7]):
            try:
                if len(hold[5][q+1]) > 2:
                    WomensCanada.append(["Canada", hold[5][q], hold[5][q+1], "G", "F"])
                    q+=2
            except:
                break
        WomensCanada.append(["Canada", "Shelina", "Zadorsky", "G", "F"])
        WomensCanada.append(["Canada", "Rebecca", "Quinn", "G", "F"])
        q = 11
        while q <= len(hold[5][11:32]):
            try:
                if len(hold[5][q+1]) > 2:
                    WomensCanada.append(["Canada", hold[5][q], hold[5][q+1], "G", "F"])
                    q+=2
            except:
                break
        WomensCanada.append(["Canada", "Christine", "Sinclair", "G", "F"])
        WomensCanada.append(["Canada", "Évelyne", "Viens", "G", "F"])
        q = 26
        while q <= len(hold[5][:-4]):
            try:
                if len(hold[5][q+1]) > 2:
                    WomensCanada.append(["Canada", hold[5][q], hold[5][q+1], "G", "F"])
                    q+=2
            except:
                break
        WomensCanada.append(["Canada", "Erin", "McLeod", "G", "F"])
        WomensCanada.append(["Head coach:", "Bev Priestman"])

        
        q = 1
        while q <= len(hold[6][1:]):
            try:
                if len(hold[6][q+1]) > 2:
                    WomensSweden.append(["Sweden", hold[6][q], hold[6][q+1], "S", "F"])
                    q+=2
            except:
                break
        WomensSweden.append(["Head coach:", "Peter Gerhardsson"])

        
        q = 2
        while q <= len(hold[7][2:10]):
            WomensUS.append(["United States", hold[7][q], hold[7][q+1], "B", "F"])
            q+=2
        WomensUS.append(["United States", hold[7][10], "".join(hold[7][11:13]), "B", "F"])       
        q = 13
        while q <= len(hold[7][13:])+12:
            WomensUS.append(["United States", hold[7][q], hold[7][q+1], "B", "F"])
            q+=2
        WomensUS.append(["Head coach:", "Vlatko Andonovski"])
        
        hold = []
        hold.append(["Country", "FirstName","LastName"," Medal", "Gender"])
        hold.append(MensBrazil)
        hold.append(MensSpain)
        hold.append(MensMexico)
        hold.append(WomensCanada)
        hold.append(WomensSweden)
        hold.append(WomensUS)
        return hold
MS = MensSwimScrape("https://en.wikipedia.org/wiki/Swimming_at_the_2020_Summer_Olympics")

WS = WomensSwimScrape("https://en.wikipedia.org/wiki/Swimming_at_the_2020_Summer_Olympics")

VB = VolleyballScrape("https://en.wikipedia.org/wiki/Volleyball_at_the_2020_Summer_Olympics")

WP = WaterPoloScrape("https://en.wikipedia.org/wiki/Water_polo_at_the_2020_Summer_Olympics")

S = SoccerScrape("https://en.wikipedia.org/wiki/Football_at_the_2020_Summer_Olympics")


def insert(source, sport):
    #used for player
    
    for i in source[1:]:
        
        for item in i[0:-1]:
            query1 = '''INSERT INTO Player (AthleteFirstName, AthleteLastName, Country, Gender, TeamID) VALUES
            (%(first)s, %(last)s, %(country)s, %(gender)s,(SELECT TeamID FROM Team WHERE Country = %(country)s AND SportName = %(sport)s AND
            Gender = %(gender)s));'''
            params1 = {'sport': sport, 'first': item[1], 'last': item[2], 'country': item[0], 'gender': item[4]}
            cnx = connect(user='admin', password='4242', database='TokyoOlympics')
            cursor = cnx.cursor()
            cursor.execute(query1, params1)
            cnx.commit()
            cnx.close()
      

def insertSwim(source):
    #used for competitor
    for item in source[1:]:
        
        
        #cnx = connect(user='root', password='Js#424242', database='TokyoOlympics')
        
        #q = '''SELECT AthleteFirstName, AthleteLastName, Country FROM Competitor WHERE AthleteFirstName = %(first)s
        #AND AthleteLastName = %(last)s AND Country = %(country)s;'''
        #p = {'first': item[1],'last': item[2], 'country': item[3]}
        #cursor = cnx.cursor()

        #test = cursor.execute(q, p)
        
        #cnx.close()  
        
        #if test is None:   #delete this test
            
        query1 = '''INSERT INTO Competitor (AthleteFirstName, AthleteLastName, Country, Gender, SportName) VALUES
        (%(first)s, %(last)s, %(country)s, %(gender)s, %(sport)s);'''
        params1 = {'sport': 'swim', 'first': item[1], 'last': item[2], 'country': item[3], 'gender': item[6]}
        cnx = connect(user='admin', password='4242', database='TokyoOlympics')
    
        cursor = cnx.cursor()
        cursor.execute(query1, params1)
        
        cnx.commit()
        cnx.close()

    for item in source[1:]:   
        query2 = '''INSERT INTO EventCompetition (Time, MedalWon, EventName, AthleteID) VALUES 
        (%(time)s, %(medal)s, %(event)s, (SELECT AthleteID FROM Competitor WHERE AthleteFirstName = %(first)s AND 
        AthleteLastName = %(last)s AND Country = %(country)s LIMIT 1));'''
        params2 = {'sport': 'swim', 'first': item[1], 'last': item[2], 'country': item[3], 'gender': item[6], 'time': item[4], 'event': item[0], 'medal': item[5]}
        cnx = connect(user='admin', password='4242', database='TokyoOlympics') 
        
        cursor = cnx.cursor()
        cursor.execute(query2, params2)
        cnx.commit()
        cnx.close()
        
insert(VB, "volleyball")
insert(S, "soccer")
insert(WP, "waterpolo")

insertSwim(WS)
insertSwim(MS)
