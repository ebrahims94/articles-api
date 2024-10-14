## Articles API

This is a Django project that implements a simple API for managing Articles for users connected with local postgres database run on Docker and docker compose.

## Solution Description

Here goes the description how I created the app and worked on it:

- I added the Article model based on provided data and I added the image field as a url indecating that we save the images into assets or S3 buckets as an example.
- I implemented serializers get all data and define the read only fields.
- I implemented the APIs and it was a `ListCreateAPIView` for listing and creating articles `RetrieveUpdateDestroyAPIView` for update and delete actions from django.
- I added the authentication to protect the API calls except the login.
- I implemented the tests for all functioanlity at the end.
- Wrote some docuemtation and learnings as well.

I used some packages while implementing this app:

- `PyJWT`, `djangorestframework-simplejwt` for authentication and authorization.
- `psycopg2` to deal with postgres database.

## Run the Project

To run the project locally, follow these steps:

1. Extract the compress file.
2. `cd` to the extracted directory and run `docker compose up --build`
3. Docker will take care of everything and the application will run verysoon.
4. In the `start.sh` file we got all the necessary commands to make the app run and do migrations for DB.
5. App is up and running now and you can use APIs or Django admin even though to check `articles`.
6. You need to create a superuser to be able to access authenticated APIs so run this command `docker exec -it articles_api-backend-1 bash` or change the container name to the created name - hence check `docker ps`.
7. You are now inside docker so now create super user bu running `python manage.py createsuperuser` and fill all details required.
8. Now you are all set and you can login to Django admin.
9. In terms of use API calls you need to be authenticated so you need to authenticate using `login/` API call with the created user.
   ```bash
   curl --location 'localhost:8000/login/' \
       --form 'username="<username>>"' \
       --form 'password="<password>"'
   ```
10. Output should be 2 tokens and looks like this:
    ```json
    {
      "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMzIxMzQ0MCwiaWF0IjoxNzEzMTI3MDQwLCJqdGkiOiI4NDA4N2Y2YTMzOWE0NjI5OGVhMjBhYzAxOTJlMzM4MiIsInVzZXJfaWQiOjF9.O8JnYjd7M9XSvl2QwW6C-PKKapOhifTQcZ2VL_HrX_g",
      "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEzMTI3MzQwLCJpYXQiOjE3MTMxMjcwNDAsImp0aSI6ImNiYTUwMTQ1MDlmNzRiODI5NjA4N2M4MzMzZGRhYWZjIiwidXNlcl9pZCI6MX0.7qbpzoD7D9X73ZUrjhXGFCqAeLwwHODcjXfBna_sxdM"
    }
    ```
    the `access` token is valid for 1 day and the `refresh` token is valid for 7 days
11. Now you can use the `access` token to call APIs but if it didn't work you can generate a new one using the `refresh` token by running:
    ```bash
    curl --location 'localhost:8000/refresh/' \
        --form 'refresh="<refresh token>"'
    ```
12. Now you got the access token again in case it got expired and should the output looks like this:
    ```json
    {
      "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEzMTM0NjA0LCJpYXQiOjE3MTMxMjcwNDAsImp0aSI6IjA4MTA1ODZmMDUwYzQyYzdiNDk5MjdiYWU0MjY1YjA1IiwidXNlcl9pZCI6MX0.jFDKptf03x_7WMI9qtdfDP84uzven7RvZlN0Zs7wpqc"
    }
    ```
13. Now you can use the access to call APIs eg:
    ```bash
        curl --location 'localhost:8000/api/v1/articles/2' \
        --header 'Authorization: Bearer <access token>'
    ```
14. Now all set and good to go!

## Imrovements

    In general this task is a first draft and didn't take long time, so many improvments possible here and I might not mention all of them.

- Improve testing from 3 points (coverage, structure and setup) where we can creat `fixtures` and auto seed for DB, better structure for test files and increase test coverage for sure.
- Add more documentation.
  and maybe more.
