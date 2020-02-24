from subprocess import call

commands = [

'python manage.py loaddata members.json',

]

if __name__ == '__main__':
    for command in commands:
        print(f'running {command}')
        try:
            call(command.split())
        except:
            pass#print(e)
