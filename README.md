# Flask Auth

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/narcisolobo/auth.svg)](https://github.com/narcisolobo/auth/stargazers)
[![GitHub Issues](https://img.shields.io/github/issues/narcisolobo/auth.svg)](https://github.com/narcisolobo/auth/issues)
[![GitHub Forks](https://img.shields.io/github/forks/narcisolobo/auth.svg)](https://github.com/narcisolobo/auth/network)

I made this project to learn how to implement a few auth-related Flask plugins. This app uses the app factory pattern with blueprints and the following plugins: Flask-Bcrypt, Flask-Login, Flask-Migrate, Flask-SQLAlchemy, and Flask-WTForms.

## Table of Contents

- [Flask Auth](#flask-auth)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)

## Introduction

Flask was the first web framework that I learned back in 2018. I did not attempt to implement any popular Flask plugins at the time, mostly because I didn't know they existed. After learning basic Flask concepts, I quickly moved to Django.

Django is amazing, but it does a lot of things for you. In order to gain a better understanding of auth flow, I decided to go back to Flask and implement a DYI auth flow using only Flask, raw SQL, and Flask-Bcrypt. After getting a good handle on all of that, I wanted an ORM, an easier way to track user authentication, and hassle-free form validation.

That brings me to Flask Auth. With this project, I have hit all the goals I set out before me. I'm confident in what I have implemented, and I'm glad to have learned how to crawl before running.

Moving forward, I'll add another model to learn how to implement a one-to-many relationship with Flask-SQLAlchemy.

## Features

List the key features of your project. For example:

- User Registration: Users can fill out a WTForm to register. If the form is valid, their raw password is hashed using Flask-Bcrypt, and a new user is created and saved to the database.
- User Login: Users can fill out a form to log into the site. If the form is valid, the app searches for the user via their email address. If the user is found, the app then checks their password against the hashed password in the database. If all is well, a session is created and the user is added to it. Finally, the user is redirected to the dashboard.
- Protected Routes: A user must be authenticated to access the dashboard.
- Form Validation: All form validations are handled with the Flask-WTForms plugin.
- Bootstrap 5.3.1: At the time of first commit, the most recent version of Bootstrap is used for styling. Dark mode is enabled by default.

## Installation

```bash
git clone https://github.com/narcisolobo/auth.git
cd auth
pipenv install
# Add more installation steps here, if needed
```

## Usage

To run this app, please rename `.env.example` to `.env` and replace the `SECRET_KEY` value with one of your own. Per the Flask documentation:
> A secret key that will be used for securely signing the session cookie and can be used for any other security related needs by extensions or your application. It should be a long random bytes or str.

I usually generate my secret keys in the Python shell using the `token_hex` method found in the `secrets` module.

```python
# python shell
>>> from secrets import token_hex
>>> print(token_hex())
```

Exit the shell and run the app by executing the `server.py` file.

```bash
# Mac
python3 server.py

# Windows
python server.py
```

## Contributing

I wholeheartedly welcome contributions to my project, whether through bug reports, feature requests, or pull requests.

```markdown
## How to Contribute

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request.
```

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

While I did not follow it to a T, I consulted the below article from Digital Ocean while creating this app.  
[How To Add Authentication to Your App with Flask-Login](https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login)

---