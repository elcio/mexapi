Migrei meu blog: do insosso Blogger para a poderosa dupla Pelican/GitHub
########################################################################
:date: 2013-08-30 11:12:46
:author: Deny Dias
:category: Development
:tags: pelican, python, development, web, open source, blog, static html
:slug: migrei-meu-blog-do-insosso-blogger-para-a-poderosa-dupla
:parts: migrei-meu-blog

My oh my! Migrei meu blog! E estou felicíssimo com o resultado!

Primeiro porque isso me deu a oportunidade de aprender para caralho sobre `Python`_, as firulas mais recentes do HTML/CSS/JS, linguagens de marcação até então obscuras para mim (`reStructuredText`_ e `AsciiDoc`_) e mais muitas, muitas outras coisas. Segundo porque quando eu criei meu blog, em novembro do ano passado, optei pelo Blogger como algo temporário, para colocar no ar rápido, com o intuito de migrar para algo mais *geeky* e que faça o meu estilo, mas que desde então havia deixado de lado, agora está feito. Terceiro porque com isso descobri que a web está voltando, depois de muitas `idas e vindas`_, a ser um ambiente civilizado no que diz respeito aos padrões e que tem uma galera porreta que já descorrelacionou conteúdo dinâmico dos stacks do tipo `LAMP`_. Quarto porque é um projeto estritamente pessoal e que, como tal, me proprociona muito prazer. E quinto, last but not least, tudo, cedo ou tarde, muda.

Mas deixa eu contar como foi isso.

Inception
=========

Out of the fucking blue, há umas duas semanas eu estava lendo um `post`_ do AlienBOB sobre os novos pacotes do KDE 4.11 para o Slackware -current. No final deste post, o Eric Hameleers (vulgo AlienBOB), pedia o voto do leitor para uma competição de blogs, a "`Best Personal Linux or FOSS Blog Competition`_". Como eu acho o blog dele muio jóia, eu fui lá votar. Voto dado, fui pra home do FOSS Force e fui ler outras coisas. Não me lembro mais exatamente como, mas a partir do FOSS Force acabei de deparando com um outro post, em outro blog, com uma `análise da taxa de desenvolvimento do branch 3.10 do kernel do Linux`_. O artigo em si é legal, mas curti também o visual desse blog, de propriedade do Greg Kroah-Hartman, que é atualmente o mantenedor do branch estável do kernel do Linux. E quando fui olhar qual a plataforma ele usava para blogar, BAMMM! Octopress! Epa! Octopress? Que porra é essa? Não é Wordpress? Não é MovableType? Não é Blogger? Que diacho é isso? E fui atrás de saber o que era. Eis que leio:

  Octopress. A blogging framework for hackers.
  
  -- Octopress Website

Saca a idéia plantada pelos agentes no filme "A Origem" (Inception)? Pois é. Foi o que essa frase "A blogging framework for hackers" fez comigo. E para piorar, no mesmo site, ainda li o seguinte:

  Octopress is a framework designed by Brandon Mathis for Jekyll, the blog aware static site generator powering Github Pages.
  
  -- Octopress Website
  
Como assim? GitHub Pages? Fuck! O GitHub não é um serviço para desenvolvedores do mundo afora colocarem seus repositórios git na nuvem? Bom, é. Mas como eu `descobri`_ em seguida, não é só para isso que o GitHub nos serve.

E aí é onde eu começo a preencher a segunda motivação que eu citei lá em cima. E o que era do jeito que você vê na imagem abaixo (guardada para a posteridade) ficou do jeito que você vê agora. Não sei você, mas eu adorei.

.. figure:: /static/images/mexapi_blogger.png

        "Meus textos continuam os mesmos, mas os meus cabelos..."

In for a penny, in for a pound
==============================

O `Octopress`_ é uma aplicação feita em Ruby que come arquivos em liguagens de marcação simplificadas, bate no liquidificador com um tema  feito em Ruby/HTML/CSS/JS e vomita HTML estático. Meu, HTML estático! Eu fazia isso em 2003 com o `Mambo`_, que sozinho não gerava HTML estático, mas eu e um mau elemento (a sério) do passado adaptamos para fazer justamente isso usando os `SSI`_ do Apache.

Eu cheguei a baixar, instalar, configurar e publicar alguns testes usando o Octopress no GH-Pages. Super bacaninha, mesmo, de verdade. Mas ele tem um defeito pra mim: é em Ruby. Assim, sem querer ofender nenhum dev Ruby por aí, é apenas a minha humilde opinião, mas eu penso que o Ruby (e outras) está para o Python (e outras) assim como o `Lego Mindstorms`_ está para o `Arduino`_. Um é um brinquedo legal pacas e que tem muita gente boa criando coisas legais enquanto o outro pode ser brinquedo se quem está criando quiser, mas vai muito além disso.

E aí comecei a futucar a internet para averiguar minhas opções. Fiquei estarrecido com a quantidade de `opções`_ e que isso está sendo feito desde 2002, mas que somente há pouco o movimento começou a ganhar momentum entre os desenvolvedores.

Nessa busca encontrei o `Pelican`_:

  Pelican is a static site generator, written in Python.

    #. Write your content directly with your editor of choice (vim!) in reStructuredText, Markdown, or AsciiDoc formats
    #. Includes a simple CLI tool to (re)generate your site
    #. Easy to interface with distributed version control systems and web hooks
    #. Completely static output is easy to host anywhere

Hummm... Python, Markdown (que eu já conhecia), CLI, VCS, estático, em qualquer lugar. Lendo a documentação, descobri que os recursos eram plenos, uma boa variedade de plugins, bons temas para começar e a integração com o GitHub bem elaborada. Bem, o Pelican parecia a escolha certa. E foi. Tanto que é o Pelican que gera todo este blog que você lê agora.

Bom, hoje eu cansei de escrever. Em outra parte desse artigo (hell yeah! I've got multi-parts!) eu vou contar como se deram as partes mais técnicas da coisa toda.

Ah, e se quiser, comenta aí! ;)

**Bônus**: Computer Magic - The End of Time
===========================================

.. youtube:: 1dwNIuN9LN8
   :width: 500
   :height: 281
   :align: center

.. _Python: http://www.python.org/
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _AsciiDoc: http://www.methods.co.nz/asciidoc/
.. _idas e vindas: http://en.wikipedia.org/wiki/Browser_wars
.. _LAMP: http://en.wikipedia.org/wiki/LAMP_(software_bundle)
.. _post: http://alien.slackbook.org/blog/kde-4-11-is-out/
.. _Best Personal Linux or FOSS Blog Competition: http://fossforce.com/2013/08/who-will-be-best-personal-linux-or-foss-blog/
.. _análise da taxa de desenvolvimento do branch 3.10 do kernel do Linux: http://www.kroah.com/log/blog/2013/07/01/3-dot-10-kernel-development-rate/
.. _descobri: http://pages.github.com/
.. _Octopress: http://octopress.org/
.. _Mambo: http://en.wikipedia.org/wiki/Mambo_(software)
.. _SSI: http://httpd.apache.org/docs/2.2/howto/ssi.html
.. _Lego Mindstorms: http://mindstorms.lego.com/en-us/default.aspx
.. _Arduino: http://www.arduino.cc/
.. _opções: http://siliconangle.com/blog/2012/03/20/5-minimalist-static-html-blog-generators-to-check-out/
.. _Pelican: http://docs.getpelican.com/en/3.2/