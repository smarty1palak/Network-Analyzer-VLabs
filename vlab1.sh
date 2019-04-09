python test.py
read -r line < segmented1.txt
echo "${line}"
locust -f locustfile1 --host=$line