# QAProjectJenkins

Objective:

Use Jenkins and Nexus to automate a CI pipline for the backup app built in project 1. It should be able to push new changes to the repository when changes are made to the source code.

Risk Assessment:

1. Source code not working would lead to the application not working correctly.

2. Making sure the Jenkins container runs without any errors or the purpose of a CI/CD Pipeline would not work.

3. Nexus Container not running would cause the project to not have a central repo connecting all parts of it.

4. If docker stops working I won't be able to build and deploy the image into a container.

5. Pushing sensitive information to my git repository as this could be a security risk as anybody could access the database.

PLANNING STAGE:

During the planning stage I created a Trello page which created an environment for me where I could track my work. I set up the board highlighting all the steps I would need to take to start the project and to understand the definition of the project being completed. This started with getting a repo set up and having my SQL database fully set up before going into building an image. Once I created this I made sure to mark it on my Trello board and move onto the next step. Following from this I made sure to understand how nexus, docker & jenkins works and which application to start of with. Once I built the docker image and started the container I made sure that the application works by testing the localhost:5000/log to see if this output the page I've set in my @app.rout('/log') within my app.py file. 

![TrelloBoard](https://github.com/netxrunna/project1/assets/103886193/b6063870-f915-46bb-91b3-4acc53b74421)

Understading that this process was completed and successful, I understood that the next step would be to set up nexus so it is ready to connect to my docker container. Once this was completed the final step was to understand jenkins and what requirements I needed to automate this process for me.

STEPS TO RECREATE:

1. First I needed to make sure that docker desktop was setup correctly to allow inseucre registries by adding the local hosts into the docker desktop config as seen in the first screenshot below. After Creating the SQL Table, app.py, backup.py & data.py files the next step is to create a Dockerfile located outside of the src/ folder all 3 .py files are located in with the code highlighted below. Whilst making sure Docker Hub is open I ran "docker build -t localhost:8083/pythonapp ." to build my docker image which is also shown below.

![DockerDesktop_Config](https://github.com/netxrunna/project1/assets/103886193/0bae20bb-337b-4f05-b9f7-f9fd64ef82ef)

![FCA_Database](https://github.com/netxrunna/project1/assets/103886193/168bba70-d362-4ecf-8e67-e4a10f16daa7)

![Dock run](https://github.com/netxrunna/project1/assets/103886193/0010b2c8-1dc2-4ad0-9cdf-c84a1a3a3067)

![Docker_Image_Ls](https://github.com/netxrunna/project1/assets/103886193/5884f37e-754c-44a5-ac44-517f050fb7d0)

2. Once the image was built and we had all that we needed it was time to build the container. Using "docker run -d -p 5000:5000 -e SQL_HOST=host.docker.internal --name pythonapp localhost:8083/pythonapp", using "SQL-host=host.docker.internal" to allow the container to connect to the database I created earlier on. Using "Docker ps" will then allow me to see whether my container is running or not, which is also shown in the screenshot.
![Docker_PS](https://github.com/netxrunna/project1/assets/103886193/0f4b61ad-ea54-46ee-a753-8b405cee0018)

![log](https://github.com/netxrunna/project1/assets/103886193/3357e01f-4237-45d3-aaf0-f65d8e112750)


3. After establishing that I was able to restart a container using my docker image the next step was to upload this to nexus using the nexus container provided to us using localhost:8081. Once Nexus was running the first step was to create a Blob storage of type "File" and filling out the information required based on your preference. Following on from the previous step I added "Docker Bearer Token" which is an access token for anonymous pulls. Furthermore, the next step would be creating a repository of type "Docker (hosted)" filling out the required fields. 

![Nexus_Blobl](https://github.com/netxrunna/project1/assets/103886193/f19b2106-1574-4b58-a9f1-5bca9febbf8f)

![Nexus_Realm](https://github.com/netxrunna/project1/assets/103886193/e00d30cf-c82a-4c04-bebe-957a1d81732e)

![Nexus_Repo](https://github.com/netxrunna/project1/assets/103886193/ab3c18de-ee59-4791-b7b0-970ac31077b0)

4. The next step and the final step included setting up 'Jenkins', for this we were required to use the "wsl" command in a fresh command line to activate Ubuntu within the command line. With the bash script provided to us we were able to install Jenkins on the VM which would then allow us to set up the required pipeline needed. Once Jenkins was all set up I created a brand new pipeline with the type of "Pipeline". The config as shown in the image highlights that I picked Pipeline script from SCM(Source Code Management) under definition, this allowed me to include my git repo after picking git as an SCM. This would allow Jenkins to understand where the necessary files are during the pipeline process. Creating a Jenkinsfile allowed me to include all the stages and commands I wanted Jenkins to use when running the pipeline. Using the correct syntax & instructions (As shown below) would allow Jenkins to Build the docker image, start container & log in to nexus to upload the container. I've also added scripts to stop the container and restart the container to allow me to make changes without breaking the pipeline.

![Jenkins_Dependancies_Install](https://github.com/netxrunna/project1/assets/103886193/9f310304-fbe0-4600-8fc5-5fbfb2200fa7)

![Pipeline_Config](https://github.com/netxrunna/project1/assets/103886193/19d8d64c-6761-4a3a-b1cd-db773de94878)

![JenkinsCode](https://github.com/netxrunna/project1/assets/103886193/c0547950-3df4-4b32-ac1e-926785abeb4b)

![Jenkins_ConsoleOutput](https://github.com/netxrunna/project1/assets/103886193/c93e9669-6ca5-4bf1-86e0-b55c1cdfdf62)

![Jenkins_Pipeline_Success](https://github.com/netxrunna/project1/assets/103886193/d00affb3-5663-4643-a6cd-ebeebaaf9c60)

![Dockerhub_Application_Log](https://github.com/netxrunna/project1/assets/103886193/5769997d-48c8-4228-8c87-20a0bcecc441)
