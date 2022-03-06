set -e

python3 deployment/create_secrets.py
docker-compose build
docker-compose push
docker-compose up -d coordinator
docker-compose logs --follow coordinator