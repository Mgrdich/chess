class Routes:
    Index = '/'
    Game_Url = '/game'
    Config_Game = '/config-game'
    Api_Make_Move = '/api/make-move'
    Api_Moves = '/api/moves'

    def __init__(self):
        pass

    @staticmethod
    def getRoute(route: str, param: str = '') -> str:
        if param:
            return route + '/' + param

        return route
