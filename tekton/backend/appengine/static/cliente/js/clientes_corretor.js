var clienteModulo = angular.module('cliente-modulo', ['cliente-servico']);

clienteModulo.directive('clienteForm', [function () {
    return {
        restrict: 'E',
        templateUrl: '/static/cliente/html/form.html',
        scope: {clienteSalvo: '&'},
        controller: function ($scope, ClienteAPI) {
            $scope.cliente = {cpf: '', nome: '', email:''};
            $scope.executandoSalvamento = false;
            $scope.errors = {};

            $scope.salvar = function () {
                $scope.executandoSalvamento = true;
                $scope.errors = {};
                var promessa = ClienteAPI.salvar($scope.cliente);
                promessa.success(function (cliente) {
                    $scope.executandoSalvamento = false;
                    if ($scope.clienteSalvo != null) {
                        $scope.clienteSalvo({'cliente': cliente})
                    }
                });
                promessa.error(function (errors) {
                    $scope.errors = errors;
                    $scope.executandoSalvamento = false;
                });
            }
        }
    };
}]);

clienteModulo.directive('clienteLinha', [function () {
    return {
        restrict: 'A',
        replace: true,
        templateUrl: '/static/cliente/html/linha_corretor.html',
        scope: {
            cliente: '=',
            clienteDeletado: '&'
        },
        controller: function ($scope, ClienteAPI) {
            $scope.apagandoFlag = false;
            $scope.editandoFlag = false;
            $scope.clienteEdicao={};
            $scope.deletar = function () {
                $scope.apagandoFlag = true;
                ClienteAPI.deletar($scope.cliente.id).success(function () {
                    $scope.apagandoFlag = false;
                    if ($scope.clienteDeletado != null) {
                        $scope.clienteDeletado();
                    }
                });
            }

            function copiarCliente(origem, destino){
                destino.id=origem.id;
                destino.cpf=origem.cpf;
                destino.nome=origem.nome;
                destino.email=origem.email;

            }

            $scope.entrarModoEdicao = function () {
                $scope.editandoFlag = true;
                copiarCliente($scope.cliente, $scope.clienteEdicao);
            };

            $scope.sairModoEdicao = function () {
                $scope.editandoFlag = false;
            };

            $scope.editar=function (){
                ClienteAPI.editar($scope.clienteEdicao).success(function(clienteServidor){
                    copiarCliente(clienteServidor,$scope.cliente);
                    $scope.editandoFlag = false;

                });
            }
        }
    };
}]);