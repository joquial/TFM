# Project Documentation


## Index
1.  Introduction
2. Docker
3.  Git
4. Python site
     * Skulpt 
     * JavaScript Functions
     * Node.js
     * Ajax 
5. Future Improvements

## Introduction
Through this project, we are trying to improve the Node-Red environment by creating a new web site directly connected with it, that allows users to write their python code, load files that they have already created, check that their code works as it should by using an interactive screen, a debugger or running directly their code and showing its output, and last but not least, letting them save the code and import it directly to Node-Red. Once, the implementation is achieved a new platform that enables companies to easily create new IoT systems will be provided just as the bIoTope project, funded by the European Union, lays its foundations.

To accomplish this, different technologies are being used. First, Docker and its technology based in containers provides the perfect environment to develop, run and deploy our applications. Git commands are used constantly to commit and push every significant change in our project, allowing us to save and control the state of the project. The Python site represents an implementation of skulpt but adding new features with new javascript functions, node.js files and ajax interactions between the client and the server side.
## Docker
Docker containers allow us to create and run our application by just installing the needed libraries and assuring the perfect performance in any environment.
The first step to understand how docker containers work is understanding how they create what they call images through the Dockerfile. In our project we have created one different Dockerfile for each application we want to run ( Node-Red, Web or the Node.js files). To effectively create the images, these Dockerfiles contain basically the following commands:

-  FROM= Search in another docker directory for information.
-  WORKDIR= Defines the docker directory where you want to work in.
-  COPY= Copies one of all of the files (using *) that appears in your Dockerfile directory into the docker directory that you define or by default your working directory.
-  RUN= Represents for docker the same functionality that executing one line from the command line.
-  EXPOSE= Opens a new port in the system.
-  CMD= Executes a file or program.

Now we understand the commands and we create a Dockerfile, we need to build the image; to achieve this we have to go to the directory of our Dockerfile in our terminal and use the next command:

```
 sudo docker build -t imagename .
```
  
(where imagename is the name you want to choose, dont forget that last point) 

The next step, once the image is build is to create the container by running the image, this can be done using :

```
sudo docker run -p portlocalhost:portexpose imagename
```

Following the previous steps you can run one of your applications. To run all of our applications as a service we need to create a docker-compose.yml in a parent directory of the dockerfiles. In the docker-compose is really important the structure and how the spaces are used, we use the following commands to create our docker-compose:

* version: Defines the version, in our case is number '3'
* services: We define the name of the services that we want to create.
       *  servicename: We define how is going to work
                    - image: name of the image that we have previously build.
                    - port: - "portlocalhost:portexpose"
                    - volumes: directory where we are going to save things.
                    
  (In our project, volumes have a vital importance to achieve that the new files created in our python site are accesible to Node Red) 
  
In order to make it run we just have to go to the directory of our docker-compose and run:

```
sudo docker swarm init
sudo docker stack deploy -c docker-compose.yml namecompose 
```
  (where namecompose is the name that you want to choose).
  
  Other useful commands that we can use in our terminal are:
  
```
- sudo docker container ls (checks wich containers are running)
- sudo docker container stop idcontainer (stops the execution of one container)
- sudo docker exec -it idcontainer /bin/sh (lets you enter in the docker directory without stopping the container)
- sudo docker swarm leave --force (stops de swarm and all the containers that were running on it)
- sudo docker-compose up (you need to install docker-compose to use this command, it allows to run your service but also seeing what is happening in each application.
- sudo docker-compose down (you need to install docker-compose to use this command, it stops the service that has been run by docker-compose up
```
In order to gain speed and improve our experience using this docker commands, we have created one python file located in the directory TFM/modules called commands.py with some shortcuts and automated functions that may be run as follows:

```
- python -c 'from commands import run; run()' (initializes the swarm and run our service)
- python -c 'from commands import stopall; stopall()' (to leave the swarm and stop all the containers)
- python -c 'from commands import stop; stop("x")' (stop a container)
- python -c 'from commands import modi; modi("x")' (builds automatically one image and makes it run)
```
  Where x refers to the name of the image we want to work with, in our case firstimage (web), nodeimage (nodesjs), node-red (Node RED), o-mi-node (dataLyon), mongo (mongodb).
## Git
Git provides the perfect way to save and control the state of our project. Every significant change is commited and pushed on GitHub, in that way we can ensure that even if we make a mistake or our computer do not respond, we can acces our code with any other device with internet access.
These are the most common used commands using git:

```
- git init (initializes a git repository)
- git add * ( adds all your files of the current directory to the git)
- git commit -m "name of the commit" ( saves all the changes of your files)
- git push origin master (pushes to github the changes that you have previously commit)
```

Other important git commands that we have not yet used but that may be useful in the future are:

```
* git branch branchname (create a new branch to follow developing the project but separated of the origin project)
* git merge otherbrachname (merges the different branches into one)
```
## Python Site
As we said our python site is a  representation of skulpt with new features added in order to improve the user experience and to integrate it with the Node Red environment.
### Skulpt
Skulpt developers did a fantastic job and create a wonderful tool to write and run python code in the browser, which is not easy because it means a full translation between python and javascript languages.
 
We took advantage of this opportunity but trying to adapt the  web better to our neeeds:

* Changing a little bit the interface by reorganazing the screens in columns
* Cleaning some code that was not really useful to us
* Letting the output screen to show also the errors that appeared when the code is executed
* Adding a new iframe that allows users to search for more information
* Removing the previous output when the code is newly executed.
* Creating new buttons and functions to gain new functionalities.

### Javascript Functions
We have created different buttons to get new functionalities in our site. For example using the button Initial Page of the iframe, the user can go directly to the google search from wherever he might have gone.
However, there are two functions that deserve to be studied with more detail. These are the ones related with the inputs and buttons of **"Save text to File"** and **"Load"**.

#### Save Text to File
When you press this botton, the next steps are processed internally:

First, the text that is written in the editor  screen is read using **editor.getValue()**. The text that is written in the input box is also read using **document.getElementById(id)**. Then two separate processes start simultaneously.

One of them, just initializes a download with the name of the input box and with the code that was written in the editor screen. This is okay because we can get the text in a file in the downloads directory, however it is nos accesible for Node-Red.

The second and most important one, sends the data to one url that we have specified, being  data.body.filename the text written in the input box and data.body.content the text of the editor screen. 

#### Load
The Load button runs a javascript function that basically removes the text that was written in the editor screen, reads the input box and sends its contents to the url that we have specified. After that it stays listening to the url to see if it receives something.

If it does, it directly writes in the editor screen the contents that it has received using **editor.setValue(contents)**.

### Node.js
Until now we have explained, one part of the process but, how do we save the text that we are sending to the url in a file that would be always accesible for Node Red? or, what are the contents that we receive when we press the load function?

The answer of this questions has its origin in the Node.js technology (this technology allows us to work from the server side) and may be found in the files that we have created named **storage.js** and **load.js**.

#### Storage.js
When this node is executed, it starts listening to one defined port, in our case to the url where we were sending the data when we press the "Save to Text" button. Then the data is received, however it comes as an object and with different problems that must be treated.

For this reason we use first **JSON.stringify(request.body)** to get the right format. After that, we proceed with the treatment, we use **text.indexOf**, **text.lastIndexOf** and **text.substring** to get  just the part of the code that we want to use both for the filename and for the contents.

We also had a problem with the break lines that appears in the code as \n and with the " that appears as \ " ; to solve both problems we use  **text.split()**. After that, a simple for function is created to unite in the proper way the differents arrays.

The last part of our node is when we actually create a document in the rigth location, with the title defined in the input box, the content of the editor screen and the .py format that allows Node Red to read it. We achieve all of this just using **fs.writeFile(location + title +'.py', contents, function (err)...**
#### Load.js
The Load.js node is pretty similar to the storage.js. First, it is listening to the port that is defined in the load function, it receives only the content of the input box, which facilitate us the treatment of the text.

After that, we use **fs.readFile(location + title + ".py", 'utf8', function(err, contents)...**  with this function we read the contents of the file stored in the location that we have defined.

The last step is sending back this contents to the javascript function, which can be achieve using **response.send (contents)**.
### Ajax
As you may have intuited, the interaction between the javascript functions and the nodes.js is achieved thanks to the Ajax technology. This technology may be difficult to implement but at the end is the best way to communicate the client and the server side. For example, in applications as ours that need not only sending data but also receiving a response, it is possible to use a "POST" connection.

In our case, we succesfully established the connection using these commands in the javascript function.

```
app.use(myParser.urlencoded({extended : true}));
jQuery.ajax({
		       type: 'POST',
		       data: datas,
               crossDomain:true,
                       url: 'http://localhost:8090/',						
                      success: function(result) {
                      console.log('Data'+result);    
                      var contents= result;
                      editor.setValue(contents);
                            }
                });
```
And these command on the Node.js files:

          app.use(function(req, res, next) {
          res.setHeader('Access-Control-Allow-Origin', '*');
          res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
          res.setHeader('Access-Control-Allow-Headers', "Origin, X-Requested-With, Content-Type, Accept");
          res.setHeader('Access-Control-Allow-Credentials', true);
          next();
          });
          app.post('/', function(request, response) {
          .
          .
          });

          
## Future Improvements
Fine, we have finally created a nice website that allows us to write python code in the browser, execute it, save it and integrate it with the Node Red environment. But, are we actually finished? The answer to this question is clearly no, we have not finished at all. 

There is no doubt that Skulpt is an amazing tool, however it stil has some limitations; one of them that is particularly relevant for our project is that there are a lot of libraries and modules that are not yet implemented. 

As you may know, Node Red is a visual programming tool, really used in the industry to connect smart objects and get more information of them. For this reason, it is really interesting the possibility of using python libraries to easily obtain more valuable information of the things. These option already exists but cannot be really tested in our site yet.

Skulpt developers are actually working on that direction but we should also contribute in some way to the cause.
