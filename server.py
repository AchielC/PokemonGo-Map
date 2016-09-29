import subprocess

subprocess.call("python runserver.py -fl -nsc -l Leuven -H 0.0.0.0 -P 5000 -k AIzaSyBt2WoOORAfgOKhf3NW-PBzYg94M9vLdVY --db-type=mysql --db-host=127.0.0.1 --db-name=pokemongomapdb --db-user=root --db-pass=plopkoekgo -os --db-max_connections=5000", shell=True)
