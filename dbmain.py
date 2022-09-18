"""This simple CRUD application performs the following operations sequentially:
    1. Creates 100 new accounts with randomly generated IDs and randomly-computed balance amounts.
    2. Chooses two accounts at random and takes half of the money from the first and deposits it
     into the second.
    3. Chooses five accounts at random and deletes them.
"""

from models import Recordings
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from sqlalchemy_cockroachdb import run_transaction
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import uuid
import random
import os
from math import floor
import json

db_uri = "cockroachdb://maaz:a_yIxMeayWxo5af9bwJz3Q@free-tier14.aws-us-east-1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster%3Dday-ram-5055"
engine = None


def add_recordngs(recording):
    """Inserts a new account into the database."""

    db_uri = "cockroachdb://maaz:a_yIxMeayWxo5af9bwJz3Q@free-tier14.aws-us-east-1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster%3Dday-ram-5055"

    try:
        engine = create_engine(db_uri, connect_args={
            "application_name": "docs_simplecrud_sqlalchemy"})
        engine.execute(
            "CREATE TABLE IF NOT EXISTS recordings (id UUID PRIMARY KEY, recording JSONB)")
    except Exception as e:
        print("Failed to connect to database.")
        print(f"{e}")
    input()

    engine.execute(
        "CREATE TABLE IF NOT EXISTS recordings (id UUID PRIMARY KEY, recording JSONB)")
    # add recording to databse
    # with engine.connect() as conn:
    #     print(conn.info)
    #     conn.execute(
    #         # f'INSERT INTO recordings (id, recording) VALUES ({str(uuid.uuid4())}, {json.dumps(recording.tolist())})',
    #         "INSERT INTO public.recordings (id, recordings) VALUES (recording, \"[]\")",
    #     )

    engine.execute(
        "INSERT INTO recordings (id, recording) VALUES ({}, '[]')".format(str(uuid.uuid4())))


# try:
#     engine=create_engine(db_uri, connect_args={
#         "application_name": "docs_simplecrud_sqlalchemy"})
#     engine.execute(
#         "CREATE TABLE IF NOT EXISTS recordings (id UUID PRIMARY KEY, recording JSONB)")
# except Exception as e:
#     print("Failed to connect to database.")
#     print(f"{e}")
#     input()
