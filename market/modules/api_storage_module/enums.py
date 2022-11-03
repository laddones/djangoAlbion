from enum import Enum


class MethodEnum(str, Enum):

    #Test sing_up
    SIGN_IN_BOT_USER = 'signIn/'

    # Start POST link method
    CREATE_ADMIN_LINK = "links/createLink/"
    CREATE_ADMIN_LINK_LIST = "links/createLinkList/"
    # {link_id}
    UPDATE_ADMIN_LINK = "links/updateLink/"
    # End POST link method

    # Start GET link method
    GET_ADMIN_LINK_LIST = "links/getLinkList/"
    GET_COUNT_OF_LINK = "links/getCountOfLink/"
    # {link_id}
    GET_ADMIN_LIST = "links/getLink/"
    # {link_id}
    DELETE_ADMIN_LINK = "links/deleteLink/"
    GET_ADMIN_LINK_UPDATE_LIST = "links/getLinkUpdateList/"
    # End GET link method

    GET_USER_BY_ACCESS_TOKEN = "users/getMe/"
    GET_ADMIN_USER_LIST = "users/getUserList/"
    GET_USER_GLOBAL_STATISTIC = "users/getUserGlobalStatistic/"

    REFRESH_ACCESS_TOKEN = "users/refreshToken/"
    # {link_id}
    UPDATE_ADMIN_USER = "users/updateUser/"

