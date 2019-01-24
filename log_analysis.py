#!usr/bin/env/python3
import psycopg2


# Connects to the database
def connect_database(database_name="news"):
    try:
        conn = psycopg2.connect("dbname={}".format(database_name))
        cur = conn.cursor()
        return conn, cur
    except Exception:
        print("Unable to connect to database")


# Disconnects from the database
def disconnect_database(cur, conn):
    cur.close()
    conn.close()

# Query1
title1 = ("What are the most popular three articles of all time?")
# Solution for the first query
query1 = ("select title, count(*) as total from articles, log "
          "where log.path like concat('%', articles.slug, '%') "
          "and log.status like '%200%' group by "
          "title order by total desc limit 3")

# Query2
title2 = ("Who are the most popular article authors of all time?")
# Solution for the second query
query2 = ("select authors.name, count(*) as total from articles "
          "inner join authors on articles.author = authors.id inner join "
          "log on log.path like concat('%', articles.slug, '%') "
          "where log.status like '%200%' group by "
          "authors.name order by total desc")

# Query3
title3 = ("On which days did more than 1% of requests lead to errors?")
# Solution for the third query
# This query uses view named log_view
query3 = ("select error_date, error from log_view where error >1")

'''
Establishes the connection with database...
Execute the query and return the result...
'''


def execute_query(query):
    conn, cur = connect_database()
    cur.execute(query)
    result = cur.fetchall()
    disconnect_database(conn, cur)
    return result


# Print the query result to the console...
def print_result(results, f):
    for index, result in enumerate(results):
        print(str(index+1)+"."+str(result[0])+"\t\t--"+str(result[1])+" views")
    print(f)


# Print the query result for the third Query to the console
def print_error_result(results, f):
    for result in results:
        print("\t"+str(result[0])+"\t--"+str(result[1])+" % errors")
    print(f)


# Formats the title/Query(capitalizes and add styles)
def format(title):
    t = title.upper()
    top = "* *" * 22
    print("\n"+top+"\n"+t+"\n"+top+"\n")
    return top


if __name__ == '__main__':
    # Get query results
    result1 = execute_query(query1)
    result2 = execute_query(query2)
    result3 = execute_query(query3)
    # Print query results
    print_result(result1, format(title1))
    print_result(result2, format(title2))
    print_error_result(result3, format(title3))
