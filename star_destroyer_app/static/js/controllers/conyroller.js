
var starApp = angular.module('StarApp',['ngResource']);



starApp.factory('Ships', [ '$resource', function($resourse){
    return $resourse('http://127.0.0.1\\:8000/destroyers/ships/', {})

}]);

starApp.controller('StarCtr', ['$scope', 'Ships', function($scope, Ships){
    console.log('Hello');
    $scope.title = "Stardestoyers";
    $scope.ships = Ships.query();
    }]);
