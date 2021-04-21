"""
    Session should be decoded by page then
    followed by _board
"""
from Util.Route import Routes


class BoardSessions:
    configRouteAction = Routes.getRouteAction(Routes.Config_Game)
    gameRouteAction = Routes.getRouteAction(Routes.Game_Url)
    KEYS = {
        configRouteAction: configRouteAction + '_board',
        gameRouteAction: gameRouteAction + '_board'
    }

    def __init__(self):
        pass

    @staticmethod
    def getBoardSession(url: str) -> str:
        page_action = url.rsplit('/', 1)[-1]
        if page_action in BoardSessions.KEYS:
            return BoardSessions.KEYS[page_action]

        return ''

