// Lógica exclusiva da página do dashboard (junta tudo pra rodar) //

import { buscarResumo } from '../services/resumoService.js';
// Busca os dados já calculados (total, média, por projeto) pro dashboard mostrar

import { criarGrafico } from '../components/grafico.js';
// Função que monta o gráfico de barras usando os dados recebidos

import { formatarNota } from '../utils/formatadores.js';
// Formata os números (ex: 4.666666 → 4.7) antes de exibir na tela