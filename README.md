# MyChat
A browser chat app using Django as main framework.

The goal here is to create a python web app that I can use to practice CI/CD principles.
The app runs with redis and nginx as containers on the backend.

# How to run

1. Clone the repo
```
git clone https://github.com/juo20/MyChat.git
```
3. Create and activate virtual environment
```python
python3 -m venv path
```
```python
source path/bin/activate
```
3. Install pip requirements
```python
pip install -r /path/to/requirements.txt
```
4. Run django migrations
```python
python3 manage.py migrate
```
5. Make sure to have docker installed and run a redis container
```
docker run -dp 6379:6379 redis
```
7. Run django server
```python
python3 manage.py runserver
```

# Issues I need to amend

- [ ] Fix room name issue when there is whitespace
- [ ] Have the chat text area scroll with message when the end of the box is reached
- [ ] Add form validation + error messages for input fields
- [x] Display username instead of email in chat room
- [ ] Find a way to display all current users in a chat room
- [ ] Restrict URL access
- [ ] Fix the horrendous test case + add some actual useful ones
- [ ] Fix github workflow
- [x] Replace sqlite with postgresql
- [x] Add dockerfiles

