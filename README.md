# fla-n

Test task:

1. Write a Python script that will create a table in a database (use Postgres)
2. We access the script through NGINX at the URL http://localhost:9000/script
3. Script, DB and nginx must be packaged in Docker
4. Everything should be run from docker-compose.yml
5. All services must communicate with each other through the internal Docker network. NGINX must be available on port 9000
6. Upload script, Dockerfile, docker-compose.yml (+ if you need nginx configs) in public access on GitHub
