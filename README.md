# JukeBox

##Installation on a linux device

sudo apt-get update

One shot install :

```shell
git clone git@github.com:IRISIB/JukeBox.git
cd JukeBox
virtualenv --distribute --no-site-packages ve
source ve/bin/activate
pip install -r requirements.txt
cd JukeBox
chmod +x ./manage.py
```

Run :

```shell
source ve/bin/activate 
./manage.py migrate
./manage.py runserver
```


## Contact information

Contact : dev.jukebox@gmail.com

Author : Harun Ali  
