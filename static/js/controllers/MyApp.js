let myApp = angular.module('myApp', []);

myApp.controller('ChessCtrl', ['$scope', '$http', function ($scope, $http) {

}]);


myApp.directive('chessBoard', ['$parse', function ($parse) {
    return {
        restrict: 'E',
        scope: {
            id: '@'
        },
        replace:true,
        template: '<div id="{{id}}" style="width: 400px"></div>',
        link: function (scope, element, attrs) {
            // TODO bind events that are found in attribute

            var board = ChessBoard(scope.id, {
                draggable: true,
                pieceTheme:'/static/img/chesspieces/{piece}.png'
            });

            scope.$on('$destroy', function () {
                // TODO unbind events
            });
        }
    }
}]);