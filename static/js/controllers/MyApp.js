let myApp = angular.module('myApp', []);

myApp.controller('ChessCtrl', ['$scope', '$http', function ($scope, $http) {
        $scope.chessBoardConfigs = {};

        // TODO  do it with ng-init
}]);


myApp.directive('chessBoard', ['$http', function ($http) {
    return {
        restrict: 'A',
        replace: true,
        scope: {
            configs: '=?configs'
        },
        template: '<div style="width: 400px"></div>',
        link: function (scope, element, attrs) {
            scope.configs = scope.configs || {};

            let defaultConfig = {
                draggable: true,
                pieceTheme: '/static/img/chesspieces/{piece}.png',
                position: 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1', //start position,
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