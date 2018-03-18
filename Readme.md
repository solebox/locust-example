# locust load testing example 
woot woot

# hello.py 
a sample flask server to make life easier when first running the test so you can play with it

# running locust with a locustfile and a web interface
locust -f locustfile.py
locust -f locustfile.py --host="http://localhost:5000"

# running locust with a locustfile and without web interface
## --csv will output all statistics to csv files with the statistics prefix
locust -f locustfile.py --no-web -c 10 -r 10 --csv=statistics
