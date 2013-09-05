Subversão tecnológica: do Mac OS X para o Slackware Linux em um Apple MacBook Pro
#################################################################################
:date: 2012-11-21 12:22
:author: Deny Dias
:tags: MacBook Pro, Linux, introdução, software, Slackware, hardware, Apple, subversão, Mac OS X, tecnologia
:slug: subversao-tecnologica-do-mac-os-x-para

Quando as pessoas criam um blog, é bastante comum que o primeiro post
seja uma espécie de "lista de resoluções para o novo ano". Já vi isso
inúmeras vezes nesse tempão de internet. Coisas do tipo: "Me deu vontade
te ter um lugar pra falar sobre isso, aquilo, blá, blá, blá...". Bom, eu
vou pular essa parte e dizer apenas o seguinte: isso aqui existe porque
eu quero. Quando eu não quiser mais, deixará de existir. Simples assim.

Para o quê eu vou usar esse espaço é uma questão só minha. Se não
gostar do que ler/ver aqui, tenho duas sugestões: clique no botão
"Próximo blog" aí e cima ou \ `aqui`_. Você tem todo o direito de não
ler/ver o que existe aqui assim como eu tenho todo o direito de não ter
que lidar com o seu `#mimimi`_. Eu respeito o seu direito, você respeita
o meu. Justíssimo. Combinado?

Passado o prólogo, direto ao tema. Chupado de um post meu no Google+:

    Comecei minha vida tecnológica em um MSX. Z80 na veia, o mesmo que
    toca os carros do metrô do Rio! Depois fui para o Apple II e o seu
    lindo 6502. Depois de passar por algum tempo em coisas bem obtusas
    ainda disponíveis no início dos anos 90 do século passado, foi a vez
    do PC. Primeiro MS-DOS, daí OS/2, depois Linux (Slackware 3), e só
    então Windows. Esse último durou um tempo por causa das exigências
    corporativas.
    Particularmente, em 2000 escolhi o Mac, um iBook branquinho. Eu fui
    feliz com o Mac. Gostava tanto que até fui dono do maior site de
    notícias e comunidade sobre a plataforma no Brasil até 2007. Deste
    então, mais especificamente quando o iPhone surgiu e trouxe como
    'bônus' um ecossistema fechado, a Apple lentamente me empurrou pra
    longe dela. A Apple cuspiu nos princípios que a tornaram uma empresa
    de sucesso. Você pode ver Steve Jobs como um gênio dos negócios (e é
    mesmo), mas para mim ele é só o mais bem sucedidos dos ditadores. A
    Apple não merece mais a minha escolha política como consumidor.

Pois bem, há três semanas o único sistema operacional instalado em meu
MacBook Pro é um Linux, mais especificamente o \ `Slackware Linux`_.
Porquê escolhi o Slackware dentre as centenas de `distribuições
disponíveis`_ por aí é uma questão menor, de puro gosto e capacidade
técnica/intelectual. O fato relevante aqui é o \ `Linux`_, um
software/sistema operacional livre, gratuito, feito por gente como eu e
você para gente como eu e você rodando em algo feito para ser fechado,
proprietário, quase uma cela tecnológica. A subversão disso pode ser
boba para muito, mas eu acho linda! Nos termos da Apple e seus fanboys,
eu sou um herege. And I can't care less!

O hardware continua sendo o `MacBook Pro 7,1`_ (Mid-2010). No Mac OS X
que eu vinha usando, o `Lion`_ (10.7.5), o MBP já vinha mostrando sinais
da idade. Mesmo com os upgrades que fiz ao longo do tempo (8GB de RAM,
SSHD Seagate `Momentus XT`_), a máquina já dava seus sinais de que no
Mac OS X o seu ciclo de vida chegava ao fim. No máximo aguentaria até a
metade do ciclo do Mac OS X Mountain Lion (10.8). No que diz respeito à
Apple, o comportamento predatório do software em relação ao hardware é
exatamente o esperado. A cada novo lançamento de iDevices ou Macs, o que
vemos são early-adopters entulhando filas para comprar as novidades.
Além do hype inerente, o fato é que muitas funções do software deixam de
funcionar ou simplesmente não são mais suportadas no hardware antigo. É
uma estratégia de marketing que, apesar de não concordar, devo admitir
que `funciona`_.

Com o Linux a realidade sobre este hardware "antigo" é essa: tenho a
nítida impressão de ter uma nova máquina. Tudo é rápido, fluído,
eficiente. Os 8GB de memória, mesmos nos momentos de uso mais extremo e
com alto `multi-tasking`_ - até nos casos de uso raros no Mac OS X, como
compilar - até hoje não chegou aos 50% de consumo. Os outros 8GB de
memória virtual que reservei só vi serem utilizados uma vez, com a
memória em 48% e 60MB de swap em uso.

O processador, um `Intel(r) Core(tm) 2 Duo P8600 de 2.4Ghz`_ lá de 2008
sem \ `hyper-threading`_ e um monte de sacanagens novas, trabalha
folgado a maior parte do tempo. Ele sofre apenas quando o
`Nepomuk`_ está efetivamente indexando algum documento grande. De resto,
o uso de processamento é bem manso. O boot (raro em \*nix), ocorre em
coisa de 30-40s até estar pronto para uso, incluindo o tempo que levo na
interação com o login.

No geral, vejo o MBP me servindo com alguma folga pelos próximos 4~5
anos se não houver uma falha irrecuperável no hardware. É uma sobrevida
de pelo menos 100% quando comparada ao Mac OS X. Na minha análise de
`ROI`_, isso vale muito a pena.

Mas é claro que nem tudo são flores. O MacBook Pro continua sendo Apple.
O Linux continua sendo Linux. A maioria desses problemas foram
resolvidos ao longo do processo de migração e sobre eles escreverei
aqui. Tem coisas muito legais, úteis não só para o meu caso, mas para
outras pessoas também. Compartilharei.

Mas apesar dos problemas solucionados, três condições já deixaram bem
claro que serão parte do cotidiano. São elas:

#. **Bateria:** 50% menos eficiente que no Mac OS X. Isso é chato e não
   há muito o que fazer com o kernel 3.2. Talvez no 3.4 ou 3.6 isso
   melhore, mas acho pouco provável. O carregador se faz mais presente.
#. **Touchpad:** apesar de boa parte do comportamento dele no Mac OS X
   estar presente no Linux, a incapacidade dele perceber que dois toques
   foram dados a distâncias maiores que algo configurado como "normal"
   para dois dedos juntos ativa o scroll/drag quando eu não quero isso.
   É um problema que só percebemos que existe quando deixamos de ter o
   recurso que o previne. E é chato, muito chato. No entanto,
   acostumável.
#. **Sleep:** não é nem o sleep em si (fechar o display e a máquina
   "dormir"). O retorno dele que é esquisito. Abro a tampa do note, ele
   volta do sleep, fica uns 5~10s e volta a dormir. Aí aperto o botão de
   ligar e só então ele volta definitivamente. Essa condição é só
   chatinha, não chega a ser um incômodo. Como tal, não procurei muito
   sobre o tema, mas deve haver uma solução. Se você que leu até aqui
   sabe um modo de resolver isso, me avise. Serei grato!

No mais, ter a consciência de que estou rodando Linux em um Mac,
maculando tudo o que a Apple quis e quer e que ela é cada vez mais voraz
nesse sentido, me faz muito bem. Subversão tecnológica na veia é o que
liga. Para o que a Apple impõe nos \ `EULAs`_ sobre como usamos seus
produtos, caguei. Um balde.

Concorda comigo? Discorda veementemente? Cabem ponderações ou tem
dúvidas? Os comentários estão aí pra isso. Adoro a beleza das
discussões. Se você entendeu o recado no segundo parágrafo, então será
um prazer e uma honra discutir com você.

**Bônus** (via `+Magno Torres`_): \ `South Park - HUMANCENTiPAD`_
=================================================================

.. youtube:: VobnOUyx2eE
   :width: 500
   :height: 281
   :align: center

.. _aqui: http://google.com/
.. _#mimimi: http://desciclopedia.ws/wiki/Mimimi
.. _Slackware Linux: http://www.slackware.com/
.. _distribuições disponíveis: http://en.wikipedia.org/wiki/List_of_Linux_distributions
.. _Linux: http://en.wikipedia.org/wiki/Linux
.. _MacBook Pro 7,1: http://www.everymac.com/systems/apple/macbook_pro/specs/macbook-pro-core-2-duo-2.4-aluminum-13-mid-2010-unibody-specs.html
.. _Lion: http://en.wikipedia.org/wiki/Mac_OS_X_Lion
.. _Momentus XT: http://www.seagate.com/br/pt/internal-hard-drives/laptop-hard-drives/momentus-xt-hybrid/
.. _funciona: http://macmagazine.com.br/2012/10/25/destaques-e-pontos-abordados-na-conferencia-de-resultados-financeiros-da-apple-para-o-fq4-2012/
.. _multi-tasking: http://en.wikipedia.org/wiki/Computer_multitasking
.. _Intel(r) Core(tm) 2 Duo P8600 de 2.4Ghz: http://ark.intel.com/products/35568/Intel-Core2-Duo-Processor-P8600-3M-Cache-2_40-GHz-1066-MHz-FSB
.. _hyper-threading: http://pt.wikipedia.org/wiki/Hyper-threading
.. _Nepomuk: http://www.vivaolinux.com.br/artigo/Nepomuk-O-que-e-isso
.. _ROI: http://en.wikipedia.org/wiki/Return_on_investment
.. _EULAs: http://en.wikipedia.org/wiki/EULA
.. _+Magno Torres: https://plus.google.com/105840196523966435765
.. _South Park - HUMANCENTiPAD: http://www.southparkstudios.com/full-episodes/s15e01-humancentipad
