# Basic Flask Login Template

Basic Flask Login Template is a simple project template that can be used as a starting point for building Flask web applications that require user authentication. The template is built using Flask, Flask-Login, and SQLAlchemy.

## Features

* User registration with password hashing
* User login and logout
* User session management with Flask-Login
* SQLite database backend using SQLAlchemy

## Installation

1. Clone or download the project from the [GitHub repository](https://github.com/shaumne/flask_login_tem).

   `git clone https://github.com/shaumne/flask_login_temp`
2. Create a virtual environment and activate it.
3. Install the dependencies with the following command:

   <pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg></button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs">pip install -r requirements.txt
   </code></div></div></pre>
4. Create a new file named `config.py` in the root directory with the following content:

   <pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span></span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg></button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-arduino">SECRET_KEY = 'your_secret_key'
   </code></div></div></pre>
5. Initialize the SQLite database with the following command:

   <pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg></button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs">python db_create.py
   </code></div></div></pre>
6. Start the application with the following command:

   <pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span></span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg></button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-arduino">python main.py
   </code></div></div></pre>

## Usage

Once the application is running, you can access it by navigating to [http://localhost:5000](http://localhost:5000/) in your web browser. From there, you can register a new user account, log in, and log out.

To use the Basic Flask Login Template in your own project, you can copy and modify the code as needed. The following files are the main components of the template:

* `app.py`: Contains the Flask application code and routes.
* `db.py`: Contains the database configuration and session management code.
* `models.py`: Contains the SQLAlchemy model definitions for the database tables.
* `templates/`: Contains the HTML templates used by the application.

## Contributing

If you find any bugs or issues with the Basic Flask Login Template, please feel free to open an issue on the [GitHub repository](https://github.com/yourusername/basic-flask-login-template). Pull requests are also welcome!
