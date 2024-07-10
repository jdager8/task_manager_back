## Getting Started

First, Clone the repo:

```bash
source env/bin/activate
pip install requirements.txt -r
sudo docker-compose up -d
cd src
alembic upgrade head
fastapi dev main.py
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.
