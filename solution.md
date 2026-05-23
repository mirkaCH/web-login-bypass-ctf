



```markdown

\# Solution: Web Login Bypass CTF



\## Vulnerability



The application contains weak authentication logic.



The login form checks whether the username is `admin`, but it does not correctly validate the password. Any non-empty password works as long as the username is `admin`.



\## Test Credentials



```text

Username: admin

Password: test

