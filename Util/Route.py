class Routes:
    # TODO maybe turn this into Enum??
    Index = '/'
    Game_Url = '/game'
    Config_Game = '/config-game'
    Api_Make_Move = '/api/make-move'
    Api_Moves = '/api/moves'

    def __init__(self):
        pass

    # maybe create two things one for internal use case and one for front ?
    @staticmethod
    def getRoute(route: str, param: str = '') -> str:
        if param:
            return route + '/' + param

        return route

    @staticmethod
    def getRouteAction(route: str) -> str:
        return route[1:]
