import connexion


def foo_get(message):
    return 'You send the message: {}'.format(message), 200


if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, port=9090, specification_dir='swagger/')
    app.add_api('swagger.yaml', arguments={'title': 'Example'})
    app.run()
