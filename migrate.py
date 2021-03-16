import ast
import os
import pickle
import mod
from constants import *


IS_TEST_ENV = os.environ.get("IS_TEST_ENV")

DATA_FILE = "data.json"
if IS_TEST_ENV:
    DATA_FILE = "test_data.json"


def load_old_participants():
    pass


def save_participants():
    with open(DATA_FILE, 'wb') as f:
        data = {
            "servers": {},
            "voting": {}
        }
        pickle.dump(data, f)


load_old_participants()
save_participants()
