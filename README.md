# QAProjectJenkins

1. After Creating the SQL Table, app.py, backup.py & data.py files the next step is to create a Dockerfile located outside of the src/ folder all 3 .py files are located in with the code highlighted below. Whilst making sure Docker Hub is open I ran "docker build -t localhost:8083/pythonapp ." to build my docker image which is also shown below.

2. Once the image was built and we had all that we needed it was time to build the container. Using "docker run -d -p 5000:5000 -e SQL_HOST=host.docker.internal --name pythonapp localhost:8083/pythonapp", using "SQL-host=host.docker.internal" to allow the container to connect to the database I created earlier on. Using "Docker ps" will then allow me to see whether my container is running or not, which is also shown in the screenshot.

3. After establishing that I was able to restart a container using my docker image the next step was to upload this to nexus using the nexus container provided to us using localhost:8081. Once Nexus was running the first step was to create a Blob storage of type "File" and filling out the information required based on your preference. 