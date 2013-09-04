Migrei meu blog: o ambiente de desenvolvimento
##############################################
:date: 2013-09-03 23:59:52
:author: Deny Dias
:category: Development
:tags: pelican, python, development, web, open source, blog, static html, virtualenv, virtualenvwrapper, apache, pip, slackware
:slug: migrei-meu-blog-o-ambiente-de-desenvolvimento
:parts: migrei-meu-blog

No artigo anterior, expus as razões que me levaram a migrar do insosso Blogger para uma plataforma completamente nova (ao menos para mim): o `Pelican`_. Agora vou contar como isso se deu do ponto de vista mais técnico, de desenvolvimento para a web mesmo.

Não vou tratar dos aspectos básicos deste ambiente. Há muitos bons artigos sobre como instalar e sair usando o Pelican por aí. Só para citar alguns:

#. `Getting Started`_, documentação oficial do Pelican, em inglês.
#. `How I built this website, using Pelican`_, por Duncan Lock, em inglês.
#. `Pelican and Github Pages`_, por Martin Brochhaus, em inglês.
#. `Tutorial: Criando sites estáticos com Python e Pelican`_, por Rodrigo Amaral, em português.

Também não vou escrever esse texto em inglês, como costumo fazer com os artigos técnicos que publico. Como visto na lista acima, há bastante conteúdo em inglês disponível sobre o tema (e se procurar tem muito mais). Por outro lado, há bem pouco conteúdo `em português`_.

O que vou abordar aqui são aspectos como: 

#. Uso do `virtualenv + virtualenvwrapper`_ no contexto do Pelican;
#. Possíveis `problemas e automação das dependências`_;
#. Configuração de um ambiente de desenvolvimento `usando o webserver local`_;
#. Customização de um tema para as suas necessidades;
#. Workflow cotidiano, de um novo post ao GitHub;
#. Alguns aspectos sobre o licenciamento do conteúdo que produzo.

.. class:: warning label

Atenção!!!

O OS que uso todo o dia é o `Slackware Linux`_. Logo é evidente que a maioria dos comandos, caminhos e configurações que indico são apropriadas a essa distribuição. Porém não deve ser problema para quem conhece um pouco de \*nix adaptar o que for necessário para o seu ambiente. Usa Windows? Morra!

Outro aspecto importante da minha abordagem: tendo como base o conhecimento que possuo das ferramentas no momento em que as uso, procuro sempre utilizá-las do modo mais simples e elegante possível, sendo que por simplicidade eu entendo como um ambiente cujos pontos de falha sejam minimizados, e por elegância eu entendo como um workflow prático e facilmente reproduzível.

Beleza? Então 'râmulá'!

Virtualenv + Virtualenvwrapper
==============================

Uma das ferramentas mais legais do Python para manter ambientes isolados é o `virtualenv`_. E o addon imprescindível para quem usa o virtualenv é o `virtualenvwrapper`_. Do site do wrapper:

  virtualenvwrapper is a set of extensions to Ian Bicking’s virtualenv tool. The extensions include wrappers for creating and deleting virtual environments and otherwise managing your development workflow, making it easier to work on more than one project at a time without introducing conflicts in their dependencies.

Instalar os dois está além do escopo deste artigo, mas os manuais estão aí nos links de cada um. O que importa aqui é como usá-los no contexto do Pelican.

Depois de instalar os dois e o ``pip`` (claro), a coisa toda é tão simples como:

.. code-block:: console

  $ mkvirtualenv pelican
  $ workon meusite
  (meusite)$ pip install pelican

A partir deste ponto, tudo o que você fizer no Python estará confinado ao ambiente ``meusite``. Se fizer uma besteira qualquer e quiser começar novamente, basta criar outro ambiente e, se quiser, apagar o antigo.

.. code-block:: console

  $ rmvirtualenv meusite

Rápido, rasteiro, elegante.

Problemas e Automação das Dependências
======================================

Eu enfrentei alguns problemas com as dependências do Pelican no Slackware. A documentação diz que ele instala essas dependências automaticamente, mas não foi o que ocorreu comigo. Não sei se por questões específicas do Slackware ou do próprio ``pip``, que não 'sabe' que a versão mais atual do ``pytz`` é a ``2013b``. Por isso cabe um adendo para os que enfrentarem problemas semelhantes.

Para instalar as dependências do Pelican, uma vez dentro do virtualenv apropriado, rode o comando:

.. code-block:: console

  (meusite)$ pip install feedgenerator jinja2 pygments docutils pytz==2013b blinker unidecode typogrify pelican

Esta é a instalação mais básica do Pelican. No entanto, para conseguir tudo que eu fiz aqui no MexApi, tive que instalar algumas outras coisas. Boa parte do que instalei é bastante genérico em relação aos recursos mais úteis do Pelican, dos plugins mais importantes e os temas mais cheios de firulas (o tema básico roda bem com a instalação padrão). Se você pretende que seu blog tenha alguns recursos mais legais, para facilitar a sua e a minha vida (no caso de uma reinstalação do ambiente), eu disponibilizei um `arquivo`_ que contém todos os módulos instalados em meu ambiente. Para instalar tudo em um tapa só:

.. code-block:: console

  (meusite)$ pip install -r stable-req.txt

Usando o Webserver Local
========================

O Pelican é legal. Ele vem com um ``Makefile`` que, dentre os muitos recursos legais que há nele, permite que você rode um webserver para fazer o preview dos seus artigos ou desenvolver seus temas. Deste modo, basta fazer isso:

.. code-block:: console

  $ make devserver

Legal, né? A partir daí, basta digitar ``http://localhost:8000/`` e seu site estará lá.

Mas peraí! Estamos num \*nix e muito provavelmente temos um servidor web instalado e em execução. E muito provavelmente é um Apache. Por quê não usá-lo? Afinal, se eu rodo o ``make devserver`` do Pelican ele vai comer uma tela de terminal com a saída das requisições HTTP, inúteis neste caso, abrir um serviço completamente redundante em minha máquina e não estará lá o tempo todo rodando. Odeio as redundâncias burras (aquelas que desperdiçam recursos), e essa é uma delas. Então, vamos usar nosso Apache local para fazer isso.

Primeiro, configure seu ``/etc/hosts/`` desta forma:

.. code-block:: bash

  127.0.0.1       localhost meusite.local

O alias (apelido) ``meusite.local`` pode ser qualquer coisa que te agrade. Esse é o endereço que você vai usar para acessar o seu site localmente, portanto ele pode ter o nome que você quiser. Só lembre-se desse nome para daqui a pouco. Salve e teste.

.. code-block:: console

  $ ping -c3 meusite.local
  PING localhost (127.0.0.1) 56(84) bytes of data.
  64 bytes from localhost (127.0.0.1): icmp_req=1 ttl=64 time=0.045 ms
  64 bytes from localhost (127.0.0.1): icmp_req=2 ttl=64 time=0.095 ms
  64 bytes from localhost (127.0.0.1): icmp_req=3 ttl=64 time=0.092 ms

  --- localhost ping statistics ---
  3 packets transmitted, 3 received, 0% packet loss, time 1999ms
  rtt min/avg/max/mdev = 0.045/0.077/0.095/0.024 ms

Jóia! Nosso servidor agora responde pelo seu novo nome. Note que ele substituiu sozinho o ``meusite.local`` por ``localhost``, que é o nome 'de verdade' do endereço 127.0.0.1 (conhecido como *loopback*).

Agora vamos fazer uma '*gambiarra*' (in english: trick) no diretório de saída do Pelican para que ele gere o site estático num lugar que o Apache 'conhece'. Vá para o diretório onde vc instalou o Pelican e rode:

.. code-block:: console

  $ sudo /srv/httpd/htdocs/meusite output && sudo chmod meuusuário:users /srv/httpd/htdocs/meusite
  $ rm output
  $ ln -s /srv/httpd/htdocs/meusite output

E depois edite o ``Makefile`` do Pelican:

.. code-block:: make

  OUTPUTDIR=/srv/httpd/htdocs/mexapi

O que fizemos aqui é bastante óbvio, mas cabe explicar assim mesmo. Primeiro criamos um diretório no ``DocumentRoot`` do Apache. Depois apagamos o diretório de saída do Pelican e o 'simbolincamos' (sic) em seguida ao diretório do Apache. Depois instruímos o ``Makefile`` a gravar os arquivos estáticos gerados no diretório que o Apache enxerga. Tudo isso vai fazer mais sentido daqui a pouco.

Agora precisamos ensinar ao Apache que quando acessarmos a URL ``http://meusite.local/`` (note que não tem a porta), ele precisa nos mostrar nosso super-ultra-mega-blaster-site-gerado-pelo-Pelican. Para isso vamos usar um recurso do Apache conhecido como ``VirtualHost``.

Primeiro, edite seu ``/etc/httpd/extra/httpd-vhosts.conf`` e coloque isso no final (ou em outro lugar, se for o seu caso):

.. code-block:: apache

  # main server
  <VirtualHost *:80>
      ServerName localhost
      DocumentRoot /srv/httpd/htdocs
  </VirtualHost>

  # mexapi server
  <VirtualHost *:80>
      ServerName  mexapi.local
      DocumentRoot /srv/httpd/htdocs/mexapi/
  </VirtualHost>

Depois, edite ``/etc/httpd/httpd.conf``, por volta da linha 484:

.. code-block:: apache

  # Virtual hosts
  Include /etc/httpd/extra/httpd-vhosts.conf

Note que se você usa Debian, Ubuntu, Mac OS X ou outras distros, suas configurações podem ser bem diferentes dessa. Veja a documentação da sua distro para ver como fazer a mesma coisa. Te garanto que não é difícil.

Configurado o ``VirtualHost``, basta reiniciar o Apache:

.. code-block:: console

  $ sudo /etc/rc.d/rc.httpd restart

Agora acesse ``http://localhost/`` e ``http://meusite.local/`` e veja a diferença. Na primeira URL, a página padrão do Apache na sua distro (no Slackware é simplesmente '**It works!**'). Na segunda, seu site Pelican (claro, se você já gerou alguma coisa. Se não, tente ``make html``). 

Well done, bro! Agora você não precisa mais rodar o webserver do Pelican para ver o seu site (só o ``make html``, ``make publish`` ou ``make regenerate``) e pode acessá-lo a qualquer hora. Se o seu firewall permite isso, ou se não há firewall algum rodando, pode até acessar o seu site de outro computador em sua rede local ou de seu smartphone ou tablet (o que eu faço para testar o tema em dispositivos móveis). Você vai precisar editar o ``hosts`` dos dispositivos para o IP do seu servidor local, mas isso eu deixo como exercício para o leitor.

Hoje vou parar por aqui porque essa parte já rendeu muito. Depois escrevo a terceira e última parte da série. Se escrevi alguma merda, comenta e que eu corrijo.

**Bônus**: Nancy Sinatra - Sugar Town 
=====================================

.. youtube:: pjsh2j7W6Bo
   :width: 500
   :height: 281
   :align: center

.. _Pelican: http://docs.getpelican.com/en/3.2/
.. _Getting Started: http://docs.getpelican.com/en/3.2/getting_started.html
.. _`How I built this website, using Pelican`: http://duncanlock.net/blog/2013/05/17/how-i-built-this-website-using-pelican-part-1-setup/
.. _Pelican and Github Pages: http://martinbrochhaus.com/pelican2.html
.. _`Tutorial: Criando sites estáticos com Python e Pelican`: http://rodrigoamaral.net/2013/07/16/tutorial-criando-sites-estaticos-com-python-e-pelican/
.. _em português: http://goo.gl/mujkou
.. _Slackware Linux: /2012/11/subversao-tecnologica-do-mac-os-x-para.html#.UiZwQOdDszs
.. _virtualenv: http://www.virtualenv.org/en/latest/
.. _virtualenvwrapper: http://virtualenvwrapper.readthedocs.org/en/latest/
.. _arquivo: https://github.com/denydias/mexapi/blob/master/stable-req.txt