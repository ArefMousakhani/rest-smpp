## 1- Clone project
## 2- Create `.env` file like `.env.mk`
* `cp .env.mk .env`
* smpp configs are available in `.env` file now
## 3- Build
* `docker-compose build`
## 4- Run
* `docker-compose up`

## 5- Api Document
* Send a new message.
    ```python
     URL = '127.0.0.1:8000/send/'
     METHOD = 'POST'
     SEND_DATA_SAMPLE = {
         "phone_number": "09016242749",
         "message": "test message"
     }
     RESPONSE_DATA_SAMPLE = {
         "message": "success",
         "response": None,
         "success": True
     }
     ```
* Check connection.

   ```python  
     URL = '127.0.0.1:8000/check/'
     METHOD = 'GET'
     RESPONSE_DATA_SAMPLE = {
         "message": "success",
         "response": None,
         "success": True
     }
     ```