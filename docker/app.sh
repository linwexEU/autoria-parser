#!/bin/bash
cd src

alembic upgrade head

cd .. 

python -m src.main
