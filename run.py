import os

try:
    os.system("docker-compose --env-file backend/db.yaml --env-file backend/server/config.yaml --env-file .env up --build")
except KeyboardInterrupt:
    exit(0)