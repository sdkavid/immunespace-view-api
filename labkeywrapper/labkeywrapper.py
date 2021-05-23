
from labkey.api_wrapper import APIWrapper
from labkey.exceptions import (
    RequestError,
    QueryNotFoundError,
    ServerContextError,
    ServerNotFoundError
)
from labkey.query import Pagination, QueryFilter
from requests.exceptions import Timeout
import json


class LabKeyWrapper:

    def __init__(self):
        with open("../config/keys.json", "r") as file:
            config = json.load(file)
        self.labkey_server = "https://immunespace.org"
        self.project_name = "Studies"  # Studies # container_path
        self.context_path = "study"  # study ?
        self.api_key = config.get("apiKey", False)

        if not self.api_key:
            raise Exception

        self.api = APIWrapper(
            self.labkey_server,
            self.project_name,
            self.context_path,
            self.api_key
        )

    def query(self):
        pass