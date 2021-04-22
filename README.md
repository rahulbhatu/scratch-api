# Scratch API Test
This repository contains the code for API and Local setup. It contains the
API code written in python. API code is build with endpoints from the swagger specifications.
As per specifications this API code will work across various systems (Unix- and Windows-based) and the CSV file provided as test is being autopopulated in the DB.


# Test the code
**Prerequisite** : To the test the code on any system you will have to install the
docker and docker-compose tool on the system.

API development tool like Postman to test the endpoints.


Clone this repo and from the root of the repository run below command
`docker-compose up -d`
This will create two conatiners one app and other db
if you can see two containers on execution of executing `docker ps` then
we can now test the API code.

Below are the example endpoints that can be used
### get all users
curl --location --request GET 'http://localhost:5001/api/v1/users' \
--data-raw ''
### get specific user details with ID.
curl --location --request GET 'http://localhost:5001/api/v1/users/3' \
--data-raw ''
### Create user
curl --location --request POST 'http://localhost:5001/api/v1/users' \
--header 'Content-Type: application/json' \
--data-raw ' {
        "id": 6,
        "name": "rahul"
}'

Make sure the ID sent in the user creation is unique and if this is being tested on
server publicly accessible than localhost can be replaced by public IP


