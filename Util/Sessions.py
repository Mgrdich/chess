"""
    Session should be decoded by page then
    followed by _board
"""
from Util.Route import Routes


class BoardSessions:
    configRouteAction = Routes.getRouteAction(Routes.Config_Game)
    gameRouteAction = Routes.getRouteAction(Routes.Config_Game)
    KEYS = {
        configRouteAction: configRouteAction + '_board',
        gameRouteAction: gameRouteAction + '_board'
    }

    def __init__(self):
        pass

    @staticmethod
    def getBoardSessionFromRequest() -> str:
        pass
