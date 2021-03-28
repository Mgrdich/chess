let myApp = angular.module('myApp', []);

myApp.controller('ChessCtrl', ['$scope', '$http', function ($scope, $http) {

}]);


myApp.directive('chessBoard', ['$parse', function ($parse) {
    return {
        restrict: 'A',
        replace:true,
        template: '<div id="{{id}}" style="width: 400px"></div>',
        link: function (scope, element, attrs) {

            var board = ChessBoard(element, {
                draggable: true,
                pieceTheme:'/static/img/chesspieces/{piece}.png',
                position:'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1' //start position
            });

            scope.$on('$destroy', function () {
                // TODO unbind events
            });
        }
    }
}]);