## TLDR: Project Achievements
  - Pulled data from government API into a mySQL database
  - Interact with mySQL database using a FLASK backend
  - Help students through the first step of the college process with data!
  
  
### Pulled data from government API into a mySQL database
I used the government's [College Scorecard API](https://collegescorecard.ed.gov/data/). Due to the pagination limit, this took some figuring out. Originally, I tried to solve this with list concatenation for each page. This was very slow and I ended up discovering pandas' dataframes which worked much better.

Once I figured out how to pull the data from the API, I then needed to store the data to make it easily accessible. In version 1, I used a csv to store the data. However after taking a databases class, I realized how flawed this approach was. I set up and hosted a mySQL database. I then wrote a series of functions to update the database directly by pulling from the API. Eventually, I will schedule a regular cron job to run these functions so that my data stays up to date.

### Interact with mySQL database using a FLASK backend
This was the first time that I used python and Flask to interface with a database. I wrote functions to convert the filters sent from the frontend into mySQL queries. I then executed those queries and processed the results before sending them back to the frontend. When I started this project, I knew very little about POST and GET requests, so I followed a tutorial and forked the original Flask infrastructure from https://github.com/ashiqks/Flask-Python. 

### Help students through the first step of the college process with data!
 In order to make the project useful to students, I created a [simple frontend](https://github.com/jack1536/simpleCollegeDataForm.git). The frontend collects information on the student's preferences and submits a post request to the backend. This post request sends a query to the database from the backend. The results are then sent back to the frontend and displayed.
 
### Future Steps
- allow data to be downloaded as a csv directly from the frontend
- Integrate data from other sources (i.e. US News, Forbes, college websites, etc.)
- Clean up frontend and add functionality
