import os
import sys

args = ["server", "postgres", "migrate_tables", "create_revision", "-d"]
args_alias = {arg: arg for arg in args}
args_alias = {**args_alias,
    "pg": args[1],
    "migrate": args[2],
    "revision": args[3],
    "detach": "-d"
}

result = ""
for arg in sys.argv[1:]:
    if arg == "all":
        result = f"{args[0]} {args[1]} "
        continue
    if arg in result:
        continue
    if arg not in args_alias:
        print(f"Wrong argument: {arg}")
        exit(0)
    result += args_alias[arg] + " "
try:
    os.system(f"docker-compose --env-file backend/db.yaml --env-file backend/server/config.yaml --env-file .env up --build {result}")
except KeyboardInterrupt:
    exit(0)