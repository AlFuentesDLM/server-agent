~~~bash
    python3 -m venv myenv
    source ./myenv/bin/activate
    pip install -r requirements.txt
    export AUDIT_URL=https://{auditserverurl}/api/v1/audit
    python3 main.py
~~~