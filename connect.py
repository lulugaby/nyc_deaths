#!/usr/bin/env python

# make sure to install these packages before running:
# pip install pandas
# pip install sodapy

import pandas as pd
from pandasql import sqldf
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
#client = Socrata("data.cityofnewyork.us/resource/jb7j-dtam.json", "J5F17tXpdVYQUtsJEjvqXn9Li")

# Example authenticated client (needed for non-public datasets):
client = Socrata("data.cityofnewyork.us",
                  "J5F17tXpdVYQUtsJEjvqXn9Li",
                 username="igabyus@gmail.com",
                  password="Web1312@1")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("jb7j-dtam", limit=2000)


# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)
pysqldf = lambda q: sqldf(q, globals())
#print(results_df)

def top_10_deaths():
    #print("top 10 causes of death ")
    causes_rank = """SELECT leading_cause, SUM(deaths) as count 
       FROM results_df
       GROUP BY leading_cause
       ORDER BY  count DESC
       LIMIT 10;"""
    death_causes_rank = pysqldf(causes_rank)
    #print(death_causes_rank)
    #print(death_causes_rank.__dict__)
    return death_causes_rank

def woman_10_death():
    print("top 10 causes of death in woman ") 
    woman_rank = """SELECT leading_cause, SUM(deaths) as count 
        FROM results_df
        WHERE sex = "Female" or sex = "F"
        GROUP BY leading_cause
        ORDER BY  count DESC
        LIMIT 10;"""
    death_woman_rank = pysqldf(woman_rank)
    #print(death_woman_rank)
    return death_woman_rank

def men_10_death():
    print("top 10 causes of death in men ")
    men_rank = """SELECT leading_cause, SUM(deaths) as count 
        FROM results_df
        WHERE sex = "Male" or sex = "M"
        GROUP BY leading_cause
        ORDER BY  count DESC
        LIMIT 10;"""
    death_men_rank = pysqldf(men_rank)
    #print(death_men_rank)
    return death_men_rank

'''
print("death count by year ")
death_year = """SELECT year, SUM(deaths) as count 
       FROM results_df
       GROUP BY year
       ORDER BY year;"""
death_year_display = pysqldf(death_year)
print(death_year_display)

print("leading death 2019")
death_2019 = """SELECT leading_cause, SUM(deaths) as count 
       FROM results_df
       where year = "2019"
       GROUP BY leading_cause
       ORDER BY count DESC
       LIMIT 10 ;"""
death_year_2019 = pysqldf(death_2019)
print(death_year_2019)


print("leading death 2014")
death_2014 = """SELECT leading_cause, SUM(deaths) as count 
       FROM results_df
       where year = "2014"
       GROUP BY leading_cause
       ORDER BY count DESC
       LIMIT 10 ;"""
death_year_2014 = pysqldf(death_2014)
print(death_year_2014)

print("leading death 2013")
death_2013 = """SELECT leading_cause, SUM(deaths) as count 
       FROM results_df
       where year = "2013"
       GROUP BY leading_cause
       ORDER BY count DESC
       LIMIT 10 ;"""
death_year_2013 = pysqldf(death_2013)
print(death_year_2013)

print("leading death 2012")
death_2012 = """SELECT leading_cause, SUM(deaths) as count 
       FROM results_df
       where year = "2012"
       GROUP BY leading_cause
       ORDER BY count DESC
       LIMIT 10 ;"""
death_year_2012 = pysqldf(death_2012)
print(death_year_2012)

print("leading death 2011")
death_2011 = """SELECT leading_cause, SUM(deaths) as count 
       FROM results_df
       where year = "2011"
       GROUP BY leading_cause
       ORDER BY count DESC
       LIMIT 10 ;"""
death_year_2011 = pysqldf(death_2011)
print(death_year_2011)

print("leading death 2010")
death_2010 = """SELECT leading_cause, SUM(deaths) as count 
       FROM results_df
       where year = "2010"
       GROUP BY leading_cause
       ORDER BY count DESC
       LIMIT 10 ;"""
death_year_2010 = pysqldf(death_2010)
print(death_year_2010)

print("leading death 2009")
death_2009 = """SELECT leading_cause, SUM(deaths) as count 
       FROM results_df
       where year = "2009"
       GROUP BY leading_cause
       ORDER BY count DESC
       LIMIT 10 ;"""
death_year_2009 = pysqldf(death_2009)
print(death_year_2009)

print("leading death 2008")
death_2008 = """SELECT leading_cause, SUM(deaths) as count 
       FROM results_df
       where year = "2008"
       GROUP BY leading_cause
       ORDER BY count DESC
       LIMIT 10 ;"""
death_year_2008 = pysqldf(death_2008)
print(death_year_2008)

print("leading death 2007")
death_2007 = """SELECT leading_cause, SUM(deaths) as count 
       FROM results_df
       where year = "2007"
       GROUP BY leading_cause
       ORDER BY count DESC
       LIMIT 10 ;"""
death_year_2007 = pysqldf(death_2007)
print(death_year_2007)


print("leading cause of death in hispanic")
death_hispanic =  """SELECT leading_cause, SUM(deaths) as count 
       FROM results_df
       WHERE race_ethnicity = "Hispanic"
       GROUP BY leading_cause
       ORDER BY count DESC
       LIMIT 10 ;"""
death_hispanic_displayed  = pysqldf(death_hispanic)
print(death_hispanic_displayed)

print("leading cause of death in Asian and Pacific Islander")
death_asian =  """SELECT leading_cause, SUM(deaths) as count 
       FROM results_df
       WHERE race_ethnicity = "Asian and Pacific Islander"
       GROUP BY leading_cause
       ORDER BY count DESC
       LIMIT 10 ;"""
death_asian_displayed  = pysqldf(death_asian)
print(death_asian_displayed)


print("leading cause of death in Black Non-hispanic")
death_black =  """SELECT leading_cause, SUM(deaths) as count 
       FROM results_df
       WHERE race_ethnicity = "Black Non-Hispanic" or race_ethnicity = "Non-Hispanic Black"
       GROUP BY leading_cause
       ORDER BY count DESC
       LIMIT 10 ;"""
death_black_displayed  = pysqldf(death_black)
print(death_black_displayed)

print("leading cause of death in White Non-hispanic")
death_white =  """SELECT leading_cause, SUM(deaths) as count 
       FROM results_df
       WHERE race_ethnicity = "White Non-Hispanic" or race_ethnicity = "Non-Hispanic White"
       GROUP BY leading_cause
       ORDER BY count DESC
       LIMIT 10 ;"""
death_white_displayed  = pysqldf(death_white)
print(death_white_displayed)

print("leading cause of death in none")
death_none =  """SELECT leading_cause, SUM(deaths) as count 
       FROM results_df
       WHERE race_ethnicity = "Other Race/ Ethnicity" or race_ethnicity = "Not Stated/Unknown"
       GROUP BY leading_cause
       ORDER BY count DESC
       LIMIT 10 ;"""
death_none_displayed  = pysqldf(death_none)
print(death_none_displayed)


print("death caused by other over years observed")
other =  """SELECT year,  SUM(deaths) as count 
       FROM results_df
       WHERE leading_cause = "(Other)" or leading_cause = "All Other Causes"
       GROUP BY year
       ORDER BY year
        ;"""
death_other  = pysqldf(other)
print(death_other)

print("death caused by cancer over years observed")
cancer =  """SELECT year, SUM(deaths) as count 
       FROM results_df
       WHERE leading_cause = "Malignant Neoplasms (Cancer: C00-C97)" 
       GROUP BY year
       ORDER BY year
        ;"""
death_cancer  = pysqldf(cancer)
print(death_cancer)

print("death caused by flu over years observed")
flu =  """SELECT year, SUM(deaths) as count 
       FROM results_df
       WHERE leading_cause = "Influenza (Flu) and Pneumonia (J09-J18)" 
       GROUP BY year
       ORDER BY year
        ;"""
death_flu  = pysqldf(flu)
print(death_flu)

print("death caused by heart disease over years observed")
heart =  """SELECT year, SUM(deaths) as count 
       FROM results_df
       WHERE leading_cause = "Diseases of Heart (I00-I09, I11, I13, I20-I51)" 
       GROUP BY year
       ORDER BY year
        ;"""
death_heart  = pysqldf(heart)
print(death_heart)

print("death caused by diabeaties over years observed")
dia =  """SELECT year, SUM(deaths) as count 
       FROM results_df
       WHERE leading_cause = "Diabetes Mellitus (E10-E14)" 
       GROUP BY year
       ORDER BY year3
        ;"""
death_dia  = pysqldf(dia)
print(death_dia)
'''
if __name__ == "__main__":
    # Creating an HTML file
    #top_10_deaths()
    #print(top_10_deaths().leading_cause)
    dic = top_10_deaths().to_dict()
    #print([v  for k,v in  dic['leading_cause'].items()])
    #print([v  for k,v in  dic['count'].items()])
    x = [v  for k,v in  dic['leading_cause'].items()]
    sx = '["' +'", "'.join(x) + '"]'
    y = [str(int(v))  for k,v in  dic['count'].items()]
    sy = '[' +', '.join(y) + ']'
    #print(dic)
    print(sx)
    print(sy)





    #string = 'hello {0} {1}'.format('test', 'bye')
    #print(string)
   
    # how to get python object to html dataframe

    output_string = '''<html lang="en"><head><meta charset="utf-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1" />

    <title>REPL</title>

    <link rel="icon" type="image/png" href="favicon.png" />
    <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
    <script defer src="https://pyscript.net/latest/pyscript.js"></script>
  </head>

  <body>
    <strong>New York City Death Stats </strong><br>
    Top 10 causes of death amongst all New Yorkers:

  


       <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.min.js"></script>
  <body>

  <canvas id="myChart" style="width:100%;max-width:1500px"></canvas>

  <script>
  var xValues = ''' 
    output_string += sx
#["bitch", "meow", "Spain", "USA", "Argentina"];
    output_string+= '''; var yValues = '''
    output_string+= sy
    #[55, 49, 44, 24, 15, 55, 49, 44, 24, 15]
    output_string +=''';
var barColors = ["red", "green","blue","orange","brown","red", "green","blue","orange","brown"];

new Chart("myChart", {
  type: "bar",
  data: {
    labels: xValues,
    datasets: [{
      backgroundColor: barColors,
      data: yValues
    }]
  },
  options: {
    legend: {display: false},
    title: {
      display: true,
      text: "Top 10 causes of death"
    }
  }
});
</script>
    
  </body>
</html>'''
    


    #print("test",x,y)
    
    Func = open("GFG-1.html","w")
    
    # Adding  to the HTML file
    Func.write(output_string)
              
    # Saving the data into the HTML file
    Func.close()
    print("done")
    
    
    


