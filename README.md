#Downloading source code

appcfg.py download_app -A \<your_app_id\> -V \<your_app_version\> <output-dir>

#Deploy

appcfg.py update <name>

<name> = where app.yaml is 

Note: Use version number with -V

#Run

dev_appserver.py <name>

(just use . when in direcotry)
