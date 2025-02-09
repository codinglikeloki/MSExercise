All testing was run on Linux. As I'm not aiming to anything perfect here - running over some other system will most likely need some fixing.

There is 3 different services under this project. You need to create .env file in running directories of all these scripts.
1. MSEServer.py
This will listen to measurements and write them to "db". Also the interface is just listening HTTP get. Values are just passed as part of url. 
Create .env file with content:
```
PORT=8616
DEBUG=False
```

Port is port you want to run the service. Debug turns on and off debuging.

2. MSEEmitter.py
that will send measures for service above.
Create .env file with content:
```
ADDRESS=http://127.0.0.1:8616
DEBUG=False
MYNAME=<Any valid UUID>
```

Address is the URL where you run the MSEServer. Remember to put the protocol and and port.
Debug is not used, but I don't remember if it's still read and im too tired to check so just put it there. Or find out if it is needed.

3. MSEAnalyser.py
that will implement some "analysis" on "db" measures.
Create .env file with content:
```
DIRECTORYOFDB=/home/username/repo
DEBUG=False
```

Directory of db is 2 things. It's the location where MSEServer is running. As db.txt created there is pretending to be a data storage solution. It's also a stark reminder to not to use too generic variable names like PATH or one will get embarrassed.
