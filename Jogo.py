import random
from mob import mobs
from mob import arma

insultos_pervtori = [

]
monstros = [
    mobs('Troll', 3, 10),
    mobs('Petista', 1, 5),
    mobs('Flamenguista', 4, 4),
    mobs('Goiano', 2, 7),
    mobs('Palmeirense', 3, 5),
    mobs('Pivete', 1, 3)
]
armas = [
    arma('Mão', 0),
    arma('Tijolo', 1),
    arma('Canivete', 2),
    arma('Machado', 3),
    arma('Revolver', 4),
]
caminhos = ['Rua deserta',
            'Ponte',
            'Caverna',
            'Viela escura',
            'Mata fechada',
            'Igreja']
mortes_jogador = ['Te Quebrou na porrada',
                  'Te partiu no meio',
                  'Te deu uma facada e saiu correndo',
                  'Mordeu sua virilha',
                  'Te bateu bem no ovo direito',
                  'Te deu uma saudade dela intankavel']


def morte():
    tipos_morte_player = ['O cara foi solado q nem clickou kkkkkk',
                          'Foi de base, F no chat',
                          'Infelizmente não tankou e foi de berço...',
                          'Capotou o corsa...',
                          'Você foi escalado pro Vasco...',
                          'Você foi de Jackson five...',
                          'Infelizmente você não tankou a cirurgia e foi de base as 19:35',
                          'Você deu o peido mestre...']
    print(tipos_morte_player[random.randint(0, 7)])
    print('Você morreu!')
    exit()

def morte_especial():
    print('Previtori não ta pra brincadeira... ele está atento aos seu movimentos e \n'
          'quando você se da conta ele já ' + mortes_jogador[random.randint(0, 5)])
    print(morte())

def alea5():
    num_a = random.randint(0, 5)
    return num_a


def luta_dificil(drop):
    defesa = armas[drop]
    maxi = 10 - defesa.dano
    numa = random.randint(1, maxi)
    print('Você ta entrando em uma luta Difícil!!!\n'
          'Você está lutando com ' + defesa.nome + ' que reduz o numero máximo em: ' + str(defesa.dano) +
          '\nVocê tem duas chances de acertar o número de 1 a ' + str(maxi) + '!')
    acerto = False
    chutes = 0
    while acerto == False and chutes <= 1:
        print('Você tem ' + str(2 - chutes) + ' Chutes')
        chute = int(input('Fala um número de 1 a ' + str(maxi) + ':\n'))
        if chute == numa:
            acerto = True
        elif chute > numa:
            print('Chute muito alto')
            chutes = chutes + 1
        elif chute < numa:
            print('Chute muito baixo')
            chutes = chutes + 1
    if chutes == 3:
        print('Você Perdeu!, o número era ' + str(numa))
        return 2
    else:
        print('Você ganhou! Foi apertado, mas esse Corno não foi perigo nem por um segundo!')
        return 1

def luta_facil(drop):
    defesa = armas[drop]
    maxi = 10 - defesa.dano
    numa = random.randint(1, maxi)
    print('Você ta entrando em uma luta!!!\n'
          'Você está lutando com ' + defesa.nome + ' que reduz o numero máximo em: ' + str(defesa.dano) +
          '\nVocê tem Três chances de acertar o número de 1 a ' + str(maxi) + '!')
    acerto = False
    chutes = 0
    while acerto == False and chutes <= 2:
        print('Você tem ' + str(3 - chutes) + ' Chutes')
        chute = int(input('Fala um número de 1 a ' + str(maxi) + ':\n'))
        if chute == numa:
            acerto = True
        elif chute > numa:
            print('Chute muito alto')
            chutes = chutes + 1
        elif chute < numa:
            print('Chute muito baixo')
            chutes = chutes + 1
    if chutes == 3:
        print('Você Perdeu!, o número era ' + str(numa))
        return 2
    else:
        print('Você ganhou!')
        return 1

def luta_impo(drop):
    defesa = armas[drop]
    maxi = 10 - defesa.dano
    numa = random.randint(1, maxi)
    print('Você ta entrando em uma luta Quase Impossível!!!\n'
          'Você está lutando com ' + defesa.nome + ' que reduz o numero máximo em: ' + str(defesa.dano) +
          '\nVocê tem Uma chances de acertar o número de 1 a ' + str(maxi) + '!')
    acerto = False
    chutes = 0
    while acerto == False and chutes <= 0:
        print('Você tem ' + str(1 - chutes) + ' Chutes')
        chute = int(input('Fala um número de 1 a ' + str(maxi) + ':\n'))
        if chute == numa:
            acerto = True
        elif chute > numa:
            print('Chute muito alto')
            chutes = chutes + 1
        elif chute < numa:
            print('Chute muito baixo')
            chutes = chutes + 1
    if chutes == 3:
        print('Você Perdeu!, o número era ' + str(numa))
        return 2
    else:
        print('Você ganhou!')
        return 1


def tutorial():
    drop = 0
    print('*** Você acorda meio tonto...***')
    print('-Qual é a de menos? Bicho fresco... - disse um homem alto, grisalho e quem sabe afrescado'
          '\n-Tá com sono?')
    print('1- Eu estou perdido, você pode me ajudar?'
          '\n2- Eu só quero morrer...')
    dec0 = input('Digite 1 ou 2:\n ')
    if dec0 == '1':
        print('-Tô de boas, mas acho que sei quem pode te ajudar, é um tal de Prevtori... Diz o Homem'
              '\n- A proposíto... qual seu nome?')
        nome = input('Qual seu nome?\n ')
        if nome == 'Prevtori':
            print('- Ha Ha Ha...  Debocha o Homem. \n'
                  '-Eu já ouvi esse nome antes... quero ver como você vai fazer depois')
        else:
            print('-Aaah... que nome estranho... ' + nome + '...nunca ouvi falar')
        print('-Então ' + nome + ' siga pela direita eu acho... ou era esquerda?... não! era a direita mesmo!')
        print('-Agora vaza!')
        print('***Qual direção seguir?*** \n1- Esquerda\n2- Direita\n ')
        dec1 = input('Digite 1 ou 2:\n ')
        if dec1 == '1':
            print('***Você encontrou um ' + creep1 + '!!!!')
            luta = luta_facil(drop)
            if luta == 1:
                print('***Voce matou o ' + creep1 +
                      ', mas encontrou um caminho sem saída... '
                      'Você tem que voltar e continuar por outro caminho')
            elif luta == 2:
                print('Infelizmente o  ' + creep1 + '  ' + mortes_jogador[alea5()])
                morte()
        print('***Você se depara com uma ' + local_zero + ' e...')
        print('1- Seguir reto\n2- Voltar')
        dec2 = input('Digite 1 ou 2:\n ')
        if dec2 == '1':
            print('***Você segue em frente...')
            return nome
        if dec2 == '2':
            print('***Quando você se vira você esbarra em um ' + str(monstros[alea5()].raca) + ' que '
                  + mortes_jogador[alea5()] + '... deu nem tempo de reagir...')
            print(morte())
    elif int(dec0) == '2':
        print('-Seu desejo é uma ordem parceiro!\n'
              '***Quando você se dá conta ele ' + mortes_jogador[alea5()])
        morte()

def transicao1():
    print('***Você entra na ' + local_zero + ' e encontra quem aquele cara tinha falado '
                                          'e se da conta de q não perguntou o nome dele.')
    print('***Você decide dar um nome a ele, qual vai ser?')
    chefe = input('Nome do doido lá:\n ')
    print('-----COMEÇA SEGUNDA PARTE------')
    return chefe

def segunda_parte():
    drop = 0
    print('-Você ai! - Berra um velho acabado igual maracuja de gaveta\n'
          '-Onde você pensa que vai? essa é a minha ' + local_zero + '!')
    print('***Você encara o velho e decide se parte pra cima dele ou se conversa...')
    dec1 = input('1- Partir pra cima e arrebentar esse velho broxa\n'
                 '2- tentar acalmar o corno manso\n')
    if dec1 == '1':
        luta = luta_dificil(drop)
        if luta == 1:
            print('***Voce matou um dos contrutores da Arca de Noé...')
            return False
        elif luta == 2:
            print(morte_especial())
        print('***Você avança como um raio pra cima do vovô, mas... ')
        print(morte_especial())
    if dec1 == '2':
        print('Você se apresenta como ' + nome +
              ' e conta que não lembra de nada e nem sabe como foi parar ali\n'
              'E conta que se encontrou com o ' + chefe + ' que disse que ele te ajudaria.')
        if nome == 'Prevtori':
            print('-Além de não fazer ideia de quem é ' + chefe + ' Que merda é essa?? Você tá brincando '
                                                                 'com a minha cara né?\n'
                  '-Ninguém tem o mesmo nome que eu... Seu Impostor!!!')
            resul = luta_dificil(drop)
            if resul == 1:
                print('***Voce matou um dos contrutores da Arca de Noé...')
                return False
            elif resul == 2:
                print(morte_especial())
            morte_especial()
        print('O velho te encara por um tempo e te pergunta:\n'
              '-E quem porra é ' + chefe + '? e que nome de bicho é esse? ' + nome + '.... nunca ouvi falar')
        print('-O meu Nome é Prevtori, mas pode me chamar de Prevtori')
        esp = input('Tá me entendendo?\n'
                    'qual é o meu nome?\n ')
        tentativas = 0
        while esp != 'Prevtori':
            esp = input('Escreve direito Viado!!:\n')
            tentativas += 1
            if tentativas == 3:
                print('Não tenho tempo pra isso não... Tá fudido na minha mão parceiro!')
                morte_especial()
        print('-Hmmmm... Pelo menos não é surdo... Mas como você '
              'invadiu minha ' + local_zero + ' ou você me faz um favor ou você vai tomar um reset')
        print('***Eai meu parceiro? vai deixar esse porra de Prevtori falar assim contigo???\n'
              '1- Tá maluco? esse velho tem cara de doido, melhor fazer oque ele quer...\n'
              '2- Eu não nasci um Corno pra levar desaforo pra casa, vou partir esse velho no meio\n')
        prevtori = input('Digite 1 ou 2:\n ')
        if prevtori == '1':
            print('Você fala calmamente: \n'
                  '-Éoque doido do caralho, para com essa porra ai, oque que tu quer que eu faça?')
            return True
        elif prevtori == '2':
            print('Bora vê então aki seu velho goiaba do caralho!!')
            resul = luta_dificil(drop)
            if resul == 1:
                print('***Voce matou um dos contrutores da Arca de Noé...')
                return False
            elif resul == 2:
                print(morte_especial())

def final_alt():
    new_nome1 = 'Pr' + nome[3:]
    new_nome2 = nome[:-3] + 'tori'
    nome_final ='Prev' + nome[2:-3] + 'tori'
    print('Prevtori está morto...')
    print('Agora sem saber pra que direção seguir nem oque fazer você está perdido...')
    print('Você vaga pela ' + local_zero + ' a procura de alguma pista ou algo útil')
    andadas = 0
    esquerda = 0
    while andadas <=5 and esquerda <=1:
        print('***Aonde procurar?\n'
              '1- Esquerda\n'
              '2- Direita')
        procu = input('Digite 1 ou 2:\n ')
        andadas += 1
        if procu == '1':
            print('Não acho que vá ter nada pra esse lado...')
            esquerda += 1
        else:
            print('Creio que aquele velho não tem nada por aqui,')
            esquerda -= 1
    if esquerda >= 1:
        print('Você encontra um velho caderno com algumas instruções meio apagadas,'
              ' mas é o suficiente pra você continuar a sua jornada!')
        return
    else:
        print('O tempo passa e tudo oque você encotra é um grande estoque de comida que parece ilimitado\n'
              'Você vê o tempo passar e suas mãos se enrugarem...\n'
              'a unica coisa que te chama atenção é o barulho do vento nessa ' + local_zero + '...')
        print('parece até um nome.... Prevtori.... e isso lá é um nome? e por falar nisso qual era o meu?')
        print('Você pensa e pensa.... qual era mesmo? ' + new_nome1 +'?.. ou era ' + nome + '?... quem sabe '
              + new_nome2 + '....')
        print('Quase certeza que era ' + nome_final + '... \n'
                                                      'Não... na verdade acho que era só Prevtori mesmo...')
        print('Após oque parecem decadas você vê um jovem correndo em sua direção e você berra: \n'
             '-Você ai!'
             '\n-Onde você pensa que vai? essa é a minha ' + local_zero + '!')

def missao(local_zero):
    drop = 0
    completo = False
    if local_zero == caminhos[0]:
 # Rua Deserta
        repetir_predio1 = False
        repetir_predio2 = False
        repetir_predio3 = False
        print('Você recebe a missão de Prevtori que te pede para procurar nos predios ao redor o seu velho diario...')
        print('Você entra na ' + local_zero)
        print('Você vê 3 prédios que batem com a descrição do Velho goiaba, um na esquerda e dois na direita.')
        print('Qual deles você quer entrar primeiro?')
        indecisao = 0
        while indecisao <= 4 and completo == False:
            dec0 = input(
                '1- Prédio da Esquerda\n2- Prédio da Direita perto\n3- Prédio da direita longe\nDigite 1, 2 ou 3:\n ')
            if dec0 == '1' and repetir_predio1 == True:
                print('Não há mais nada aqui que possa me interessar.')
            if dec0 == '2' and repetir_predio2 == True:
                print('***Você decide Voltar e Entregar o diário!***')
                completo = True
            if dec0 == '3' and repetir_predio3 == True:
                print('Não há mais nada aqui que possa me interessar.')
            if dec0 == '1' and repetir_predio1 == False:
                print(
                    'O prédio parece abandonado... apenas mobilia velha e empoeirada, '
                    'você entra em uma sala e vê um vulto num canto\n'
                    'Você quer se aproximar?\n'
                    '1- Sim, qualquer coisa eu mato ele na porrada oush\n'
                    '2- Não, tá maluco, doido, biluteteia??? imagina chegar até aki e '
                    'morrer de bobeira pra um Flamenguista??')
                comb0 = input('Digite 1 ou 2:\n ')
                if comb0 == '1':
                    print('Você se aproxima e percebe que é um ' + monstros[alea5()].raca + ' puto da cara!')
                    luta = luta_facil(drop)
                    if luta == 1:
                        print('Você vê o corpo dele sem vida e Pensa sozinho:\n'
                              'Como foi fácil acabar com ele... ainda mais com 3 chutes\n\n'
                              '*** Você encontra um... ' + armas[1].nome + '!!!, sua nova arma!!')
                        print('Você não vê mais nada de útil nesse prédio e volta para a rua...')
                        drop += 1
                        indecisao -= 1
                        repetir_predio1 = True
                    else:
                        morte()
                if comb0 == '2':
                    indecisao += 1
                    print('Você volta pra rua e tem que decidir pra onde vai...')
            elif dec0 == '2' and repetir_predio2 == False:
                print('Você anda pela direita e entra no primeiro prédio, dentro dele você encontra varias caixas.\n'
                      'A Velha gagá do Prevtori tinhe lhe falado dessas caixas!! o diario deve estar aqui!!\n'
                      'Você decide dar uma olhada nas caixas...')
                print('Você vê 12 caixas, em qual delas você quer olhar?')
                chute = 15
                demora = 0
                while chute != 0 and demora <= 11:
                    giro = random.randint(1, 12)
                    chute = int(input('Em qual caixa vc quer procurar de 1 a 12? \n (0 para sair da casa)\n '))
                    if chute == 0:
                        break
                    elif chute == giro:
                        print('CARALHO!!! Você encontrou o diário daquele velho broxa!!!\n'
                              'Você volta para a rua com o objetivo da missão em mãos\n'
                              '***Ir novamente para o Prédio 2 completará a missão***')
                        repetir_predio2 = True
                        indecisao -= 4
                        break
                    elif chute != giro:
                        print('Você NÃO encontra nada e quando levanta os olhos vc sente que '
                              'alguém embaralhou as caixas novamente...\n'
                              'Você não tem todo o tempo do mundo...')
                        demora += 1
                if demora >= 11:
                    print('Você está tão concentrado em tentar achar um padrão que não nota um ' + monstros[alea5()].raca +
                          ' que chegou \n por trás e ' + mortes_jogador[alea5()])
                    morte()
                print('Você volta a Rua...')
                indecisao += 1
            elif dec0 == '3' and repetir_predio3 == False:
                print('Você anda sozinho em direção ao Prédio na esquina e se sente observado...\n'
                      'Você chega na sua porta e vê que ela está trancada...\n'
                      'Você quer:\n'
                      '1- Tentar arrombar a porta.\n'
                      '2- Voltar pra trás.')
                dec3 = input('Digite 1 ou 2:\n ')
                if dec3 == '1':
                    print('Você se prepara... Toma distância e corre com tudo contra a porta...')
                    print('Você escuta um CRACK\n\nA porta parece inteira e quando você olha pra baixo a última'
                          ' coisa que você nota antes de tudo ficar escuro\né o seu ombro fora do lugar')
                    print('\nQuando você acorda você vê um ' + monstros[alea5()].raca +
                          ' te olhando de cima\n quando você pensa em se levantar e correr ele já ' + mortes_jogador[alea5()])
                    morte()

                if dec3 == '2':
                    print('Você sente um frio na espinha e olha ao redor...\nTá maluco que eu vou ficar aki!'
                          '\nVocê volta num pique que deixaria o Usain comendo poeira!'
                          '\n Se eu voltar ali eu sou um corno! Tá maluco boy.')
                    indecisao += 2
        if indecisao >= 4:
            print('Você se sente perdido e quando se da conta você acorda morto')
            morte()
    if local_zero == caminhos[1]:
# Ponte
        print('Você recebe a missão de Prevtori que te pede para procurar nos Carros o seu velho diario...')
        print('Você entra na ' + local_zero)
        print('Você começa a caminhar entre os carros que parecem abandonados a décadas.'
              'Alguns deles te chamam a atenção! Qual deles você quer olhar primeiro?')
        carro1 = False
        carro2 = False
        carro3 = False
        carro4 = False
        carro5 = False
        while completo == False:
            car = input('1- Marea preto\n'
                            '2- Pegeout prata\n'
                            '3- Fusca Azul\n'
                            '4- Camaro Vermelha\n'
                            '5- Brasília Amarela\n:  ')
            if car == '4' and carro4 == True:
                completo = True
                break
            elif car == '1' and carro1 == True:
                print('Não tem mais o que ver ali além de um marea sendo um marea.')
            elif car == '2' and carro2 == True:
                print('Não tem mais o que ver ali, vai que você realmente adquire um pegeout?')
            elif car == '3' and carro3 == True:
                print('Não tem mais o que ver ali, o Fusca Azul gera agressão involuntaria')
            elif car == '5' and carro5 == True:
                print('Não tem mais o que ver ali.')
            if car == '1' and carro1 == False:
                print('Você se aproxima do Marea com cuidado, ele parece estranho e o risco de combustão espontanêa é real!')
                car1 = input('Você quer correr o risco?\n1- Sim, eu tô maluco biluteteia biruta da cabeça\n'
                             '2- não comi merda não meu parceiro, perto de um Marea eu só chego depois de morto!\n ')
                if car1 == '1':
                    print('Parece que você comeu merda meu amigo, vc se aproxima e escuta um barulho alto vindo '
                          'dele antes de vê a bola de fogo!\nVocê deu sorte, mais um passo pra frente e você tinha perdido mais'
                          ' do que só as sombrancelhas!')
                    carro1 = True
                if car1 == '2':
                    print('Você decide seguir a razão e recua, após o segundo passo você vê a bola de fogo!\n'
                          'o Marea explodiu como de costume e você agradece por esta a uma distancia segura!')
                    carro1 = True
            if car == '2' and carro2 == False:
                print('Você se aproxima do Pegeout e começa a sentir o perigo de adquirir um deles\n'
                      'Você agradece por não ter a sua carteira com você pra nem correr o risco de comprar.')
                print('Dentro dele você vê o que uma alma penada, talvez condenada a ficar aqui até vender o carro!')
                ajud = input('Você quer tentar ajudar a alma artomentada?\n1- Sim, ninguém merece um carro assim, '
                      'vamos tentar da a segunda alegria do dono de pegeout\n'
                      '2- Melhor não, se ele me empurra esse monstro eu vou ficar preso aqui também....\n ')
                if ajud == '1':
                    print('Você se aproxima e o Fantasma ja lhe pergunta se você tem interesse no Pegeout 206 prata, 2 portas,\n'
                          'tudo funcionando, só o ar q tá meio fraco, mas nada que uma janela aberta não resolva!\n'
                          'Você diz que quer dar uma olhada e ele te olha com os olhos marejados.\n- Obrigado... '
                          'Você é um Héroi! - ele diz e desaparece!\n'
                          'Ele só precisava que alguem com noção demonstrasse interesse no carro...\n'
                          'Essa foi fácil, apesar de arriscadíssimo!')
                    print('***Você encontrou um ' + armas[1].nome + ' em baixo de um dos Pneus***')
                    drop += 1
                    carro2 = True
                if ajud == '2':
                    print('Você é um homem sensato e não deixou que um fantasma que caiu na arapuca te puxasse junto!\n'
                          'Você vai conseguir dormir em paz sabendo que não tem um pegeout na garagem.')
            if car == '3' and carro3 == False:
                print('Você se aproxima do fusca azul e um ' + monstros[alea5()].raca +
                      ' Aparece do nada e vem te agredir gritando "Fusca Azul!", '
                      'você não tem alternativa além de se defender!')
                car3 = luta_facil(drop)
                carro3 = True
                if car3 == 1:
                    print('Você acabou com a raça daquele corno infantil!, mas não encontra \n'
                          'nada além de um belo fusca azul!')
                    carro3 = True
                if car3 == 2:
                    print('Ele acerta o seu braço com uma força jamais vista...')
                    morte()
            if car == '4' and carro4 == False:
                print('Você se aproxima do Camaro e pensa quem era o Playboy q dirigia ese Bumblebee vermelho...\n'
                      'ao olhar no banco de trás você encontra um livro, mas a porta está trancada!\n'
                      'Você precisa de alguma coisa para quebrar o vidro! ')
                if drop >= 1:
                    print('***Você usa o tijolo para Arrebentar o vidro do '
                          'Camaro e consegue o Diário do velho broxa!***\n'
                          'Vir novamente ao Camaro completará a missão!')
                    carro4 = True
                else:
                    print('***Você tem que procurar em outros lugares!***')
            if car == '5' and carro5 == False:
                print('Você se aproxima da Brasília amarela e observa que suas portas estão abertas!\n'
                      'Apesar dessa cena lhe parecer familiar você não encontra nada de útil nela...')
                carro5 = True
    if local_zero == caminhos[2]:
# Caverna
        print('Você recebe a missão de Prevtori que te pede para procurar ao redor o seu velho diario...')
        print('Você entra na ' + local_zero)
        print('Você está num breu que não consegue nem ver oque está a sua frente!\n'
              'Suas opções são limitadas! o máximo que você pode fazer é sair tateando!\n'
              'para que lado você quer tatear?\n'
              '1- Esquerda\n2- Direita\n3- Frente')
        while completo == False:
            input('Digite 1, 2 ou 3:\n ')
            print('Você adentra na escuridão e no segundo passo sem vê a entrada da caverna você se perde...')
            print('Você não sabe nem pra que lado fica o teto... agora é tudo sorte!\nAdivinhe um número de 1 a 15!')
            saida = random.randint(0, 15)
            acerto = False
            desculpa = False
            tempo = 0
            while acerto == False:
                while desculpa == False:
                    chute = int(input('Qual seu chute de 1  a 15?\n  '))
                    if chute == saida:
                        desculpa = True
                    elif chute < 7:
                        print('Não consigo ver nada, mas parece ser um beco sem saída.')
                        tempo += 1
                    elif chute >= 7:
                        print('Droga... não pode ser por aqui... apenas pedras.')
                        tempo += 1
                    if tempo == 3:
                        print('Droga... eu não sei se escutei alguma coisa ou se foi algo da minha cabeça...')
                    if tempo == 5:
                        print('Eu tenho certeza que ouvi alguma coisa!! que merda é essa?')
                    if tempo == 7:
                        print('PORRRA! esse bicho tá do meu lado... eu posso sentir o seu cheiro Podre!')
                    if tempo ==8:
                        print('Uma criatura te ataca e te derruba no chão, apesar do breu você precisa se defender!')
                        resu = luta_facil(drop)
                        if resu == 1:
                            print('Você consegue se desvencilhar e correr!\n'
                                  'Ainda está perdido, pelo menos consegue um pouco mais de tempo!')
                            tempo -= 5
                        elif resu == 2:
                            print('A Criatura finca seus dentes na sua garganta...')
                            print(morte())
                print('***Você encontrou o Diario do Velho viado Prevtori!!!\n'
                      '*** Você encontra um... ' + armas[1].nome + '!!!, sua nova arma!!\n'
                      'Mas agora você precisa achar a saída!! e a Criatura se aproxima\n'
                      '1- Derrotar a Criatura e sair sem pressa\n'
                      '2- Fugir e tentar a sorte encontrando a sáida')
                drop += 1
                lut = int(input('Digite 1 ou 2:\n '))
                if lut == 1:
                    luta = luta_facil(drop)
                    if luta == 1:
                        print('Você consegue vencer a criatura que agora você examina e descobre que era\n'
                              'apenas uma capivara enorme... bem, antes ela do que eu!\n'
                              'Você vaga pela caverna sem pressa até encontrar a luz que vem de sua entrada.')
                        acerto = True
                        completo = True
                    if luta == 2:
                        print('A Criatura é mais forte do que você imaginava... Você é obrigado a fugir!')
                        lut = 2
                if lut == 2:
                    print('Você está correndo no escuro... 50% de chance de dar merda...')
                    bola = random.randint(1,2)
                    chut = int(input('Digite 1 ou 2:\n '))
                    if chut == bola:
                        print('Você corre no breu aos tropeços até que comeca a ver a luz da entrada da caverna!\n'
                              'Ainda bem que está de dia!! apesar de você não saber se ainda é do mesmo dia...')
                        acerto = True
                        completo = True
                    else:
                        print('Você corre para uma beco sem saída... pelo menos você não '
                              'consegue ver oque vai acontecer com você...'
                              '\nA ultima coisa que você sente é o Bafo da criatura na sua nuca')
                        print(morte())
    if local_zero == caminhos[3]:
# Viela Escura
        print('Você recebe a missão de Prevtori que te pede para procurar nos predios ao redor o seu velho diario...')
        print('Você entra na ' + local_zero)
    if local_zero == caminhos[4]:
# Mata Fechada
        print('Você recebe a missão de Prevtori que te pede para procurar nos arbustos ao redor o seu velho diario...')
        print('Você entra na ' + local_zero)
    if local_zero == caminhos[5]:
# Igreja
        print('Você recebe a missão de Prevtori que te pede para procurar ao redor o seu velho diario...')
        print('Você entra na ' + local_zero)
    elif completo == True:
        print('Você volta correndo pra devolver aquela merda pro velho broxa!!\n'
              'mas Lembra que ele te pediu para não ler o diario... eai meu parceiro?\n'
              'Vai escutar aquela quenga velha ou vai ser um pau no cu?\n'
              '1- Amarelar igual uma bicha, escutar o Velho Corno e ficar na curiosidade\n'
              '2- Ser um Pau no cu do Caralho e ler os segredos obscuros do Prev "Rola-murcha" tori?')
        diario = int(input('Digite 1 ou 2:\n '))
        if diario == 1:
            print('Você decide ser uma boa moça e seguir com a missão à risca! (com crase ein)')
            return 1
        elif diario == 2:
            print('-Aquele Velho baitola não manda nem na mulher dele vai mandar em mim?\n'
                  'Você descobre que o Velho era um cara que apareceu perdido aqui muito tempo atrás\n'
                  'e que com o tempo foi perdendo a memoria e do nada decidiu que iria se chamar Prevtori!!\n\n'
                  'Que parada zoada ein... quem inventou essa merda??')
            return 2


local_zero = caminhos[alea5()]
creep1 = monstros[alea5()].raca
creep2 = monstros[alea5()].raca
nome = tutorial()
chefe = transicao1()
prevtori = segunda_parte()
if prevtori == False:
    final_alt()
elif prevtori == True:
   print('Prevtori te da uma missão...\n'
         'TO BE CONTINUED')
r_missao = missao(local_zero)
if r_missao == 1:
    print('Você chega ao Prevtori e lhe entrega o diário!')
if r_missao == 2:
    print('Pelo seu olhar o Velho viado já sabe oque você fez\n'
          'Apesar dele parecer uma múmia ele não nasceu ontem!!'
          '\nQuando você abre a boca pra falar o Prevtori avança em sua direção!!')
