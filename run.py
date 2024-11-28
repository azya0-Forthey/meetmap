import os
import sys

result = ""
for arg in sys.argv[1:]:
    result += arg + " "
try:
    os.system(f"docker-compose --env-file backend/db.yaml --env-file backend/server/config.yaml --env-file .env up --build {result}")
except KeyboardInterrupt:
    exit(0)