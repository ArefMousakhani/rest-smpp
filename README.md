## 1- Clone project


## 2- Create `.env` file like `.env.mk`
* `cp .env.mk .env`
* smpp configs are available in `.env` file now


## 3- Build
* `docker-compose build`
* if do not want to use docker compose:
    * `docker build . -t rest-smpp`
    
    
## 4- Run
* `docker-compose up`
* if do not want to run with docker compose:
    *  `docker run -e SMPP_HOST=mscsim.melroselabs.com -e SMPP_PORT=2775 -e SMPP_SYSTEM_ID=887490 -e SMPP_PASSWORD=YQPMQGd -e SMPP_SOURCE_ADDRESS=00887490 -e KAVENEGAR_KEY=XXXX -p 8000:8000 rest-smpp`
    
    *  `docker run --env-file .env -p 8000:8000 rest-smpp`
    
    
## 5- Api Document
* Send a new message.
    ```python
     URL = '127.0.0.1:8000/send/'
     METHOD = 'POST'
     SEND_DATA_SAMPLE = {
         "phone_number": "09xxxxxxxxx",
         "message": "test message",
         "method": "smpp" # smpp, ht
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