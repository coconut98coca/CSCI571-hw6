## hw6

# ativate virtual environment on Windows: 
```Shell
env/Scripts/activate
```

# Run code:
```Shell
python main.py
```

# deploy on Google Cloud Platform
Need to change backend_url (in base.html) from "http://127.0.0.1:8080/search?" to "https://myfirstpython-9901.wl.r.appspot.com/search?"
```Shell
gcloud app deploy
```
# To browse
```Shell
gcloud app browse
```

# exit the virtual environment
```Shell
deactivate
```