# -*- coding: utf-8 -*-
"""
Dados completos e estruturados dos 38 slides do curso 'Como investir e gerenciar o seu dinheiro'.
"""

SLIDES_DATA = [
    # -------------------------------------------------------------------------
    # SLIDE 01: CAPA GERAL
    # -------------------------------------------------------------------------
    {
        "slide_num": 1,
        "type": "cover",
        "category": "FORMAÇÃO PRÁTICA • EDUCAÇÃO FINANCEIRA 2026",
        "title": 'Como Investir e Gerenciar <br><span class="gradient-text">o Seu Dinheiro</span>',
        "subtitle": 'O método direto ao ponto, sem juridiquês e com bom humor para dominar seu orçamento, sair das armadilhas dos bancos, bater a inflação com Renda Fixa, lucrar com Ações e FIIs e explorar Criptoativos com responsabilidade.',
        "cards": [
            {
                "icon": "emerald",
                "title": "6 Módulos Práticos",
                "desc": "Da mentalidade anti-dívidas à carteira global blindada e criptoativos com estratégias reais."
            },
            {
                "icon": "amber",
                "title": "6 Quizzes da Vida Real",
                "desc": "Dilemas do cotidiano: o 13º salário, o carro que quebrou, o gerente do banco e o primo do churrasco."
            },
            {
                "icon": "cyan",
                "title": "Certificado Executivo",
                "desc": "Emissão oficial personalizada com autenticação criptográfica INV-2026 e selo de excelência."
            }
        ],
        "tip": "<strong>Dica de Navegação:</strong> Use as setas do teclado <strong>← →</strong> para navegar, <strong>M</strong> para a trilha de aulas e clique em qualquer card ou ilustração para <strong>ampliar</strong> em tela cheia.",
        "svg_type": "cover"
    },

    # -------------------------------------------------------------------------
    # MÓDULO 01: MENTALIDADE FINANCEIRA & O JOGO DO DINHEIRO (Slides 2 a 7)
    # -------------------------------------------------------------------------
    {
        "slide_num": 2,
        "type": "lesson",
        "category": "MÓDULO 01 • MENTALIDADE & O JOGO DO DINHEIRO",
        "title": "O Paradoxo do Salário Alto & A Corrida dos Ratos",
        "subtitle": "Por que quem ganha R$ 20.000 muitas vezes vive mais sufocado e endividado do que quem ganha R$ 4.000.",
        "cards": [
            {
                "icon": "rose",
                "title": "A Inflação do Estilo de Vida",
                "desc": "Recebeu uma promoção de R$ 3.000? No dia seguinte troca de carro por um de parcela de R$ 3.500 e aluga um apartamento maior. Se seus gastos sobem no mesmo ritmo da renda, você continua escravo do trabalho."
            },
            {
                "icon": "cyan",
                "title": "Ativo vs Passivo (Sem Filtro)",
                "desc": "Como ensina Robert Kiyosaki: Ativo é tudo que põe dinheiro no seu bolso enquanto você dorme. Passivo é tudo que tira dinheiro do seu bolso. Seu carro zero não é investimento: é gerador de IPVA, seguro e manutenção."
            },
            {
                "icon": "emerald",
                "title": "A Régua da Riqueza Real",
                "desc": "Riqueza não é o extrato do que você gasta no restaurante caro para postar nos Stories. Riqueza é o número de meses que você sobrevive com dignidade e paz se parar de trabalhar hoje."
            }
        ],
        "tip": "<strong>Princípio Nº 1:</strong> Não importa quanto entra na sua conta todo dia 5; o que determina seu destino é quanto sobra para comprar sua liberdade.",
        "svg_badge": "MÓDULO 01 • AULA 01",
        "svg_icon": "scale"
    },
    {
        "slide_num": 3,
        "type": "lesson",
        "category": "MÓDULO 01 • MENTALIDADE & O JOGO DO DINHEIRO",
        "title": "As Regras de Ouro de Warren Buffett & O Jogo do Longo Prazo",
        "subtitle": "Mais de 90% da fortuna do maior investidor de todos os tempos foi construída após os 65 anos de idade.",
        "cards": [
            {
                "icon": "amber",
                "title": "Regra 1 e Regra 2",
                "desc": "Regra nº 1: Nunca perca dinheiro do seu patrimônio principal. Regra nº 2: Nunca esqueça a regra nº 1. Preservar o capital acumulado com suor vem sempre antes de tentar dobrar o dinheiro em aventuras mágicas."
            },
            {
                "icon": "cyan",
                "title": "O Círculo de Competência",
                "desc": "Só invista naquilo que você entende como funciona e como gera receita. Se alguém te oferecer uma 'oportunidade secreta e complexa demais para explicar', o segredo é que o dinheiro vai sumir."
            },
            {
                "icon": "emerald",
                "title": "A Bolsa Transfere Paciência",
                "desc": "Como diz Buffett: 'O mercado financeiro é uma máquina extraordinária de transferir dinheiro dos impacientes e afobados diretamente para a conta dos pacientes e disciplinados'."
            }
        ],
        "tip": "<strong>Choque de Realidade:</strong> Quem tenta ficar rico rápido na bolsa de valores geralmente fica pobre da noite para o dia. Quem aceita enriquecer devagar, chega lá com certeza matemática.",
        "svg_badge": "MÓDULO 01 • AULA 02",
        "svg_icon": "buffett"
    },
    {
        "slide_num": 4,
        "type": "lesson",
        "category": "MÓDULO 01 • MENTALIDADE & O JOGO DO DINHEIRO",
        "title": "A Matemática dos Juros Compostos: Devedor vs Investidor",
        "subtitle": "A oitava maravilha do mundo: quem entende os juros compostos, ganha; quem não entende, paga com lágrimas.",
        "cards": [
            {
                "icon": "emerald",
                "title": "A Bola de Neve a Seu Favor",
                "desc": "Aportando R$ 500 por mês a uma taxa média de 10% ao ano: em 20 anos você junta R$ 380.000. Deste total, apenas R$ 120.000 saíram do seu bolso; mais de R$ 260.000 foram gerados puramente pelos juros trabalhando para você."
            },
            {
                "icon": "rose",
                "title": "A Bola de Neve Contra Você",
                "desc": "Uma dívida no rotativo do cartão de R$ 2.000 a 14% ao mês vira mais de R$ 9.600 em apenas 12 meses e mais de R$ 46.000 em 24 meses. É a mesma matemática trabalhando para te falir."
            },
            {
                "icon": "blue",
                "title": "O Fator Tempo é Supremo",
                "desc": "Quem começa a investir R$ 200/mês aos 22 anos acumula mais patrimônio aos 50 do que quem começa com R$ 1.000/mês aos 40. Não espere ter muito dinheiro para começar: comece para ter muito dinheiro."
            }
        ],
        "tip": "<strong>Fórmula Mental:</strong> O tempo faz o trabalho pesado. Cada ano que você procrastina o primeiro aporte custa o equivalente a anos inteiros de salário no futuro.",
        "svg_badge": "MÓDULO 01 • AULA 03",
        "svg_icon": "compound"
    },
    {
        "slide_num": 5,
        "type": "lesson",
        "category": "MÓDULO 01 • MENTALIDADE & O JOGO DO DINHEIRO",
        "title": "O Sistema dos 3 Potes: Sobrevivência, Crescimento e Liberdade",
        "subtitle": "Acabe com a confusão mental dividindo seus recursos em caixas funcionais que trazem paz de espírito.",
        "cards": [
            {
                "icon": "cyan",
                "title": "Pote 1: O Pote do Presente (50%)",
                "desc": "O custo de vida básico inegociável: moradia, alimentação nutritiva, transporte, saúde e contas de consumo. É o piso de estabilidade que mantém sua rotina funcionando com dignidade."
            },
            {
                "icon": "amber",
                "title": "Pote 2: O Pote da Paz & Sonhos (30%)",
                "desc": "Sua Reserva de Emergência intocável para imprevistos + verba para desfrutar o presente (lazer, jantar com a família, viagens de férias) sem contrair um único centavo de dívida parcelada."
            },
            {
                "icon": "emerald",
                "title": "Pote 3: A Máquina da Liberdade (20%)",
                "desc": "Dinheiro que entra na corretora e NUNCA MAIS volta para consumo. Esse capital compra cotas de fundos, ações e títulos públicos que pagam dividendos e compram sua aposentadoria antecipada."
            }
        ],
        "tip": "<strong>Regra de Ouro:</strong> Nunca misture a conta do supermercado com a conta do seu futuro. Se você juntar tudo na mesma conta corrente, seu futuro será devorado no delivery de sexta-feira.",
        "svg_badge": "MÓDULO 01 • AULA 04",
        "svg_icon": "jars"
    },
    {
        "slide_num": 6,
        "type": "lesson",
        "category": "MÓDULO 01 • MENTALIDADE & O JOGO DO DINHEIRO",
        "title": "O Raio-X do Seu Dinheiro: Onde Está o Ralo da Sua Conta?",
        "subtitle": "Não são os grandes gastos que quebram as pessoas: são os microvazamentos invisíveis que escorrem todo mês.",
        "cards": [
            {
                "icon": "rose",
                "title": "As Tarifas Bancárias Fantasmas",
                "desc": "Bancos tradicionais cobram entre R$ 35 e R$ 85 por mês em 'pacotes de serviços' que quase ninguém usa. Pela Resolução nº 3.919 do Banco Central, você tem direito à Conta de Serviços Essenciais 100% gratuita."
            },
            {
                "icon": "amber",
                "title": "O Efeito Pix Compulsivo",
                "desc": "O Pix facilitou a vida, mas destruiu a dor de pagar. Gastos de R$ 15, R$ 25 e R$ 40 repetidos dezenas de vezes somam facilmente R$ 600 a R$ 1.000 ao longo do mês em besteiras que você nem lembra."
            },
            {
                "icon": "cyan",
                "title": "A Regra das 48 Horas",
                "desc": "Sentiu aquele desejo urgente de comprar algo não essencial na internet? Espere 48 horas antes de clicar no botão pagar. Em 80% das vezes, o pico de dopamina baixa e você percebe que não precisava daquilo."
            }
        ],
        "tip": "<strong>Diagnóstico Rápido:</strong> Encontrar R$ 300 de vazamentos no seu extrato e aplicar em Renda Fixa equivale a receber um aumento salarial líquido sem precisar pedir permissão ao seu chefe.",
        "svg_badge": "MÓDULO 01 • AULA 05",
        "svg_icon": "audit"
    },
    {
        "slide_num": 7,
        "type": "quiz",
        "quiz_id": 1,
        "category": "MÓDULO 01 • DESAFIO DE DECISÃO FINANCEIRA",
        "title": "Quiz 01: O Dilema do 13º Salário e da Promoção Inesperada",
        "subtitle": "Coloque em prática a mentalidade de investidor sob a tentação imediata do dinheiro extra na conta.",
        "scenario": 'Você foi promovido com aumento de 30% e, no mesmo dia, cai na sua conta a 1ª parcela do seu 13º salário (R$ 6.000 líquidos). No grupo de amigos, marcam uma viagem cara para o feriado, e você sente aquele impulso incontrolável de comprar o celular topo de linha do ano "porque você ralou muito e merece". Como age um investidor com maturidade executiva?',
        "options": [
            {
                "letter": "A",
                "desc": "Gasta todos os R$ 6.000 na viagem de luxo e financia o celular novo em 18 vezes no cartão, porque 'a vida é uma só e mês que vem o salário aumentado compensa tudo'.",
                "correct": False
            },
            {
                "letter": "B",
                "desc": "Reserva uma fatia justa (10% a 15%) para comemorar sua conquista com quem você ama, e direciona os 85% restantes para blindar a Reserva de Emergência e acelerar aportes.",
                "correct": True
            },
            {
                "letter": "C",
                "desc": "Tranca o dinheiro na gaveta sem comemorar nada, cancela qualquer lazer com amigos e passa o mês comendo miojo para provar que é um investidor rigoroso e sem sentimentos.",
                "correct": False
            }
        ],
        "feedback_text": "<strong>Resposta Correta (B):</strong> Parabéns! O segredo dos grandes investidores é o equilíbrio emocional inteligente. O extremismo da opção A te mantém na corrida dos ratos (gastando o que ainda não ganhou), e o extremismo da opção C gera frustração que culmina em recaídas compulsivas. Comemorar suas vitórias com 10-15% sacia sua mente, enquanto os 85% restantes compram sua liberdade real.",
        "svg_badge": "DESAFIO 01 • MENTALIDADE",
        "svg_icon": "quiz"
    },

    # -------------------------------------------------------------------------
    # MÓDULO 02: ORÇAMENTO SEM NEURA & RESERVA ANTI-CRISE (Slides 8 a 13)
    # -------------------------------------------------------------------------
    {
        "slide_num": 8,
        "type": "lesson",
        "category": "MÓDULO 02 • ORÇAMENTO SEM NEURA & RESERVA",
        "title": "O Método 50/30/20 Simplificado: Sem Planilhas Neuróticas",
        "subtitle": "A divisão financeira mais consagrada do mundo que funciona na vida real sem precisar anotar o cafezinho.",
        "cards": [
            {
                "icon": "cyan",
                "title": "50% Necessidades Essenciais",
                "desc": "Aluguel, condomínio, luz, água, feira, remédios e transporte. Se suas necessidades básicas estão engolindo 80% da sua renda líquida, seu padrão de vida atual está desalinhado com sua renda real."
            },
            {
                "icon": "amber",
                "title": "30% Desejos Pessoais & Lazer",
                "desc": "Jantares fora, cinema, viagens, hobbies, streaming e compras pessoais. Essa fatia é sagrada para você desfrutar do fruto do seu trabalho sem qualquer sentimento de culpa ou remorso."
            },
            {
                "icon": "emerald",
                "title": "20% Futuro & Independência",
                "desc": "A regra inegociável: pague-se primeiro. No mesmo dia em que o salário pinga na conta, 20% já é transferido para a corretora antes de pagar qualquer boleto do mês."
            }
        ],
        "tip": "<strong>Dica de Ouro:</strong> Se você deixar para investir 'o que sobrar no fim do mês', a resposta estatística é quase sempre zero. Invista primeiro, gaste o restante sem culpa.",
        "svg_badge": "MÓDULO 02 • AULA 01",
        "svg_icon": "budget"
    },
    {
        "slide_num": 9,
        "type": "lesson",
        "category": "MÓDULO 02 • ORÇAMENTO SEM NEURA & RESERVA",
        "title": "A Faxina dos Boletos Fantasmas: Assinaturas e Ralos Invisíveis",
        "subtitle": "Como resgatar de R$ 300 a R$ 800 por mês apenas eliminando serviços que você nem lembra que paga.",
        "cards": [
            {
                "icon": "rose",
                "title": "O Cemitério dos Streamings",
                "desc": "Você realmente assiste a 5 plataformas de séries simultaneamente? Assinar Netflix, HBO Max, Disney+, Prime e Apple TV juntos custa mais de R$ 180/mês. Alterne planos: assine um por vez e assista tudo o que quer."
            },
            {
                "icon": "amber",
                "title": "A Academia Teórica",
                "desc": "Pagar anuidade de academia de R$ 150/mês para comparecer 2 vezes a cada 4 meses é doar dinheiro aos donos do estabelecimento. Cancele e opte por corridas ao ar livre ou planos mensais flexíveis."
            },
            {
                "icon": "emerald",
                "title": "Renegociação de Internet e Celular",
                "desc": "Planos antigos ficam caros e desatualizados. Uma ligação cordial de 15 minutos para sua operadora solicitando a tabela atual de novos clientes costuma reduzir sua fatura em 30% a 50% de imediato."
            }
        ],
        "tip": "<strong>Exercício Prático:</strong> Abra a fatura do seu cartão dos últimos 3 meses com uma caneta vermelha. Marque tudo que você pagou mas não usou. O valor resgatado vai direto para seu patrimônio.",
        "svg_badge": "MÓDULO 02 • AULA 02",
        "svg_icon": "trash"
    },
    {
        "slide_num": 10,
        "type": "lesson",
        "category": "MÓDULO 02 • ORÇAMENTO SEM NEURA & RESERVA",
        "title": "Cartão de Crédito: Sua Maior Ferramenta ou Seu Pior Inimigo?",
        "subtitle": "Como acumular milhas, cashback e fluxo de caixa inteligente sem jamais pagar R$ 1 em juros bancários.",
        "cards": [
            {
                "icon": "emerald",
                "title": "Regra Suprema: Fatura em 100%",
                "desc": "Cartão de crédito é excelente ferramenta de pagamento, mas é o pior meio de empréstimo do universo. Nunca, sob hipótese alguma, pague o 'mínimo da fatura' ou parcele a fatura do cartão."
            },
            {
                "icon": "cyan",
                "title": "O Limite Não é Seu Dinheiro",
                "desc": "Ter R$ 15.000 de limite no cartão não significa que você é R$ 15.000 mais rico. Significa apenas que o banco tem uma corda de R$ 15.000 pronta para apertar o seu pescoço se você pisar em falso."
            },
            {
                "icon": "blue",
                "title": "Rentabilizando o Prazo de 30 Dias",
                "desc": "O investidor inteligente concentra gastos no cartão para manter o dinheiro na conta rendendo 100% do CDI durante os 30 dias até o vencimento da fatura, embolsando pontos e cashback no processo."
            }
        ],
        "tip": "<strong>Blindagem Mental:</strong> Se você não tem o dinheiro na conta para comprar o produto à vista hoje, você não tem o direito de comprar parcelado no cartão. Trate o crédito com respeito cirúrgico.",
        "svg_badge": "MÓDULO 02 • AULA 03",
        "svg_icon": "card"
    },
    {
        "slide_num": 11,
        "type": "lesson",
        "category": "MÓDULO 02 • ORÇAMENTO SEM NEURA & RESERVA",
        "title": "O Método Bola de Neve para Eliminar Dívidas sem Sofrimento",
        "subtitle": "A estratégia de Dave Ramsey para zerar débitos caros e recuperar de vez a tranquilidade das noites de sono.",
        "cards": [
            {
                "icon": "rose",
                "title": "Dívidas Caras Vêm Primeiro",
                "desc": "Não existe no planeta Terra nenhum investimento em ações, cripto ou renda fixa que renda mais do que os 14% ao mês do cheque especial ou rotativo. Antes de investir em ações, estanque a hemorragia das dívidas caras."
            },
            {
                "icon": "amber",
                "title": "A Bola de Neve Comportamental",
                "desc": "Liste todas as dívidas da menor para a maior em valor total. Quite a menorzinha primeiro. A sensação psicológica de vitória rápida te dá fôlego e dopamina para esmagar as próximas na sequência."
            },
            {
                "icon": "emerald",
                "title": "O Poder do Feirão Limpa-Nome",
                "desc": "Dívidas antigas com bancos podem ser renegociadas no Serasa Limpa Nome com descontos de 70% a 90% sobre o valor corrigido para quitação à vista. Guarde caixa e negocie na sua posição de força."
            }
        ],
        "tip": "<strong>Consciência Financeira:</strong> Estar endividado não é uma falha de caráter, é uma falha de estratégia temporária. Reconheça a situação, trace um plano de ataque e encerre esse ciclo.",
        "svg_badge": "MÓDULO 02 • AULA 04",
        "svg_icon": "snowball"
    },
    {
        "slide_num": 12,
        "type": "lesson",
        "category": "MÓDULO 02 • ORÇAMENTO SEM NEURA & RESERVA",
        "title": "A Sagrada Reserva de Emergência: Onde Deixar e Quanto Guardar",
        "subtitle": "O airbag financeiro que garante que um imprevisto na sua vida não vire uma tragédia patrimonial.",
        "cards": [
            {
                "icon": "cyan",
                "title": "Tamanho Ideal da Reserva",
                "desc": "De 3 a 6 meses do seu custo de vida essencial se você for CLT estável. De 6 a 12 meses se você for autônomo, profissional liberal ou PJ com receita sazonal. É a sua apólice de paz pessoal."
            },
            {
                "icon": "emerald",
                "title": "Onde DEVE Ficar a Reserva",
                "desc": "Apenas em investimentos com risco de crédito soberano/mínimo e liquidez imediata (D+0 ou D+1): Tesouro Selic ou CDB de liquidez diária que pague 100% do CDI em instituição sólida."
            },
            {
                "icon": "rose",
                "title": "Onde NUNCA Deixar a Reserva",
                "desc": "Nunca em ações, nunca em fundos imobiliários, nunca em criptoativos e nunca em títulos com carência de 2 anos. Reserva de emergência não serve para lucrar alto: serve para estar 100% disponível quando o caos bater."
            }
        ],
        "tip": "<strong>Regra Sagrada:</strong> Quem não tem reserva de emergência é obrigado a vender ações no pior momento da crise ou recorrer a empréstimos agiotas no banco para pagar um conserto urgente.",
        "svg_badge": "MÓDULO 02 • AULA 05",
        "svg_icon": "emergency"
    },
    {
        "slide_num": 13,
        "type": "quiz",
        "quiz_id": 2,
        "category": "MÓDULO 02 • DESAFIO DE DECISÃO FINANCEIRA",
        "title": "Quiz 02: O Radiador Estourou no Dia 27 e a Reserva Salva a Pele",
        "subtitle": "Como um investidor preparado lida com a clássica 'lei de Murphy' sem se endividar.",
        "scenario": 'Faltam 4 dias para cair o próximo salário. Na volta do trabalho numa sexta-feira chuvosa, seu carro ferve no meio da avenida e fumaça sai do capô. O guincho leva para a oficina e o mecânico diagnostica: junta do cabeçote e radiador estourados, custo de R$ 2.800 à vista. Sua conta corrente tem R$ 180, mas você possui R$ 15.000 na sua Reserva de Emergência no Tesouro Selic. Qual a decisão correta?',
        "options": [
            {
                "letter": "A",
                "desc": "Entra em pânico, liga para o gerente do banco e aceita um empréstimo pessoal com juros de 8,5% ao mês em 24 parcelas para não mexer no dinheiro investido.",
                "correct": False
            },
            {
                "letter": "B",
                "desc": "Resgata com calma e serenidade os R$ 2.800 da sua Reserva de Emergência, paga o conserto à vista com desconto e planeja recompor a reserva nos próximos 3 meses.",
                "correct": True
            },
            {
                "letter": "C",
                "desc": "Passa o carro para frente por metade do preço de tabela e vai trabalhar de patinete elétrico para não admitir que o carro quebrou.",
                "correct": False
            }
        ],
        "feedback_text": "<strong>Resposta Correta (B):</strong> Exatamente! Essa é a função sagrada e exclusiva da Reserva de Emergência: transformar o que seria uma catástrofe financeira e emocional em apenas um contratempo resolvido em minutos. Não tenha dó nem culpa de usar a reserva para emergências genuínas — para isso ela foi criada. Depois, basta focar em recompô-la com tranquilidade.",
        "svg_badge": "DESAFIO 02 • RESERVA DE CRISE",
        "svg_icon": "quiz"
    },

    # -------------------------------------------------------------------------
    # MÓDULO 03: RENDA FIXA INTELIGENTE & O FIM DA POUPANÇA (Slides 14 a 19)
    # -------------------------------------------------------------------------
    {
        "slide_num": 14,
        "type": "lesson",
        "category": "MÓDULO 03 • RENDA FIXA INTELIGENTE",
        "title": "Por Que a Caderneta de Poupança é um Crime Contra o Seu Futuro",
        "subtitle": "Entenda a mecânica perversa que faz a poupança perder para a inflação e enriquecer apenas os grandes bancos.",
        "cards": [
            {
                "icon": "rose",
                "title": "A Regra dos 70% da Selic",
                "desc": "Quando a Selic está acima de 8,5%, a poupança rende míseros 0,5% ao mês + TR (cerca de 6,17% ao ano). Enquanto isso, o Tesouro Selic e CDBs 100% CDI pagam mais de 10% a 13% ao ano com a mesma ou maior segurança."
            },
            {
                "icon": "amber",
                "title": "A Pegadinha do Aniversário",
                "desc": "A poupança só credita juros no dia do aniversário do depósito. Se você colocar o dinheiro no dia 1 e resgatar no dia 29, o banco lucrou com seu capital e você recebe ZERO centavos de rendimento. No CDI, rende todo dia útil."
            },
            {
                "icon": "emerald",
                "title": "O Efeito em 10 Anos",
                "desc": "R$ 50.000 aplicados por 10 anos na poupança versus no Tesouro Selic/CDI geram uma diferença brutal de mais de R$ 35.000 a favor da Renda Fixa inteligente. É o preço da comodidade e desinformação."
            }
        ],
        "tip": "<strong>Fato Irrefutável:</strong> O banco adora seu dinheiro na poupança: ele te remunera migalhas e empresta esse mesmo dinheiro para outras pessoas cobrando 12% ao mês no cheque especial.",
        "svg_badge": "MÓDULO 03 • AULA 01",
        "svg_icon": "fixed_income"
    },
    {
        "slide_num": 15,
        "type": "lesson",
        "category": "MÓDULO 03 • RENDA FIXA INTELIGENTE",
        "title": "O Guia Definitivo do Tesouro Direto: Selic, IPCA+ e Prefixados",
        "subtitle": "Como emprestar dinheiro para o pagador mais seguro de todo o país — o Tesouro Nacional.",
        "cards": [
            {
                "icon": "emerald",
                "title": "Tesouro Selic (Pós-Fixado)",
                "desc": "Rende a taxa Selic diária. Não oscila negativamente no resgate e tem liquidez imediata. É o ativo livre de risco mais seguro da economia brasileira. O porto seguro número 1 para sua Reserva de Emergência."
            },
            {
                "icon": "cyan",
                "title": "Tesouro IPCA+ (Proteção Real)",
                "desc": "Paga a inflação oficial (IPCA) + uma taxa real de juros fixada (ex: IPCA + 6,5% ao ano). Garante que seu poder de compra jamais seja corroído pela alta dos preços. O melhor título para aposentadoria a longo prazo."
            },
            {
                "icon": "amber",
                "title": "Tesouro Prefixado (Atenção)",
                "desc": "Trava a taxa exata na contratação (ex: 12% ao ano até 2029). Se carregar até o vencimento, recebe exatamente o combinado. Se vender antes, sofre 'marcação a mercado' e pode ter lucro ou prejuízo temporário."
            }
        ],
        "tip": "<strong>Conceito Chave:</strong> O Tesouro Direto tem risco de crédito soberano. Se o Governo do Brasil der calote no Tesouro Direto, todos os bancos privados do país já faliram muito antes.",
        "svg_badge": "MÓDULO 03 • AULA 02",
        "svg_icon": "treasury"
    },
    {
        "slide_num": 16,
        "type": "lesson",
        "category": "MÓDULO 03 • RENDA FIXA INTELIGENTE",
        "title": "O Cardápio dos Bancos: CDB, LCI e LCA Sem Complicação",
        "subtitle": "Decifrando a sopa de letrinhas das corretoras e calculando a isenção de Imposto de Renda no bolso.",
        "cards": [
            {
                "icon": "cyan",
                "title": "CDB (Certificado de Depósito Bancário)",
                "desc": "Você empresta dinheiro ao banco para ele financiar empréstimos. Sofre Imposto de Renda regressivo: de 22,5% (até 180 dias) até 15% (acima de 720 dias). Muito comum com liquidez diária ou prazos de 1 a 5 anos."
            },
            {
                "icon": "emerald",
                "title": "LCI & LCA (Isenção Total de IR)",
                "desc": "Letras de Crédito Imobiliário e do Agronegócio. Criadas para fomentar setores vitais. O governo concede 100% DE ISENÇÃO DE IMPOSTO DE RENDA para pessoas físicas! Todo rendimento vai direto para você."
            },
            {
                "icon": "amber",
                "title": "A Matemática da Equivalência",
                "desc": "Como a LCI/LCA não tem IR, uma LCI que paga 88% do CDI rende o mesmo ou mais do que um CDB de 105% do CDI para prazos de até 1 ano. Nunca compare taxas brutas: compare sempre o rendimento líquido no bolso."
            }
        ],
        "tip": "<strong>Dica de Estratégia:</strong> Exija no mínimo 100% do CDI em CDBs com liquidez diária. Em prazos fechados de 2 a 3 anos, busque LCIs/LCAs isentas que batam com folga os títulos tradicionais.",
        "svg_badge": "MÓDULO 03 • AULA 03",
        "svg_icon": "fixed_income"
    },
    {
        "slide_num": 17,
        "type": "lesson",
        "category": "MÓDULO 03 • RENDA FIXA INTELIGENTE",
        "title": "O Fundo Garantidor de Créditos (FGC): Seu Co-Piloto até R$ 250k",
        "subtitle": "A rede de proteção que permite você investir em bancos médios pagando 115% do CDI com tranquilidade.",
        "cards": [
            {
                "icon": "emerald",
                "title": "O Que o FGC Garante",
                "desc": "Se o banco emissor do seu CDB, LCI ou LCA falir ou sofrer liquidação judicial, o FGC devolve 100% do seu dinheiro aplicado + os rendimentos acumulados até o limite de R$ 250.000 por CPF e por conglomerado financeiro."
            },
            {
                "icon": "blue",
                "title": "O Limite Global de R$ 1 Milhão",
                "desc": "Você pode ter até R$ 250.000 em 4 bancos diferentes protegidos simultaneamente, totalizando o teto global de R$ 1 milhão a cada período de 4 anos. Uma salvaguarda fantástica para quem tem patrimônio em expansão."
            },
            {
                "icon": "rose",
                "title": "O Que o FGC NÃO Cobre",
                "desc": "O FGC não cobre Tesouro Direto (que tem garantia soberana do governo), nem Ações, nem Fundos Imobiliários, nem Debêntures e nem Criptoativos. Conheça as fronteiras da sua garantia."
            }
        ],
        "tip": "<strong>Truque Inteligente:</strong> Nunca aplique exatamente R$ 250.000 em um mesmo banco; aplique até R$ 200.000 para que os juros que vão render nos próximos anos não ultrapassem o teto coberto pelo FGC.",
        "svg_badge": "MÓDULO 03 • AULA 04",
        "svg_icon": "fgc"
    },
    {
        "slide_num": 18,
        "type": "lesson",
        "category": "MÓDULO 03 • RENDA FIXA INTELIGENTE",
        "title": "Montando uma Escada de Vencimentos (Bond Ladder)",
        "subtitle": "A estratégia profissional para ter previsibilidade de caixa, alta rentabilidade e liquidez programada ano a ano.",
        "cards": [
            {
                "icon": "cyan",
                "title": "O Que é a Escada de Vencimentos",
                "desc": "Em vez de travar todo o seu dinheiro num CDB de 5 anos ou deixar tudo em liquidez diária rendendo menos, você divide seu capital em degraus: 1 ano, 2 anos, 3 anos e 4 anos."
            },
            {
                "icon": "emerald",
                "title": "O Fluxo Contínuo de Resgate",
                "desc": "Todo ano vence uma fatia com a rentabilidade máxima contratada no passado. Você recebe o capital corrigido e decide: se precisa do dinheiro para um projeto, usa; se não precisa, reaplica no degrau mais longo."
            },
            {
                "icon": "amber",
                "title": "Captura das Melhores Taxas",
                "desc": "Com a escada, você nunca fica refém dos ciclos de juros. Se os juros sobem, você tem dinheiro vencendo para travar taxas altas; se caem, você já tem títulos antigos rendendo taxas elevadas por anos."
            }
        ],
        "tip": "<strong>Visão de Longo Prazo:</strong> Diversificar prazos de vencimento é tão importante quanto diversificar ativos. Mantenha sempre um lote vencendo a cada 6 ou 12 meses.",
        "svg_badge": "MÓDULO 03 • AULA 05",
        "svg_icon": "ladder"
    },
    {
        "slide_num": 19,
        "type": "quiz",
        "quiz_id": 3,
        "category": "MÓDULO 03 • DESAFIO DE DECISÃO FINANCEIRA",
        "title": "Quiz 03: A Ligação Sedutora do Gerente Oferecendo Capitalização",
        "subtitle": "Como reagir quando o gerente tenta bater a meta dele usando o seu dinheiro suado.",
        "scenario": 'Você acabou de receber R$ 10.000 na conta corrente. O gerente do seu banco liga extremamente simpático: "Olá! Como você é um cliente especial, tenho um produto exclusivo: você guarda R$ 500 por mês num Título de Capitalização Ouro, concorre a um carro zero e uma lancha todo mês e, daqui a 5 anos, pega todo o seu dinheiro de volta!" Como você responde?',
        "options": [
            {
                "letter": "A",
                "desc": "Aceita na hora, emocionado com a simpatia do gerente e já começa a pesquisar vagas de garagem para a lancha que certamente vai ganhar no sorteio.",
                "correct": False
            },
            {
                "letter": "B",
                "desc": "Agradece com elegância, recusa a oferta e investe por conta própria em títulos de Renda Fixa reais (Tesouro IPCA+ ou LCI/CDB), sabendo que capitalização é loteria com rendimento abaixo da inflação.",
                "correct": True
            },
            {
                "letter": "C",
                "desc": "Xinga o gerente no telefone e transfere seu dinheiro para um site de apostas esportivas de apostas de escanteios asiáticos.",
                "correct": False
            }
        ],
        "feedback_text": "<strong>Resposta Correta (B):</strong> Parabéns! Você acabou de se esquivar de um dos maiores ralos de dinheiro do sistema bancário brasileiro. Título de Capitalização NÃO é investimento: é um bilhete de rifa caríssimo que rende menos que a poupança e onde a inflação devora seu poder de compra em 5 anos. O gerente tem metas a bater para a agência; quem tem metas para o seu patrimônio é você!",
        "svg_badge": "DESAFIO 03 • RENDA FIXA",
        "svg_icon": "quiz"
    },

    # -------------------------------------------------------------------------
    # MÓDULO 04: RENDA VARIÁVEL: AÇÕES DE VALOR, DIVIDENDOS & FIIS (Slides 20 a 25)
    # -------------------------------------------------------------------------
    {
        "slide_num": 20,
        "type": "lesson",
        "category": "MÓDULO 04 • RENDA VARIÁVEL & DIVIDENDOS",
        "title": "Desmistificando a Bolsa: Você é Sócio de Negócios Reais, Não Apostador",
        "subtitle": "Esqueça os filmes de Wall Street e o estresse de Day Trade: ações são frações de empresas sólidas.",
        "cards": [
            {
                "icon": "emerald",
                "title": "O Que é Uma Ação de Verdade",
                "desc": "Ao comprar ações do Itaú, da Taesa ou da Vale, você não está comprando um bilhete de cassino: você virou coproprietário oficial de agências, torres de transmissão de energia ou ferrovias que geram bilhões em receita real."
            },
            {
                "icon": "rose",
                "title": "A Farsa do Day Trade",
                "desc": "Estudos da FGV comprovam que mais de 97% dos praticantes de Day Trade perdem dinheiro e menos de 0,5% ganha mais que um salário mínimo. A riqueza não vem de ficar encarando gráficos piscando 8 horas por dia."
            },
            {
                "icon": "cyan",
                "title": "A Postura de Proprietário",
                "desc": "Se você fosse dono de uma padaria lucrativa no seu bairro, você venderia sua padaria só porque um vizinho chato ofereceu pagar 5% a menos hoje? Trate suas ações com a mesma mentalidade de dono de negócio."
            }
        ],
        "tip": "<strong>Frase de Peter Lynch:</strong> 'Atrás de cada ação existe uma empresa de carne e osso. Descubra o que ela faz, como ganha dinheiro e se continuará indispensável nos próximos 15 anos.'",
        "svg_badge": "MÓDULO 04 • AULA 01",
        "svg_icon": "stocks"
    },
    {
        "slide_num": 21,
        "type": "lesson",
        "category": "MÓDULO 04 • RENDA VARIÁVEL & DIVIDENDOS",
        "title": "Fundos Imobiliários (FIIs): Receba 'Aluguel' Isento Todo Mês",
        "subtitle": "Como ser dono de shoppings, galpões logísticos da Amazon e agências bancárias a partir de R$ 10.",
        "cards": [
            {
                "icon": "emerald",
                "title": "O Pinga-Pinga Isento de IR",
                "desc": "Pela legislação brasileira, os FIIs são obrigados a distribuir no mínimo 95% do lucro líquido aos cotistas. E o melhor: para pessoas físicas, o rendimento mensal de aluguel é 100% ISENTO de Imposto de Renda!"
            },
            {
                "icon": "cyan",
                "title": "Imóvel Físico vs Fundo Imobiliário",
                "desc": "Imóvel físico exige R$ 300 mil, tem corretagem, vacância, inquilino que não paga condomínio e IR de até 27,5% no aluguel. No FII, você investe com R$ 100, tem inquilinos multinacionais e diversificação máxima."
            },
            {
                "icon": "amber",
                "title": "FIIs de Tijolo vs FIIs de Papel",
                "desc": "FIIs de Tijolo possuem prédios de verdade (lajes corporativas, galpões, shoppings). FIIs de Papel investem em títulos de crédito imobiliário (CRIs) atrelados à inflação ou ao CDI com altos rendimentos."
            }
        ],
        "tip": "<strong>O Poder Psicológico:</strong> Receber dividendos de FIIs caindo na sua conta todo dia 15 sem você precisar levantar da cadeira é o melhor estímulo para continuar aportando mês após mês.",
        "svg_badge": "MÓDULO 04 • AULA 02",
        "svg_icon": "fiis"
    },
    {
        "slide_num": 22,
        "type": "lesson",
        "category": "MÓDULO 04 • RENDA VARIÁVEL & DIVIDENDOS",
        "title": "O Método dos Dividendos Inteligentes (Barsi & Peter Lynch)",
        "subtitle": "A estratégia do maior investidor pessoa física do Brasil para transformar ações em previdência eterna.",
        "cards": [
            {
                "icon": "emerald",
                "title": "A Filosofia Barsi de Acumulação",
                "desc": "Luiz Barsi começou engraxate e hoje recebe milhões por dia em dividendos. O segredo dele? Ele nunca vende suas ações. Ele usa os dividendos para comprar mais ações, criando um efeito bola de neve imparável."
            },
            {
                "icon": "cyan",
                "title": "Dividend Yield & Preço-Teto",
                "desc": "Busque empresas com histórico consistente de distribuição e Dividend Yield superior a 6% ao ano. Estabeleça um preço-teto: se a cotação subir demais e o dividendo percentual cair, pare de comprar e espere correções."
            },
            {
                "icon": "amber",
                "title": "O Ponto de Virada (Break-Even)",
                "desc": "Chega um momento em que os dividendos que você recebe no mês são suficientes para comprar um novo lote inteiro de ações sem tirar 1 centavo do seu salário. A partir desse dia, sua liberdade é questão de tempo."
            }
        ],
        "tip": "<strong>Foco no Número de Ações:</strong> Não se preocupe se a cotação oscilou 3% hoje. Pergunte a si mesmo: 'Quantas ações geradoras de proventos eu acumulei este mês?'",
        "svg_badge": "MÓDULO 04 • AULA 03",
        "svg_icon": "dividends"
    },
    {
        "slide_num": 23,
        "type": "lesson",
        "category": "MÓDULO 04 • RENDA VARIÁVEL & DIVIDENDOS",
        "title": "O Filtro BESST: Os 5 Setores Mais Perenes da Bolsa",
        "subtitle": "As áreas da economia que a sociedade nunca deixa de pagar, faça chuva, faça sol ou durante recessões.",
        "cards": [
            {
                "icon": "cyan",
                "title": "B - Bancos & E - Energia Elétrica",
                "desc": "Bancos brasileiros têm as maiores margens do planeta e cobram spreads gordos. Empresas de Transmissão de Energia (como Taesa e Alupar) recebem receita garantida por contrato mesmo se ninguém ligar uma lâmpada."
            },
            {
                "icon": "blue",
                "title": "S - Saneamento & S - Seguros",
                "desc": "Saneamento (água e esgoto) é monopólio natural inegociável: ninguém corta a água. Seguradoras (BB Seguridade, Porto) recebem prêmios adiantados e aplicam bilhões em Renda Fixa a juros altos enquanto esperam sinistros."
            },
            {
                "icon": "emerald",
                "title": "T - Telecomunicações",
                "desc": "Internet e conectividade viraram necessidade básica humana tão vital quanto comida. Quem atrasa a conta de luz ou internet para comprar roupa nova? O consumidor sempre paga o básico primeiro."
            }
        ],
        "tip": "<strong>Lição de Defesa:</strong> Em crises severas, as pessoas cancelam viagens e restaurantes caros, mas continuam pagando a conta de água, luz, internet e a parcela do seguro de vida. Invista onde o fluxo nunca seca.",
        "svg_badge": "MÓDULO 04 • AULA 04",
        "svg_icon": "besst"
    },
    {
        "slide_num": 24,
        "type": "lesson",
        "category": "MÓDULO 04 • RENDA VARIÁVEL & DIVIDENDOS",
        "title": "A Psicologia do Mercado: Por Que a Manada Compra no Topo e Vende na Baixa",
        "subtitle": "Dominando as emoções primitivas de medo e ganância para comprar em liquidações históricas.",
        "cards": [
            {
                "icon": "rose",
                "title": "O Sr. Mercado de Benjamin Graham",
                "desc": "Imagine que você tem um sócio maníaco-depressivo chamado Sr. Mercado. Em dias de euforia, ele quer te vender ações a preços absurdamente caros. Em dias de pânico, ele aparece desesperado te vendendo pechinchas com 40% de desconto."
            },
            {
                "icon": "amber",
                "title": "A Parábola do Supermercado",
                "desc": "Se o supermercado faz uma queima de estoque e a picanha ou o azeite cai 30%, você corre para comprar ou sai gritando desesperado que nunca mais vai comer? Por que quando excelentes ações caem 20% as pessoas entram em pânico?"
            },
            {
                "icon": "emerald",
                "title": "Howard Marks & Os Ciclos",
                "desc": "Quando os jornais estampam manchetes apocalípticas e seus colegas dizem que 'a bolsa acabou', é exatamente a hora em que os maiores lucros futuros estão sendo semeados por quem tem estômago frio."
            }
        ],
        "tip": "<strong>Frase de Warren Buffett:</strong> 'Seja ganancioso quando os outros estão com medo, e seja temeroso quando os outros estão eufóricos e gananciosos.'",
        "svg_badge": "MÓDULO 04 • AULA 05",
        "svg_icon": "psychology"
    },
    {
        "slide_num": 25,
        "type": "quiz",
        "quiz_id": 4,
        "category": "MÓDULO 04 • DESAFIO DE DECISÃO FINANCEIRA",
        "title": "Quiz 04: O Noticiário Grita Caos e o Ibovespa Desaba 4,5%",
        "subtitle": "Teste sua frieza comportamental sob a pressão de um dia de sangue nas cotações.",
        "scenario": 'Uma crise política repentina estoura no noticiário durante a madrugada. Na abertura do pregão, o Ibovespa despenca 4,5% e as ações daquela empresa elétrica sólida que você comprou caem 6%. No grupo de WhatsApp da família, seu tio manda figurinhas de apocalipse dizendo que "o país vai quebrar e todo mundo deveria vender tudo agora". Qual a sua postura estratégica?',
        "options": [
            {
                "letter": "A",
                "desc": "Entra no aplicativo da corretora tremendo de nervoso, vende todas as suas ações com prejuízo no fundo do poço e jura que nunca mais entra na bolsa de valores.",
                "correct": False
            },
            {
                "letter": "B",
                "desc": "Verifica os fundamentos da empresa: ela continua lucrando, gerando energia e pagando dividendos intocados. Mantém a calma e aproveita a queda irracional para comprar mais cotas com desconto.",
                "correct": True
            },
            {
                "letter": "C",
                "desc": "Pega um empréstimo de R$ 50.000 no banco com juros rotativos para comprar contratos futuros de dólar alavancado tentando recuperar as perdas em 15 minutos.",
                "correct": False
            }
        ],
        "feedback_text": "<strong>Resposta Correta (B):</strong> Brilhante! Cotações oscilam todos os dias por histeria coletiva, mas o valor real de empresas sólidas depende de faturamento, lucros e caixa. Uma crise política não faz as pessoas pararem de acender a luz ou tomar banho quente. O investidor de sucesso compra ativos excelentes em dias de desconto enquanto a manada amadora vende em pânico.",
        "svg_badge": "DESAFIO 04 • PSICOLOGIA DA BOLSA",
        "svg_icon": "quiz"
    },

    # -------------------------------------------------------------------------
    # MÓDULO 05: CRIPTOATIVOS, BITCOIN & A NOVA FRONTEIRA DIGITAL (Slides 26 a 31)
    # -------------------------------------------------------------------------
    {
        "slide_num": 26,
        "type": "lesson",
        "category": "MÓDULO 05 • CRIPTOATIVOS & BITCOIN",
        "title": "O Que é o Bitcoin e Por Que a Escassez dos 21 Milhões Importa",
        "subtitle": "O ouro digital da internet e a proteção matemática contra a impressão desenfreada de dinheiro estatal.",
        "cards": [
            {
                "icon": "amber",
                "title": "Escassez Absoluta Imutável",
                "desc": "Governos imprimem trilhões de dólares e reais a qualquer momento, gerando inflação e perda de poder de compra. No Bitcoin, está gravado em código matemático: NUNCA existirão mais do que 21 milhões de moedas no mundo."
            },
            {
                "icon": "cyan",
                "title": "Descentralização & Censura Zero",
                "desc": "Nenhum presidente, juiz ou banco central pode 'fechar' o Bitcoin, confiscar seus saldos ou impedir você de transacionar. Ele roda em milhares de computadores distribuídos pelo planeta sem ponto único de falha."
            },
            {
                "icon": "emerald",
                "title": "O Halving a Cada 4 Anos",
                "desc": "A cada 210.000 blocos (cerca de 4 anos), a emissão de novos bitcoins cai pela metade automaticamente. Com a demanda global crescendo e a nova oferta despencando, a pressão estrutural de valorização no longo prazo é histórica."
            }
        ],
        "tip": "<strong>Conceito Fundamental:</strong> O Bitcoin não foi criado para substituir seu cartão de débito na padaria; ele nasceu como reserva de valor global independente e resistente a confiscos.",
        "svg_badge": "MÓDULO 05 • AULA 01",
        "svg_icon": "bitcoin"
    },
    {
        "slide_num": 27,
        "type": "lesson",
        "category": "MÓDULO 05 • CRIPTOATIVOS & BITCOIN",
        "title": "Criptoativos Sérios vs Micos, Memecoins e Pirâmides",
        "subtitle": "Como separar projetos tecnológicos de infraestrutura das promessas criminosas com foto de cachorro.",
        "cards": [
            {
                "icon": "emerald",
                "title": "Projetos de Primeira Linha (Blue Chips)",
                "desc": "Bitcoin (reserva de valor soberana) e Ethereum (a plataforma computacional descentralizada onde rodam contratos inteligentes, DeFi e tokenização de ativos do mundo real). Base sólida com adoção institucional trilionária."
            },
            {
                "icon": "rose",
                "title": "O Alerta Vermelho das Pirâmides",
                "desc": "Toda empresa ou guru que te promete 'rendimento fixo de 2% a 10% ao mês com criptomoedas' É GOLPE. Cripto é mercado volátil de renda variável. Garantir retorno fixo em cripto é a assinatura clássica de pirâmide Ponzi."
            },
            {
                "icon": "amber",
                "title": "A Armadilha das Memecoins",
                "desc": "Moedas com nomes engraçados e mascotes de bichinhos não possuem utilidade econômica. São jogos de batata quente especulativa: 99% viram pó e quem comprou na euforia fica com a conta zerada."
            }
        ],
        "tip": "<strong>Regra Anti-Fraude:</strong> Se você não sabe de onde vem o rendimento miraculoso que estão te pagando, o rendimento é você. Fique no arroz com feijão das grandes criptos consolidadas.",
        "svg_badge": "MÓDULO 05 • AULA 02",
        "svg_icon": "crypto_pyramid"
    },
    {
        "slide_num": 28,
        "type": "lesson",
        "category": "MÓDULO 05 • CRIPTOATIVOS & BITCOIN",
        "title": "Custódia Pessoal e Segurança: Not Your Keys, Not Your Coins",
        "subtitle": "Se você não tem o controle exclusivo das suas chaves privadas, você não tem criptomoedas de verdade.",
        "cards": [
            {
                "icon": "rose",
                "title": "A Lição do Colapso da FTX",
                "desc": "Deixar todo o seu saldo dentro de uma corretora de cripto (Exchange) significa que você não é dono dos bitcoins: você é apenas um credor desprotegido da corretora. Se ela quebrar ou sofrer golpe interno, seu saldo desaparece."
            },
            {
                "icon": "cyan",
                "title": "Hot Wallets vs Cold Wallets",
                "desc": "Hot Wallets (apps no celular como Exodus ou MetaMask) são práticas para quantias pequenas. Cold Wallets / Hardware Wallets (Ledger, Trezor, Jade) são cofres físicos 100% offline para guardar patrimônio relevante."
            },
            {
                "icon": "emerald",
                "title": "As 12/24 Palavras-Semente (Seed Phrase)",
                "desc": "Sua chave mestra de recuperação são 12 ou 24 palavras em inglês. Anote-as à mão em papel ou chapa de metal e guarde a sete chaves. NUNCA tire foto, nunca salve no WhatsApp e nunca digite no Google Drive."
            }
        ],
        "tip": "<strong>Mandamento Hacker:</strong> Nenhum suporte oficial de corretora ou carteira jamais vai te pedir suas 12 palavras secretas. Quem te pede suas palavras é sempre um golpista tentando te roubar.",
        "svg_badge": "MÓDULO 05 • AULA 03",
        "svg_icon": "coldwallet"
    },
    {
        "slide_num": 29,
        "type": "lesson",
        "category": "MÓDULO 05 • CRIPTOATIVOS & BITCOIN",
        "title": "A Estratégia DCA (Dollar Cost Averaging): Sem Estresse e Sem Gráficos",
        "subtitle": "Como acumular patrimônio em criptoativos sem perder o sono nem tentar adivinhar topos e fundos.",
        "cards": [
            {
                "icon": "emerald",
                "title": "O Que é o Método DCA",
                "desc": "Consiste em comprar um valor fixo em reais com periodicidade constante (ex: R$ 100 toda segunda-feira ou R$ 300 todo dia do pagamento), independentemente de o preço estar subindo ou caindo."
            },
            {
                "icon": "cyan",
                "title": "A Mágica do Preço Médio",
                "desc": "Quando o Bitcoin sobe, você compra menos frações e seu patrimônio valoriza. Quando o Bitcoin cai 40%, seus mesmos R$ 100 compram quase o dobro de frações. O DCA transforma a volatilidade violenta em aliada."
            },
            {
                "icon": "amber",
                "title": "Paz Mental e Zero Ansiedade",
                "desc": "Você se liberta da obrigação tola de tentar acertar o momento perfeito. Você não precisa passar madrugadas acompanhando Twitter/X ou gráficos de velas. O processo fica 100% automatizado e racional."
            }
        ],
        "tip": "<strong>Estatística Histórica:</strong> Praticamente 100% dos investidores que fizeram compras programadas (DCA) em Bitcoin por um período superior a 3 anos obtiveram rentabilidades extraordinárias.",
        "svg_badge": "MÓDULO 05 • AULA 04",
        "svg_icon": "dca"
    },
    {
        "slide_num": 30,
        "type": "lesson",
        "category": "MÓDULO 05 • CRIPTOATIVOS & BITCOIN",
        "title": "Alocação Consciente: A Regra de Ouro dos 2% a 5% da Carteira",
        "subtitle": "Exposição com potencial de valorização assimétrica sem colocar seu estilo de vida em risco.",
        "cards": [
            {
                "icon": "emerald",
                "title": "A Assimetria Convexa (Nassim Taleb)",
                "desc": "Colocar de 2% a 5% do seu portfólio em Bitcoin é a aposta assimétrica perfeita: se o ativo multiplicar por 10x, ele turbina todo o seu patrimônio global; se ele cair 70%, sua vida financeira continua 100% intacta."
            },
            {
                "icon": "rose",
                "title": "O Erro Mortal do 'All-In'",
                "desc": "Vender a casa da família, pegar empréstimo bancário ou colocar 80% do patrimônio em criptoativos é roleta russa. A volatilidade pode te obrigar a vender no prejuízo durante um inverno cripto para pagar contas."
            },
            {
                "icon": "blue",
                "title": "Rebalanceamento Periódico",
                "desc": "Se o Bitcoin explodir e seus 5% virarem 20% do total da sua carteira, o investidor sábio realiza parte do lucro e transfere para Renda Fixa ou FIIs, travando o ganho e voltando ao equilíbrio de segurança."
            }
        ],
        "tip": "<strong>Limite Racional:</strong> Cripto é tempero na comida: na medida certa traz um sabor espetacular; se despejar o pote inteiro na panela, estraga todo o jantar.",
        "svg_badge": "MÓDULO 05 • AULA 05",
        "svg_icon": "allocation"
    },
    {
        "slide_num": 31,
        "type": "quiz",
        "quiz_id": 5,
        "category": "MÓDULO 05 • DESAFIO DE DECISÃO FINANCEIRA",
        "title": "Quiz 05: A Dica Quente do Primo no Churrasco de Domingo",
        "subtitle": "Como se esquivar da armadilha clássica da moeda secreta com retorno garantido.",
        "scenario": 'No almoço de domingo da família, aquele seu primo que troca de emprego a cada 3 meses aparece com um relógio dourado chamativo e sussurra: "Descobri o Novo Bitcoin antes de todo mundo! É uma moeda chamada RocketDogCoin. Se você entrar hoje com R$ 5.000 no meu link, a empresa garante 4% de rendimento ao dia e você pode comprar um importado em dezembro!" O que você faz?',
        "options": [
            {
                "letter": "A",
                "desc": "Saca R$ 5.000 da sua poupança na hora e transfere via Pix para o primo, porque família vem em primeiro lugar e você não quer ficar de fora do foguete.",
                "correct": False
            },
            {
                "letter": "B",
                "desc": "Come mais um pedaço de pão de alho, elogia o relógio dele com bom humor e recusa com firmeza, ciente de que retorno fixo diário em cripto é a receita clássica de golpe e pirâmide financeira.",
                "correct": True
            },
            {
                "letter": "C",
                "desc": "Vende sua casa própria para colocar R$ 200.000 na RocketDogCoin para virar diamante supremo da rede do primo.",
                "correct": False
            }
        ],
        "feedback_text": "<strong>Resposta Correta (B):</strong> Sensacional! Você acabou de salvar o seu patrimônio de um golpe descarado. No mercado financeiro sério não existe 4% ao dia garantido — isso daria mais de 100.000% ao ano, o que tornaria seu primo mais rico que Elon Musk em 18 meses. Criptoativos legítimos não precisam de links de recrutamento nem promessas de ganhos fáceis. Mantenha seu foco no Bitcoin e Ethereum sob custódia própria.",
        "svg_badge": "DESAFIO 05 • DEFESA CRIPTO",
        "svg_icon": "quiz"
    },

    # -------------------------------------------------------------------------
    # MÓDULO 06: A CARTEIRA BLINDADA, REBALANCEAMENTO & LIBERDADE (Slides 32 a 37)
    # -------------------------------------------------------------------------
    {
        "slide_num": 32,
        "type": "lesson",
        "category": "MÓDULO 06 • PORTFÓLIO BLINDADO & LIBERDADE",
        "title": "A Teoria do Portfólio Blindado de Ray Dalio (All-Weather)",
        "subtitle": "A estratégia criada pelo maior gestor de fundos de hedge do planeta para prosperar em qualquer cenário.",
        "cards": [
            {
                "icon": "cyan",
                "title": "As 4 Estações Econômicas",
                "desc": "O mundo financeiro só tem 4 climas possíveis: 1) Inflação acima do esperado; 2) Inflação abaixo do esperado; 3) Crescimento econômico em alta; 4) Recessão e estagnação. Nenhum guru sabe qual clima virá amanhã."
            },
            {
                "icon": "emerald",
                "title": "O Barco que Navega em Toda Tempestade",
                "desc": "Em vez de apostar tudo em um único cenário, você aloca ativos descorrelacionados: Renda Fixa IPCA+ (protege na inflação), Ações e FIIs (lucram no crescimento), Ouro/Dólar (protegem no caos e na recessão)."
            },
            {
                "icon": "amber",
                "title": "A Redução Drástica da Volatilidade",
                "desc": "Quando as ações caem numa crise, o dólar e a renda fixa sobem. O resultado prático é que o seu patrimônio total quase não oscila negativamente e continua subindo em linha reta no longo prazo."
            }
        ],
        "tip": "<strong>Sabedoria de Dalio:</strong> 'Não tente prever o futuro nem apostar em qual cavalo vai vencer. Construa uma carruagem sólida que funcione tanto no asfalto liso quanto na lama.'",
        "svg_badge": "MÓDULO 06 • AULA 01",
        "svg_icon": "allweather"
    },
    {
        "slide_num": 33,
        "type": "lesson",
        "category": "MÓDULO 06 • PORTFÓLIO BLINDADO & LIBERDADE",
        "title": "Internacionalização do Patrimônio: Dólar, ETFs e Proteção Global",
        "subtitle": "Por que manter 100% do seu dinheiro no Brasil (apenas 1% da economia mundial) é um risco desnecessário.",
        "cards": [
            {
                "icon": "blue",
                "title": "O Risco Brasil (Custo País)",
                "desc": "O Brasil historicamente enfrenta crises fiscais, instabilidade política e depreciação da moeda. Se você tem 100% dos seus ovos na mesma cesta brasileira, você é refém das decisões de Brasília."
            },
            {
                "icon": "emerald",
                "title": "S&P 500: As 500 Maiores Empresas do Planeta",
                "desc": "Através de ETFs simples na B3 (como IVVB11 ou SPXI11) ou contas globais em dólar (Nomad, Avenue, Inter), você vira sócio de Apple, Microsoft, Google, Nvidia e Amazon a partir de R$ 100."
            },
            {
                "icon": "cyan",
                "title": "Seus Gastos Já São em Dólar",
                "desc": "Seu celular, seu computador, o trigo do pão francês, o combustível do seu carro e as viagens de férias são todos precificados em dólar. Ter investimentos em moeda forte é preservar seu poder de compra real."
            }
        ],
        "tip": "<strong>Estratégia Moderna:</strong> Alocar entre 15% e 30% do seu patrimônio em ativos globais dolarizados é a melhor blindagem patrimonial que um investidor individual pode construir.",
        "svg_badge": "MÓDULO 06 • AULA 02",
        "svg_icon": "globe"
    },
    {
        "slide_num": 34,
        "type": "lesson",
        "category": "MÓDULO 06 • PORTFÓLIO BLINDADO & LIBERDADE",
        "title": "O Número da Liberdade Financeira: A Regra dos 4% e a Renda Perpétua",
        "subtitle": "Quanto você realmente precisa ter investido para viver dos rendimentos pelo resto da vida?",
        "cards": [
            {
                "icon": "emerald",
                "title": "O Estudo de Trinity (A Regra dos 4%)",
                "desc": "Pesquisadores americanos comprovaram que um portfólio diversificado permite retirar 4% do valor total no primeiro ano e corrigir pela inflação nos anos seguintes com mais de 98% de chance de o dinheiro nunca acabar."
            },
            {
                "icon": "cyan",
                "title": "A Fórmula do Número Mágico",
                "desc": "Pegue o seu custo de vida anual desejado e multiplique por 25 ou 30. Exemplo: se você vive muito bem com R$ 6.000/mês (R$ 72.000/ano), seu número de liberdade total é R$ 1,8 milhão a R$ 2,1 milhões gerando renda perpétua."
            },
            {
                "icon": "amber",
                "title": "Liberdade Não é Parar de Trabalhar",
                "desc": "Liberdade financeira não significa ficar deitado numa rede sem fazer nada até o tédio bater. Significa ter a opção de trabalhar apenas no que você ama, com quem você quer e nos horários que você escolher."
            }
        ],
        "tip": "<strong>Meta Visível:</strong> Quando você descobre o seu 'Número da Liberdade', cada aporte de R$ 500 deixa de ser um sacrifício chato e passa a ser um passo a mais em direção à sua soberania de vida.",
        "svg_badge": "MÓDULO 06 • AULA 03",
        "svg_icon": "freedom"
    },
    {
        "slide_num": 35,
        "type": "lesson",
        "category": "MÓDULO 06 • PORTFÓLIO BLINDADO & LIBERDADE",
        "title": "Rebalanceamento em 15 Minutos: Comprando na Baixa no Automático",
        "subtitle": "O mecanismo disciplinar que te obriga a realizar lucros sem apego emocional e sem perder tempo.",
        "cards": [
            {
                "icon": "cyan",
                "title": "Definindo Suas Porcentagens Alvo",
                "desc": "Exemplo de carteira equilibrada: 45% Renda Fixa (IPCA+/CDI), 25% Ações de Dividendos, 15% Fundos Imobiliários, 10% Dólar/Global e 5% Cripto. Essas porcentagens formam a sua âncora de segurança."
            },
            {
                "icon": "emerald",
                "title": "O Aporte Inteligente do Mês",
                "desc": "A cada mês, você olha sua carteira por 10 minutos. Qual classe está mais abaixo da meta? Você direciona seu novo aporte exatamente para essa classe que ficou para trás (ou seja, a que está mais barata no momento)."
            },
            {
                "icon": "amber",
                "title": "Sem Giro Desnecessário de Carteira",
                "desc": "Você não precisa ficar vendendo e pagando DARF de Imposto de Renda a todo momento. O rebalanceamento é feito suavemente através dos novos aportes e do reinvestimento dos dividendos recebidos."
            }
        ],
        "tip": "<strong>Automatismo Disciplinado:</strong> O rebalanceamento elimina a dúvida cruel de 'o que comprar hoje?'. A própria matemática da sua carteira te diz exatamente para onde deve ir cada centavo.",
        "svg_badge": "MÓDULO 06 • AULA 04",
        "svg_icon": "rebalance"
    },
    {
        "slide_num": 36,
        "type": "lesson",
        "category": "MÓDULO 06 • PORTFÓLIO BLINDADO & LIBERDADE",
        "title": "Os 5 Mandamentos da Riqueza Duradoura",
        "subtitle": "A síntese executiva das lições que transformaram trabalhadores comuns em pessoas prósperas e tranquilas.",
        "cards": [
            {
                "icon": "emerald",
                "title": "1. Gaste Menos do que Ganha & Aporte Todo Mês",
                "desc": "Não existe fórmula mágica sem superávit financeiro. Pague-se primeiro e faça dos aportes mensais um compromisso inegociável tão sagrado quanto sua conta de luz."
            },
            {
                "icon": "cyan",
                "title": "2. Fuja de Promessas Fáceis & Juros Compostos",
                "desc": "Se alguém te oferecer ganhos rápidos, corra na direção oposta. Deixe os juros compostos agirem com paciência ao longo dos anos. Quem respeita o tempo nunca é traído por ele."
            },
            {
                "icon": "amber",
                "title": "3. Diversifique e Cuide da Sua Paz de Espírito",
                "desc": "Nunca coloque todos os ovos em uma única cesta. Tenha Renda Fixa, Imóveis, Ações e Moeda Forte. A verdadeira riqueza é conseguir deitar a cabeça no travesseiro e dormir como um bebê."
            }
        ],
        "tip": "<strong>Regra Suprema da Vida:</strong> O dinheiro é um servo extraordinário, mas é um mestre tirânico. Aprenda a gerenciá-lo com sabedoria para que ele trabalhe para você pelo resto dos seus dias.",
        "svg_badge": "MÓDULO 06 • AULA 05",
        "svg_icon": "commandments"
    },
    {
        "slide_num": 37,
        "type": "quiz",
        "quiz_id": 6,
        "category": "MÓDULO 06 • DESAFIO DE DECISÃO FINANCEIRA",
        "title": "Quiz 06: O Desafio da Bolada de R$ 50.000: Como Alocar com Maestria?",
        "subtitle": "O teste final do investidor executivo: distribuindo um capital relevante com precisão cirúrgica.",
        "scenario": 'Você recebeu uma bolada limpa de R$ 50.000 (proveniente de um bônus de desempenho ou acerto trabalhista). Você já possui uma Reserva de Emergência sólida de 6 meses montada no Tesouro Selic. Como um investidor executivo formado aloca esse capital para gerar patrimônio perpétuo?',
        "options": [
            {
                "letter": "A",
                "desc": "Troca de carro imediatamente, dá uma festa de comemoração de R$ 10.000 para os colegas e aposta o restante em opções a seco na bolsa para 'ver se dobra'.",
                "correct": False
            },
            {
                "letter": "B",
                "desc": "Distribui estrategicamente segundo seu plano de alocação: 45% em Renda Fixa IPCA+ longa, 25% em Ações de Valor/Dividendos, 15% em FIIs geradores de aluguel, 10% em ETF Global dolarizado e 5% em Bitcoin.",
                "correct": True
            },
            {
                "letter": "C",
                "desc": "Coloca os R$ 50.000 na caderneta de poupança do mesmo banco tradicional onde você abriu conta quando tinha 16 anos porque 'não confia em nada moderno'.",
                "correct": False
            }
        ],
        "feedback_text": "<strong>Resposta Correta (B):</strong> PERFEITO! Você atingiu o nível mais alto de maturidade e sabedoria financeira! Distribuir seu capital entre classes descorrelacionadas com proteção contra a inflação (IPCA+), geração de renda passiva mensal (FIIs e Dividendos), blindagem em moeda forte (ETFs Globais) e assimetria tecnológica (Bitcoin) é a exata receita dos grandes patrimônios mundiais. Parabéns pela formação executiva!",
        "svg_badge": "DESAFIO FINAL • MESTRIA",
        "svg_icon": "quiz"
    },

    # -------------------------------------------------------------------------
    # SLIDE 38: DASHBOARD EXECUTIVO FINAL & CERTIFICAÇÃO OFICIAL
    # -------------------------------------------------------------------------
    {
        "slide_num": 38,
        "type": "certificate",
        "category": "CERTIFICAÇÃO OFICIAL • FORMAÇÃO EXECUTIVA 2026",
        "title": "Certificado Oficial de Formação Executiva em Gestão Financeira & Investimentos",
        "subtitle": "Comprovação formal de proficiência em planejamento patrimonial, renda fixa, renda variável, criptoativos e alocação global.",
        "svg_badge": "CERTIFICAÇÃO OFICIAL",
        "svg_icon": "certificate"
    }
]
