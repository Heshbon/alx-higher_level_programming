# Python - Network #1

For this project, I learned how to send and receive HTTP messages to URLs using the urllib and requests Python libraries. I worked on retrieving JSON resources, sending GET and POST requests, and manipulating data from an external service.

# Tasks 📃

# 0. What's my status? #0

  + <u>[0-hbtn_status.py]()</u>: Python script that fetches https://alx-intranet.hbtn.io/status.

# 1. Response header value #0

  + <u>[1-hbtn_header.py]()</u>: Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id.

# 2. POST an email #0

  + <u>[2-post_email.py]()</u>: Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter.

# 3. Error code #0

  + <u>[3-error_code.py]()</u>: Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).

# 4. What's my status? #1

  + <u>[4-hbtn_status.py]()</u>: Python script that fetches https://alx-intranet.hbtn.io/status

  + Use the package requests.

# 5. Response header value #1

  + <u>[5-hbtn_header.py]()</u>: Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header.

# 6. POST an email #1

  + <u>[6-post_email.py]()</u>: Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter.

# 7. Error code #1

  + <u>[7-error_code.py]()</u>: Python script that takes in a URL, sends a request to the URL and displays the body of the response.

# 8. Search API

  + <u>[8-json_api.py]()</u>: Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user.

	+ The letter must be sent in the variable q.

	+ If no argument is given, set q="".

	+ If the response body is properly JSON formatted and not empty, display the id and name like this: [<id>] <name>.

  + Use the package requests and sys.

# 9. My GitHub!

  + <u>[10-my_github.py]()</u>: Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id.
