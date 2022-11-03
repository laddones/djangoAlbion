from typing import Optional, List

import requests

from .enums import MethodEnum
from .schemas.access_token import AccessTokenSchema
from .schemas.global_link_statistic_schema import GlobalLinkStatisticSchema
from .schemas.link_schema import CreateLinkSchema, LinkDetailSchema, LinkActionSchema
from .schemas.user_schema import UserSignUpRequestSchema, UserGlobalStatisticSchema, \
    UserSchema
from .schemas.user_statistic_schema import UserStatisticSchema
from typing import List


class ApiStorageModule:
    bot_api_path = "/api/v1/bots/"
    admin_api_path = "/api/v1/admin/"

    def __init__(self, api_host: str):
        self.api_host = api_host

    def sing_in(self, user_schema: UserSignUpRequestSchema) -> AccessTokenSchema:
        url = self.api_host + self.bot_api_path + MethodEnum.SIGN_IN_BOT_USER
        response = requests.post(url, json=user_schema.dict())
        if response.status_code == 200:
            return AccessTokenSchema.parse_obj(response.json())

    def get_link(self, access_token: AccessTokenSchema, offset: str = '0', limit: str = '10') -> list[LinkDetailSchema]:
        headers = {
            "Authorization": "Bearer " + access_token.access_token,
        }
        url = self.api_host + self.admin_api_path + MethodEnum.GET_ADMIN_LINK_LIST + '?offset=' + offset + '&limit=' + limit
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return [LinkDetailSchema(**item) for item in response.json()]

