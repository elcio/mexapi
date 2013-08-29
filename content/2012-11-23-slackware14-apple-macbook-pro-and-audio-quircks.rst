Slackware14, Apple MacBook Pro and audio quircks
################################################
:date: 2012-11-23 12:53
:author: Deny Dias
:category: Slackware
:tags: KDE, ALSA, MacBook Pro, Linux, microphone, Amarok, audio, Slackware, Skype, Apple
:slug: slackware14-apple-macbook-pro-and-audio

My oh my! Audio was always a wierd thing to configure on Linux. Worst
it is when you are trying to make it work in an Apple MacBook Pro
(`MacBook Pro 7,1`_, Mid-2010, MC374LL/A, A1278 in my very own case).
Yet worst when it comes to Slackware Linux, where this particular area
is not very well documented as many others distributions out there
(don't blame me, Slackers. It's true). When it comes to the audio
matter, `Slackware Documentation Project`_, Linux Questions [`1`_\ ]
[`2`_\ ], `Ubuntu Community Help Wiki`_ and `Google`_ are your friends,
but the best they can do is to give you some clues, `Yoda style`_.

This is a quick'n dirty guide on how to make audio work properly and
with minimal effort on Slackware (and possible others) and MacBook Pro
7,1 (ans possible others too). The bottom line: almost all audio
software infrastructure is already there when you finishes a
Slackware14's fresh install and some configuration is needed to make it
work as it should.

Before we start, two words of advice: 

#. Instead of just "follow the leader", try to understand what you are
   doing, typing, whatever. Don't hit the "comment" button at the end of
   this post with silly questions. I'm experienced enough to now what
   kind of user you are by just reading your words. If you don't tried
   to understand what you're doing before ask, your comment/question is
   going to be lost on the thin wires of the Internet. I'll never reply
   to you. Alas, this is true for anything technical you read from me.
#. As you may have noted at this point, I'm not a natural born English
   speaker. I'm Brazilian and I had never, ever took English classes
   beyond the high school (which are the most basic classes in Brazil,
   for kids). I also don't like to use an automated translator to help
   me write in english because they feel, err, synthethic. If my English
   sounds kinda redneck (which I'm, tks for ask) and it does bothers
   you, feel free to positively criticize me. If you hit the "comment"
   button just to let me know that my "English is bad", don't bother to.
   I know that already. So, just fuck off while I keep writing the
   articles that I think may help a broader audience with my bad
   English, which I think is just good enough to transmit an idea, which
   in turns is the most basic concept on communication.

Across this article there will be specific Apple MacBook Pro 7,1
[MBP71] tips and most general [G] ones. The general tips could apply to
Slackware and other Linux flavors also. I'll let you know the difference
during the reading by using the aforementioned tags.


Step 1 [MBP71] : Just after install finishes, set the proper kernel module configuration
========================================================================================

.. code:: bash

    $ sudo vi /etc/modprobe.d/alsa-base.conf
      options snd-hda-intel model=mbp55

Reboot your system. Sorry.

Step 2 [G]: Set ALSA mixer and store its settings
=================================================

Run ``alsamixer`` on your term. The first screen shows the playback
controls. Unmute all of them but S/PDIF (unless you acutally have
optical audio cables connected to your receiver or want a red light
coming out of your headphone jack on MacBook Pro). Set the volumes to
the max.

Hit ``tab`` (or ``F4``) to go to capture settings. If ``Capture`` reads
``-------`` above it, it's muted. Select it with arrow keys (it turns red
when selected) and hit space to unmute it (should read ``CAPTURE`` instead
of dashes).

Now run the command bellow to store your settings so they come alive
between reboots. Note to run it as user ($), not as root (#), as you
want to store the mixers settings for your user.

.. code:: console

    $ /usr/sbin/alsactl store

Step 3 [G]: Avoid KMix to mess with your ALSA mixer setting
===========================================================

When you store the mixer settings with ``alsactl store``, the expected
behavior when you reboot is to have the exact same settings that you
manually stored before, loaded again. Some distros stores ALSA mixer
settings upon shutdown/reboot (i.e Arch), but Slackware seems to not do
it. If you'd like, it's easy enough to add the ``/usr/sbin/alsactl store`` 
command to your ``~/.bash\_logout`` script so it
make this happen automatically. It didn't bother me, so I don't.

For the ones that uses KDE as their window manager (I do), KMix has a
`bug`_ (fixed on KDE 4.9.0, Slackware14's is 4.8.5) on session restore
feature that prevents it to "remember" the levels from its last session.
The most annoyng part is that you have to remember to always open KMix
before a video call on Gtalk, Skype and others, because the capture
devices are going to be always muted and set to 0.

There's an easy `workaround`_ for this, though. Go to ``KMix > Settings
> Configure KMix``  and uncheck ``Restore volumes upon login``.

Step 4 [MBP71]: Fix Apple shit on microphone audio routing
==========================================================

.. class:: warning label

Note

This is for Skype only. Gtalk is smart enough to fix this
internally. Tks, Google devs!

Generally speaking, notebook microphones are mono devices. They
capture audio at one channel only instead the two for the stereo sound.
That's just fine from the engineering perspective for the kind of
application that a built-in notebook mic has.

When it comes to audio, there's a *de facto* `standard`_: mono audio
sources, when connected to stereo devices, have the live channel (the
one that carries the signal) as the left channel while the right channel
is unused. Right? Not to Apple, you bitch!

Apple did us the favor to reverse this connection on their notebooks
and one could have very interesting times wondering what is happening to
the microphone audio capture (as I did). To solve this shit (many thanks
to `Arch Linux Skype Wiki page`_ maintainers to give me the clues for
this):

.. code:: bash

    $ vi ~/.asoundrc
      pcm.skype {
        type route
        slave.pcm "hw:0,0"
        slave.channels 2
        ttable.0.1 4
        ttable.1.0 0
      }

After save the file, logout and login from X, go to ``Skype > Options >
Audio > Microphone`` and select the new device in the list: ``skype (route)``.
Make an Skype call to the echo test service (echo123) to check that's
working. If it's not, double check steps 2 and 3. Done. Your voice
spreading to the world. Talk soft, smart things.

Step 5 [G]: Dumb Amarok
=======================

Finally, Amarok (the default playlist based music player in KDE) do not
work out of the box on Slackware14. Thanks to `Itaman Cavalcanti`_, who
pointed out a solution for this issue, here's how to make Amarok plays
your tunes.

First, download OpenSUSE's `gstreamer-0\_10-plugins-fluendo\_mp3`_ rpm
package. Note to download the right file for your CPU architecture (i586
for 32bit, X86\_64 for 64bit). Then issue on terminal:

.. code:: console

    $ rpm2txz gstreamer-0_10-plugins-fluendo_mp3-[VERSION].[ARCH].rpm
    $ sudo /sbin/installpkg gstreamer-0_10-plugins-fluendo_mp3-[VERSION].[ARCH].txz

Of course, ``[VERSION]`` and ``[ARCH]`` must be replaced with your needs.
Almost done, lets make Amarok play MPEG-4 AAC audio files (I came from
a Mac, so I have a bunch of these around) and make it able to transcode
things:

.. code:: console

    $ sbopkg -i "gst-plugins-ugly gst-plugins-bad gst-ffmpeg"

Restart Amarok and you're good to go.

Wrap up
=======

From the end user perspective, we've learned here how to make
Slackware14 be a good guy when it comes to audio. We also learned how to
properly configure audio in Slacware14 to the Apple's Macbook Pro 7,1
(Mid-2010) specifics wierdness.

Doubts, comments? The channel is open. Be my guest.

**Bonus**: Paloma Faith - Do You Want the Truth or Something Beautiful (the roots version)
==========================================================================================

.. youtube:: TskmeMoUh-8
   :width: 500
   :height: 281
   :align: center

.. _MacBook Pro 7,1: http://www.everymac.com/systems/apple/macbook_pro/specs/macbook-pro-core-2-duo-2.4-aluminum-13-mid-2010-unibody-specs.html
.. _Slackware Documentation Project: http://docs.slackware.com/howtos:hardware:audio_and_snd-hda-intel
.. _1: http://www.linuxquestions.org/questions/linux-hardware-18/slackware-13-sound-problem-791270/
.. _2: http://www.linuxquestions.org/questions/slackware-14/microphone-doesnt-record-on-slackware-14-0-a-4175437726/
.. _Ubuntu Community Help Wiki: https://help.ubuntu.com/community/MacBookPro7-1/Maverick
.. _Google: http://www.google.com/
.. _Yoda style: http://www.flero.net/unlikely-saying-that-you-would-not-find-soda-saying/
.. _bug: https://bugs.kde.org/show_bug.cgi?id=293043
.. _workaround: https://bugs.kde.org/show_bug.cgi?id=293043#c22
.. _standard: http://en.wikipedia.org/wiki/Phone_connector_(audio)#Switch_contacts
.. _Arch Linux Skype Wiki page: https://wiki.archlinux.org/index.php/Skype
.. _Itaman Cavalcanti: http://itaman.blogspot.com.br/2012/10/pequeno-comentario-sobre-o-slackware.html
.. _gstreamer-0\_10-plugins-fluendo\_mp3: http://pkgs.org/download/gstreamer-0_10-plugins-fluendo_mp3
