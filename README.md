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
chmod +x ./manage.py
```

Run :

```shell
source ve/bin/activate # Do only once (if it's a new tty)
./manage.py runserver
```


## Contact information

Contact : dev.jukebox@gmail.com
