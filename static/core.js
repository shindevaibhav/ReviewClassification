var scotchTodo = angular.module('rutvijTodo', []);

scotchTodo.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
 }); // NEWLY ADDED

//$scope.labels = ['summary','solution','problem','praise','neutrality','mitigation','localization'];
function mainController($scope, $http) {
        $scope.formData = {};
        $scope.labels = ['summary','solution','problem','praise','neutrality','mitigation','localization'];

        // when landing on the page, get all todos and show them
       
        // when submitting the add form, send the text to the node API
        $scope.createTodo = function() {
                $http.post('/api/getPrediction', $scope.formData)
                        .success(function(data) {
                                // clear the form so our user is ready to enter another
                                $scope.todos = data;
                                $scope.table = {'fields': data.result };
                                console.log("In here");
                                for(var i=0;i<7;i++){
               				console.log($scope.table.fields[i]);
               				if($scope.table.fields[i]=='Positive'){
                 				 $scope.table.fields[i]='1';
              				}else{
                 				 $scope.table.fields[i]='0';
              				}
              			}    
   				console.log($scope.table);
                        })
.error(function(data) {
                                console.log('Error: ' + data);
                        });
        };

        // Update the data
         $scope.updateTodo = function() {
               console.log($scope.table);
               //$scope.labels = ['summary','solution','problem','praise','neutrality','mitigation','localization'];
               console.log($scope.labels);
              // if(               
             // for(var i=0;i<7;i++){
             //  console.log($scope.table.fields[i]);
             //  if($scope.table.fields[i]=='Positive'){
             //     $scope.table.fields[i]='1';
             // }else{
             //    $scope.table.fields[i]='0';
             // }
             // }         

  	      
               console.log("rutvij..........."); 
               $scope.table.comment = $scope.formData;
               console.log($scope.table.fields[0]);
               $http.post('/api/postPrediction',$scope.table)
			.success(function(data) {
                              console.log("Success");
                         })
                        .error(function(data) {
                                console.log('Error: ' + data);
                         });
        };
      
}


