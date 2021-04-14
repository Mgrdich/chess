let myApp = angular.module('myApp', []);

myApp.controller('ChessCtrl', ['$scope', '$http', function ($scope, $http) {
    $scope.chessBoardConfigs = {};

}]);


myApp.directive('chessBoard', ['$http', function ($http) {
    return {
        restrict: 'A',
        replace: true,
        scope: {
            configs: '=?configs'
        },
        controller: function () {
            this.suggestions = {};
            let self = this;

            this.onDrop = function (source, target) {
                // see if the move is legal
                // console.log(source, target);

            };

            this.onDragStart = function (source, piece, position, orientation) {
                // do not pick up pieces if the game is over
                $http({
                    method: 'GET',
                    url: 'http://127.0.0.1:8080/api/moves/' + source
                }).then(function (data) {
                    if (data.status !== 200) {
                        return
                    }
                    self.suggestions[source] = data.data;

                }, function errorCallBack(err) {
                    console.log(err);
                })
            };

            this.onChange = function (oldPos, newPos) {
                console.log('Position changed:')
                console.log(oldPos, newPos);
                console.log('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            };
        },
        template: '<div style="width: 400px"></div>',
        link: function (scope, element, attrs, Ctrl) {
            scope.configs = scope.configs || {};

            let defaultConfig = {
                draggable: true,
                pieceTheme: '/static/img/chesspieces/{piece}.png',
                position: 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1', //start position,
                onDrop: Ctrl.onDrop,
                onDragStart: Ctrl.onDragStart,
                onChange: Ctrl.onChange
            };

            let board = ChessBoard(element, {
                ...defaultConfig,
                ...scope.configs
            });

            scope.$on('$destroy', function () {
                // TODO unbind events
            });
        }
    }
}]);