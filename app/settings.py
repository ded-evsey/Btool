settings = {
    'db': {
        'name': 'btool',
        'username': 'btool',
        'password': 'btool',
        'type': 'postgres',
        'port': 'postrgesql',
        'address': 'localhost',
    }
}

conf = {
    'SQLALCHEMY_DATABASE_URI': '{}://{}:{}@{}:{}/{}'.format(
        settings['db']['type'],
        settings['db']['username'],
        settings['db']['password'],
        settings['db']['address'],
        settings['db']['port'],
        settings['db']['name']
    )
}
