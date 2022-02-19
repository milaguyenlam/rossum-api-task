# rossum-api-task
Flask application for annotation export and its conversion (Rossum platform)

## Quick overview
- Simple flask app aiming to export annotations by communicating with Rossum API, converting it's xml response, sending it to my-little-endpoint.ok/rossum and finally returning a json response telling if the whole pipeline was successful.

### API
- GET /export/\<queue-id\>/\<annotation-id\> (with Authorization: Basic <hash>)
  - returns json response: {"success": Boolean}
  
### Environment variables
- Environment variables should be defined in .env file (located in the root folder of the project)
- "DEFAULT_USERNAME" - username that's going to be authorized by the flask app
- "DEFAULT_PASSWORD" - password that's going to be authorized by the flask app
- "ROSSUM_API_USERNAME" - username for the Rossum platform 
- "ROSSUM_API_PASSWORD" - password for the Rossum platform
### Project structure

- ./api - folder that contains all the routes/end points of the application. These routes/end points only for accept the request. The logic of this routes/end points are implemented in a different folder.
- ./services - where all the logic of routes/end points are implemented
- ./utils - this is the folder that we are going to add our other functions and classes such as auth, xml parsing and so on.
- ./tests - folder containing test files (tests run by pytest module)
- ./xml_resources - folder containing .xslt files (xml transformation) and .xsd files (xml schema for validation purposes)
- config.py - file containing flask configuration and environment variables data
- app.py - flask entrypoint file
- Dockerfile - file that defines the container's build procedure (Note that: if you want to run tests as a part of build pipeline, you shall uncomment the line containing "RUN pytest tests")
- requirements.txt - file defining all python dependencies of this project