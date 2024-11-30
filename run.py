import os
import sys

args = ["server", "postgres", "adminer", "migrate_tables", "create_revision", "-d"]
args_alias = {arg: arg for arg in args}
args_alias = {**args_alias,
    "pg": args[1],
    "migrate": args[3],
    "revision": args[4],
    "detach": "-d"
}


if len(sys.argv) < 3:
    print("Too few arguments")
    exit(0)

base_command = sys.argv[1]

if base_command == "up":
    base_command = "up --build"
else:
    base_command = "down"

result = ""
for arg in sys.argv[2:]:
    if arg == "all":
        result = f"{args[0]} {args[1]} {args[2]} "
        continue
    if arg in result:
        continue
    if arg not in args_alias:
        print(f"Wrong argument: {arg}")
        exit(0)
    result += args_alias[arg] + " "
try:
    os.system(f"docker-compose --env-file backend/db.yaml --env-file backend/server/config.yaml --env-file .env {base_command} {result}")
except KeyboardInterrupt:
    exit(0)