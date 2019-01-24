# Log_Analysis

### Overview
>In this project, we have to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

This project provides the solution for the following three queries:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

[Top](#top)

### Prerequisites
* [Python](https://www.python.org/downloads/)
* [Vagrant](https://www.vagrantup.com/downloads.html)
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
* [PostgreSQL](https://www.postgresql.org/docs/9.5/index.html)

															[Top](#top)

### Steps to Run the Project 
1. Download and install Python from the link provided in the section of prerequisites.
2. Download and install Vagrant and VirtualBox from the links provided in the section of prerequisites.
3. Navigate to the vagrant folder in your bash interface/cmder/command prompt.
4. Launch the Virtual Machine using the following command:
	
	```
	vagrant up
	```
   This command creates and configures guest machines according to your Vagrantfile.
5. After that continue with the following command:
	
	```
	vagrant ssh
	```
   This will SSH into a running Vagrant machine and give you access to a shell.
6. The command line will start with vagrant now, then change the directory to the vagrant.
7. If not psycopg2 is already installed, download and install it in vagrant using the following command:
	
	```
	pip install python-psycopg2
	```
8. Download the repository of [Log Analysis]() project and unzip it into the vagrant folder.
9. Download the [data here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and unzip it into the vagrant folder.
10. To load the data:
	
	```
	psql -d news -f newsdata.sql
	```
11. To run the database:
	
	```
	psql -d news
	```

The database includes three tables
1. The `authors` table includes authors of articles.
2. The `articles` table includes the articles.
3. The `log` table includes the entry for each time a user has accessed it.

#### Creating View
Create a view named log_view which would be useful for the third query.

```sql
create or replace view log_view as select date(time) as error_date,round(100.0*sum(case log.status when '404 NOT FOUND' then 1 else 0 end)/count(log.status), 2) as error from log group by error_date
 ```

 After creating the view, finally run the source code:
 
 ```
 python log_analysis.py
 ```

															[Top](#top)

### Output

```
WHAT ARE THE MOST POPULAR THREE ARTICLES OF ALL TIME?             

1.Candidate is jerk, alleges rival      -- 338647 views            
2.Bears love berries, alleges bear      -- 253801 views            
3.Bad things gone, say good people      -- 170098 views            
                                                                  
                                                                  
WHO ARE THE MOST POPULAR ARTICLE AUTHORS OF ALL TIME?             

1.Ursula La Multa       	-- 507594 views                            
2.Rudolf von Treppenwitz        -- 423457 views                    
3.Anonymous Contributor 	-- 170098 views                            
4.Markoff Chaney        	-- 84557 views                             
                                                                  
                                                                  
ON WHICH DAYS DID MORE THAN 1% OF REQUESTS LEAD TO ERRORS?        

	2016-07-17    --2.26% errors

```

															[Top](#top)

#### FAQ's [here](https://udacity.zendesk.com/hc/en-us)

															[Top](#top)
