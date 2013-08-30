Keeping Slackware -current, multilib up-to-date kinda automatically
###################################################################
:date: 2013-04-24 01:32
:author: Deny Dias
:category: Slackware
:tags: development, slackext, Linux, software, multilib, update, Slackware, -current
:slug: keeping-slackware64-current-multilib-up

Wow! That's a lot of unsupported stuff in just one title: ``-current`` and
``multilib``.

As many of you out there, it took just a couple of weeks so I jump
from the safe, supported side to the unsupported one with -current and
multilib setup. I'll not get into the details of what -current and
multilib is to the Slackware64 context here. There are plenty of lecture
to this already.

Once you have an Slackware64 pointed to the -current tree, this means
at least some dozens of minutes every month keeping it up to date. Some
of those could make you to spend a couple hours. Well, you're on
Slackware's bleeding edge. So don't complain. At least we have slackpkg
to help with the task.

The same isn't 100% true for AlienBOB's multilib packages. And before
you ask: yes, I'm aware of `Multilibpkg`_. It's a hell of a tool, but I
just don't like all its bells and whistles. From my humble opinion,
Multilibpkg adds an unnecessary complexity layer. I like it `KISS`_.

`LQ`_ users also have pointed out many ways to keep a multilib setup
updated over the time. Even AlienBOB himself has a very good `wiki`_
about the housekeeping process. The 'feature' all those methods share
are that they are almost in its entirety by hand. I don't like it by
hand... at least not at computers.

So decided to write an script to handle this: `slackext`_.

It does everything needed to a good and reliable Slackware64 multilib
update:

#. Create cache directories on demand;
#. Download required files from the repository (by mirroring them, tks
   to `lftp`_);
#. Check for ``MD5`` and ``GPG`` signatures (only if provided by the package
   maintainer);
#. Install new packages or upgrade the ones already installed.

Besides, it does one thing I could not find either on Multilibpkg nor
any other script out there: it works with any repository that provides
Slackwares ``tgz/txz`` packages.

So, to bring my multilib setup to the latest packages, I just:

.. code:: console

    # slackext http://taper.alienbase.nl/mirrors/people/alien/multilib/current/

I want to watch a movie! So I fire:

.. code:: console

    # slackext http://slackware.org.uk/slaxbmc/14.0/slaxbmc64-14.0/slackware64/xbc/
    # slackext http://slackware.org.uk/slaxbmc/14.0/slaxbmc64-14.0/updates/frodo/

AlienBOB (does he sleep?!?) releases a new openjdk. No problem:

.. code:: console

    # slackext http://taper.alienbase.nl/mirrors/people/alien/slackbuilds/openjdk/pkg64/14.0/

Do you live outside US and want all those fancy codecs that those stupid
US patent laws don't let you? Cool, so type:

.. code:: console

    # slackext http://slackware.org.uk/people/alien/restricted_slackbuilds/vlc/pkg64/14.0/

There are lots of Slackware third party package maintainers out there
which delivers them in either ``tgz`` or ``txz`` formats. If you can find an URL
to those packages, you can use ``slacktext`` to easily download, check,
install and keep them up to the date.

Well, as you can see, ``slackext`` is smart enough to keep your multilib
packages in shape as well as all that aliens stuff you install on your
Slackware64 -current multilib. Unsupported my ass!

**Bonus**: Feeling Good, Nina Simone
====================================

.. youtube:: CJA69C6SlRk
   :width: 500
   :height: 281
   :align: center

.. _Multilibpkg: http://multilibpkg.sourceforge.net/
.. _KISS: http://en.wikipedia.org/wiki/KISS_principle
.. _LQ: https://www.google.com.br/search?q=site:linuxquestions.org+slackware+multilib+update
.. _wiki: http://docs.slackware.com/howtos:slackware_admin:systemupgrade#multilib_considerations
.. _slackext: https://github.com/denydias/slackext
.. _lftp: http://lftp.yar.ru/
