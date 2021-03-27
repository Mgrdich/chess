let app = angular.module('myApp');

app.config(['$rootScope', function ($rootScope) {
}]);

app.run(function () {
});


app.controller('ChessCtrl', ['$scope', '$http', function ($scope, $http) {

}]);


app.directive('chessBoard',['$parse', function ($parse) {
    return {
        restrict:'A',
        scope:{

        },
        template:'<div></div>',
        link:function (scope, element, attrs) {
            // TODO bind events that are found in attribute

            scope.$on('$destroy',function (){
               // TODO unbind events
            });
        }
    }
}])