# Server Agent

this repository contains a short script that gather data from the system where is executed, then send it to a cloud server where is stored in a relational database.

# Requirements

- python3
- pip3
- webserver - [this web server](https://github.com/AlFuentesDLM/api-compliance)


# Install

~~~bash
    pip3 install -r requirements.txt
    export AUDIT_URL={auditserverurl}
    python3 main.py
~~~
expected output
~~~bash
> the request was successfully sent to the audit server
> make a get request to our api to see the results
> http://audit-server.../api/v1/audit/4
> http://audit-server.../api/v1/audit/4/process
> http://audit-server/api/v1/audit/4/users
~~~