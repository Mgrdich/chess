let myApp = angular.module('myApp', []);

const whiteSquareGrey = '#a9a9a9'
const blackSquareGrey = '#696969'

myApp.controller('ChessCtrl', ['$scope', '$http', function ($scope, $http) {
    $scope.chessBoardConfigs = {};

    $scope.form = {};

    $scope.submitFen = function (url) {
        if (!url || !$scope.form.fen) {
            return;
        }

        $http({
            method: 'POST',
            url: url,
            data: {
                fen: $scope.form.fen
            }
        }).then(function (data) {
            if (!data.status) {
                return; // TODO Validation later on
            }

            $scope.showChessBoard = true;
            $scope.boardFen = data.fen;

        }, function errorCallBack(err) {
            console.log(err);
        })
    }
}]);

myApp.directive('chessBoard', ['$http', function ($http) {
    return {
        restrict: 'A',
        replace: true,
        scope: {
            configs: '=?configs',
            pieceHashes: '=',
            suggestionUrl:'@',
            moveUrl:'@'
        },
        controller: function ($scope) {
            this.suggestions = {};
            let self = this;


            this.onDrop = function (source, target, element) {
                // see if the move is legal
                $scope.removeGreySquares();

                // illegal move
                if (!self.suggestions[source] || !self.suggestions[source].includes(target)) {
                    return 'snapback';
                }

                let move = target;
                if ($scope.pieceHashes[element] !== 'p') {
                    move = $scope.pieceHashes[element].toUpperCase() + move;
                }


            };

            this.onDragStart = function (source, piece, position, orientation) {
                // do not pick up pieces if the game is over
                console.log(source, piece, position)
            };

            this.onChange = function (oldPos, newPos) {
                console.log('Position changed:')
                console.log(oldPos, newPos);
                console.log('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            };

            this.grayFields = function (square) {
                let moves = self.suggestions[square];
                // exit if there are no moves available for this square
                if (moves.length === 0) return

                // highlight the square they moused over
                $scope.greySquare(square)

                // highlight the possible squares for this piece
                for (let i = 0; i < moves.length; i++) {
                    $scope.greySquare(moves[i]);
                }
            };

            this.onMouseoverSquare = function (square, piece) {
                // get list of possible moves for this square

                if (self.suggestions[square]) {
                    self.grayFields(square);
                    return;
                }

                $http({
                    method: 'GET',
                    url: 'http://127.0.0.1:8080/api/moves/' + square
                }).then(function (data) {
                    if (data.status !== 200) {
                        return
                    }
                    self.suggestions[square] = data.data.result;
                    self.grayFields(square);
                }, function errorCallBack(err) {
                    console.log(err);
                })

            };

            this.onMouseoutSquare = function (square, piece) {
                // removeGreySquares()
                $scope.removeGreySquares()
            };

        },
        template: '<div style="width: 400px"></div>',
        link: function (scope, element, attrs, Ctrl) {
            Ctrl.pieces_hash = scope.pieceHashes;

            scope.configs = scope.configs || {};

            let defaultConfig = {
                draggable: true,
                pieceTheme: '/static/img/chesspieces/{piece}.png',
                position: 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1', //start position,
                onDrop: Ctrl.onDrop,
                onDragStart: Ctrl.onDragStart,
                onMouseoutSquare: Ctrl.onMouseoutSquare,
                onMouseoverSquare: Ctrl.onMouseoverSquare,
                onChange: Ctrl.onChange
            };

            let board = ChessBoard(element, {
                ...defaultConfig,
                ...scope.configs
            });


            scope.removeGreySquares = function () {
                element.find('.square-55d63').css('background', '');
            };

            scope.greySquare = function (square) {
                let $square = element.find('.square-' + square);

                let background = whiteSquareGrey
                if ($square.hasClass('black-3c85d')) {
                    background = blackSquareGrey
                }

                $square.css('background', background)
            }

            scope.$on('$destroy', function () {
                // TODO unbind events
            });
        }
    }
}]);