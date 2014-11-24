$(document).ready(function () {

    var $clienteForm = $('#cliente-form');
    $clienteForm.hide();
    $('#mostrar-form-btn').click(function () {
        $clienteForm.slideToggle();
    });

    var $cpfInput = $('#cpfInput');
    var $nomeInput = $('#nomeInput');
    var $rgInput = $('#rgInput');
    var $nascimentoInput = $('#nascimentoInput');
    var $nacionalidadeInput = $('#nacionalidadeInput');
    var $estado_civilInput = $('#estado_civilInput');
    var $profissaoInput = $('#profissaoInput');
    var $complementoInput = $('#complementoInput');
    var $cepInput = $('#cepInput');
    var $enderecoInput = $('#enderecoInput');
    var $numeroInput = $('#numeroInput');
    var $bairroInput = $('#bairroInput');
    var $cidadeInput = $('#cidadeInput');
    var $estadoInput = $('#estadoInput');
    var $telefoneInput = $('#telefoneInput');
    var $celularInput = $('#celularInput');
    var $emailInput = $('#emailInput');

    var $ajaxGif = $('#ajax-gif');

    var $cpfDiv = $('#cpfDiv');
    var $nomeDiv = $('#nomeDiv');
    var $rgDiv = $('#rgDiv');
    var $nascimentoDiv = $('#nascimentoDiv');
    var $nacionalidadeDiv = $('#nacionalidadeDiv');
    var $estado_civilDiv = $('#estado_civilDiv');
    var $profissaoDiv = $('#profissaoDiv');
    var $cepDiv = $('#cepDiv');
    var $enderecoDiv = $('#enderecoDiv');
    var $numeroDiv = $('#numeroDiv');
    var $bairroDiv = $('#bairroDiv');
    var $cidadeDiv = $('#cidadeDiv');
    var $estadoDiv = $('#estadoDiv');
    var $telefoneDiv = $('#telefoneDiv');
    var $celularDiv = $('#celularDiv');
    var $emailDiv = $('#emailDiv');

    $ajaxGif.hide();
    var $salvarBtn = $('#salvar-btn');

    var $helpCpfSpan = $('#help-cpf');
    var $helpNomeSpan = $('#help-nome');
    var $helpRgSpan = $('#help-rg');
    var $helpNascimentoSpan = $('#help-nascimento');
    var $helpNacionalidadeSpan = $('#help-nacionalidade');
    var $helpEstado_CivilSpan = $('#help-estado_civil');
    var $helpProfissaoSpan = $('#help-profissao');
    var $helpCepSpan = $('#help-cep');
    var $helpEnderecoSpan = $('#help-endereco');
    var $helpNumeroSpan = $('#help-numero');
    var $helpBairroSpan = $('#help-bairro');
    var $helpCidadeSpan = $('#help-cidade');
    var $helpEstadoSpan = $('#help-estado');
    var $helpTelefoneSpan = $('#help-telefone');
    var $helpCelularSpan = $('#help-celular');
    var $helpEmailSpan = $('#help-email');

    var $corpoTabela = $('#corpo-tabela');

    var adicionarLinha=function adicionarLinha(cliente) {
        var linha = '<tr id="tr' + cliente.id + '"> ' +
            '<td></td>' +
            '<td>' + cliente.id + '</td>' +
            '<td>' + cliente.cpf + '</td>' +
            '<td>' + cliente.nome + '</td>' +
            '<td>' + cliente.email + '</td>' +
            '<td><button id="bt' + cliente.id + '" class="btn btn-danger btn-sm"><i class="glyphicon glyphicon-trash"></i></button>' +
            '</td> </tr>';

        $corpoTabela.prepend(linha);

        var $linhaHtml = $('#tr' + cliente.id);

        $linhaHtml.hide();
        $linhaHtml.fadeIn();

        $('#bt' + cliente.id).click(function () {
            $linhaHtml.fadeOut();
            $.post('/clientes/rest/delete', {'cliente_id': cliente.id}).success(function () {
                $linhaHtml.remove();
            }).error(function () {
                alert('Remoção não funcionou');
                $linhaHtml.fadeIn();
            });
        });

    }

    $.get('/clientes/rest').success(function (listaDeClientes) {
        for (var i = 0; i < listaDeClientes.length; i += 1) {
            adicionarLinha(listaDeClientes[i]);
        }
    });

    $salvarBtn.click(function () {
        var cliente = {cpf: $cpfInput.val(),
                       nome: $nomeInput.val(),
                       email: $emailInput.val()};

        $ajaxGif.slideDown();
        $salvarBtn.hide();

        var cliente_psalvar = $.post('/clientes/rest/save', cliente);
        cliente_psalvar.success(function (cliente_do_servidor) {
            $cpfInput.val("");
            $cpfDiv.removeClass('has-error');
            $helpCpfSpan.text("");

            $nomeInput.val("");
            $nomeDiv.removeClass('has-error');
            $helpNomeSpan.text("");

            $emailInput.val("");
            $emailDiv.removeClass('has-error');
            $helpEmailSpan.text("");

            $clienteForm.fadeOut();
            adicionarLinha(cliente_do_servidor);
        });


        cliente_psalvar.error(function (errors) {

            if (errors.responseJSON != null && errors.responseJSON.cpf != null) {
                $cpfDiv.addClass('has-error');
                $helpCpfSpan.text(errors.responseJSON.cpf);
            } else {
                $cpfDiv.removeClass('has-error');
                $helpCpfSpan.text("");
             }

             if (errors.responseJSON != null && errors.responseJSON.nome != null) {
                 $nomeDiv.addClass('has-error');
                 $helpNomeSpan.text(errors.responseJSON.nome);
             } else {
                $nomeDiv.removeClass('has-error');
                $helpNomeSpan.text("");
             }

             if (errors.responseJSON != null && errors.responseJSON.email != null) {
                 $emailDiv.addClass('has-error');
                 $helpEmailSpan.text(errors.responseJSON.email);
             } else {
                 $emailDiv.removeClass('has-error');
                 $helpEmailSpan.text("");
             }
        });

        cliente_psalvar.always(function () {
            $ajaxGif.slideUp();
            $salvarBtn.slideDown();
        })
    });

});