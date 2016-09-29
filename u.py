import runserver
port = 8080
step_size = 18
location = "50.8728857,4.6904617"
s = ''
command = "python PokemonGo-Map/runserver.py -os -l {} -k AIzaSyBt2WoOORAfgOKhf3NW-PBzYg94M9vLdVY -H 0.0.0.0 -P {} --db-type=mysql --db-host=127.0.0.1 --db-name=pokemongomapdb --db-user=root --db-pass=plopkoekgo".format(location, port)

print(command)

subprocess.call(command, shell=True)
