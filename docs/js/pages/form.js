// Lógica exclusiva da página do formulário (junta tudo pra rodar)//

import { enviarResposta } from '../services/respostasServices.js';
// Função que efetivamente envia os dados do formulário pro backend

import { mostrarMensagem } from '../components/mensagem.js';
// Mostra feedback visual (sucesso/erro) pro usuário depois do envio

import { validarFormulario } from '../utils/validacao.js';
// Confere os dados antes de enviar, evitando mandar campo vazio/errado pro backend