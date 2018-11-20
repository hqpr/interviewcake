var myApp = angular.module('myApp', []).config(function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken'
});

myApp.controller('appCtrl', function($scope, $http) {

    myApp.config(['$qProvider', function ($qProvider) {
        $qProvider.errorOnUnhandledRejections(false);
    }]);

    $http.get('/api/v1/courses/readings/').
    then(function(response) {
        $scope.data = response.data;
    });

    $scope.update_reading = (function (id, $event) {
        var element = $event.currentTarget;
        $http.put('/api/v1/courses/r/'+id+'/', {}).then(function(response) {
            var marked = response.data.marked;
            if (marked) {
                element.classList.remove('bg-blue-600');
                element.classList.add('bg-green-600');
            } else
                element.classList.remove('bg-green-600');
                element.classList.add('bg-blue-600');
        });
    });
    $scope.update_question = (function (id, $event) {
        var element = $event.currentTarget;
        $http.put('/api/v1/courses/q/'+id+'/', {}).then(function(response) {
            var marked = response.data.marked;
            if (marked) {
                element.classList.remove('bg-blue-600');
                element.classList.add('bg-green-600');
            } else
                element.classList.remove('bg-green-600');
                element.classList.add('bg-blue-600');
        });
    });


});
