# Flask API Template

1. Create the environment
```
$ python -m venv venv
```
  - retart the terminal to jump into the environment

2. Create some files and folders
  - main.py
  - app (folder)
    - everything will live in this folder for the app
  
3. Set up the following:
  - README
  - GIT
  - .flaskenv
  - .env

4. inside the app folder create the following:
  - __init__.py
  - routes.py

5. Install Flask

6. run the following command:

```
$ pip freeze > requirements.txt
```

7. put the following in the __init__ file in app
```
from flask import Flask

app = Flask(__name__)

from app import routes
```

8. set up a .vscode folder with settings.json to correct formatting. (autoformatter will want every import at the top but with this flask it needs to be at the bottom)
```json
{
  "editor.formatOnSave": false,
    "[python]": {
    "editor.tabSize": 4
  },
}
```

9. Open routes folder and put following
```
from app import app
```

10. After doing so you are able to create the routes in this file

11. go to main and 
```
from app import app
```

12. in your .flaskenv file put the following:
```
FLASK_APP=main.py
```

13. Run the following command in the terminal
```
$ flask run
```

