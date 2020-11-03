## Project Achievements

  - Learn how to build a restful Flask backend
  - Learn how to pull data from API's
  - Learn how to filter and clean data using pandas
  - Help students through the first step of the college process with data!
  
### Build a restful Flask backend
  
  Rather than start from scratch, I forked a simple, working flask backend from https://github.com/ashiqks/Flask-Python. I then used this as a template for how to make POST and GET requests. The POST request is the fundamental request that the frontend makes in order to trigger the backend to filter the data and send it to the user
  
### Learn how to pull data from API's
  I used the government's [College Scorecard API](https://collegescorecard.ed.gov/data/). While I originally used lists, I found that the 100 items per page limit was making list concatenation very slow. Pandas' dataframes were a natural solution. As of now, the only way to update the data is by manually running the step_1.py file, but in the future this could be done with a scheduled cron job, or the whole process could store the data in a database rather than in the plk file.
  
### Learn how to filter and clean data using pandas
  Using the [College Scorecard Data Dictionary](https://collegescorecard.ed.gov/assets/CollegeScorecardDataDictionary.xlsx) I converted the numerical categories into something a human could more easily interpret. I then filtered the data based on preferences from the POST request. Once filtered, the data is simply converted to csv.
  
### Help students through the first step of the college process with data!
  In order to make the project useful to students, I created a [simple frontend](https://github.com/jack1536/simpleCollegeDataForm.git). The frontend collects information on the student's preferences and submits a post request to the backend. This post request causes the data to be filtered and triggers an email to be sent to the inputted email address with the actual data. Emailing the data seemed like a good solution to the annoyance of waiting for the download.
  
  
### Future Steps
  - export the data to an excel workbook with multiple sheets and better formatting to make it easier for users to interpret the data
  - set up a database to store information about user requests in order to possibly do some sort of future data science project on the usage of the tool
  - Regularly schedule pulls from the API so that it is always using the most recent data
  - integrate data from other sources (i.e. US News, Forbes, college websites, etc.)
