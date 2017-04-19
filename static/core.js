var scotchTodo = angular.module('rutvijTodo', []);

scotchTodo.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
 }); // NEWLY ADDED


function mainController($scope, $http) {
        $scope.formData = {};
        
        // when landing on the page, get all todos and show them
       
        // when submitting the add form, send the text to the node API
        $scope.createTodo = function() {
                $http.post('/api/getPrediction', $scope.formData)
                        .success(function(data) {
                                $scope.formData = {}; // clear the form so our user is ready to enter another
                                $scope.todos = data;
                                $scope.table = { fields: data.result };
   				console.log($scope.table);
                        })
.error(function(data) {
                                console.log('Error: ' + data);
                        });
        };

        // Update the data
         $scope.updateTodo = function() {
               console.log($scope.table);
        };
      
}


