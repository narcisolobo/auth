import random
import string
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {"txt", "pdf", "png", "jpg", "jpeg", "gif", "webp"}


def allowed_file(filename: str):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def generate_random_string():
    letters = string.ascii_letters
    numbers = "1234567890"
    alphanumeric = letters + numbers
    random_string = "".join(random.choice(alphanumeric) for _ in range(9))
    return random_string


def unique_name(filename: str):
    split_filename = filename.rsplit(".", 1)
    prefix = split_filename[0].lower() + generate_random_string()
    return prefix + "." + split_filename[1].lower()


def safe_unique_name(filename: str):
    secure_name = secure_filename(filename)
    return unique_name(secure_name)
