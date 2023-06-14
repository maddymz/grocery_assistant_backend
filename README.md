## GA (Grocery Assistant) BACKEND 

This application is a flask rest api server which conencts to chat GPT.
Currently it connects to a fine tuned chatGPT model. (will only work if your api Key of openAI has that fine tuned model, To create that fine tuned model please chcekout fine tuned models repo)

## How to run this app 
* Intalling virual Env for python
    * `python3 -m venv venv` ->  creats  an new venv
    * `python3 -m pip install --upgrade pip` -> upgrade your pip
    * `source venv/bin/activate` ->  activate it
    * `deactivate` ->  to deactive V-Env

* This app uses firebase no sql database , so better make account on firebase,Heroku, and openAI

* Download the private key and replace the firebase-private.json with your firebase key 

* You will also need to replace your openAi Api Key in chatController.py
    ```
    In chatController.py
    openai.api_key = "#Add your api key" 
    model="trained model id , we get this after fine tuning"
    ```
* Create a nltk.txt if not present and the file should mention follwing dependencies:
    ```
    wordnet
    stopwords
    punkt
    ```
* Create a .env file anandh save your aoenai key 
   ```
   OPENAI_API_KEY=<Actual key which we get from openai>
   ```

* Running the APP on local host
    * `python3 app.py`  -- to run the flask app

### How to Deploy to Heroku

* Steps to deploy
    * `curl https://cli-assets.heroku.com/install.sh | sh`  ---Installs heroku CLI
    * Create account on Heroku
    * `heroku login` Type in terminal then login to your heroku
    * Server and server files are already created 
    * Initialize your local directoty "git init" if not a git repo
    * `heroku git:remote -a <your app name on heroku>` sets the remote to a heroku repo and we push our code there to deploy  
    *  $ git add .
    * git commit -m "make it better"
    * `git push heroku main` to deploy.
    * `heroku open` in termial opens the app on heroku
    * These commands may or may not be needed
    ```
    echo "web: gunicorn app:app" > Procfile
    python3 -m pip install gunicorn==20.0.4
    python3 -m pip freeze > requirements.txt
    ```

### LOADING DATA TO ITEMS
```
run the laodData.py to laod data to you firestore DB

make sure you ahve replace the firebase-private.json key first
```