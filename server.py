from factory import create_app
from factory.extensions import db

if __name__ == "__main__":
    app = create_app()

    # Create db tables if they don't exist
    with app.app_context():
        import factory.blueprints.auth.model

        db.create_all()

    app.run(host="localhost", port=5001, debug=True)
