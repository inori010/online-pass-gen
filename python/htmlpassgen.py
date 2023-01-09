from js import document
from pyodide import create_proxy
import secrets
import string
    
def create_password(e):
    global password
    from js import a
    library = string.ascii_letters + string.digits + "!@#$%&-/"
    password = "".join(secrets.choice(library) for i in range(int(a)))
    pyscript.write("generated-password", password)

create_password_proxy = create_proxy(create_password)
create_password_button = document.getElementById('generate-button')
create_password_button.addEventListener("click", create_password_proxy)