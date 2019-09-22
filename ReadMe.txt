

1)command to run celery using event log 

 celery -A ThiruApp worker -l info -P eventlet


2) Command to start flower GUI 

flower -A ThiruApp --port=5050 

3) For RabitMq Montitor GUI 

http://localhost:15672/ 
username: guest
password:guest
