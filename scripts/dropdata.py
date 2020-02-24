import shutil

if __name__ == '__main__':
    items = [
                'db.sqlite3',
                'core/migrations',
                'api/migrations',
                'core/__pycache__',
                'mysite/__pycache__',
                'api/__pycache__',
       ]
    for item in items:
        print(f'removing {item}')
        try:
            shutil.rmtree(item)
        except FileNotFoundError as e:
            pass#print(e)
