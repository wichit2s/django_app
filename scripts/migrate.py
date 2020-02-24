from subprocess import call

commands = [
  'python manage.py makemigrations core',
  'python manage.py makemigrations',
  'python manage.py migrate core',
  'python manage.py migrate'
]

if __name__ == '__main__':
    for command in commands:
        print(f'running {command}')
        try:
            call(command.split())
        except:
            pass#print(e)
