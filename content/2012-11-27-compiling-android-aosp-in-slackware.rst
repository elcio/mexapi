Compiling Android (AOSP) in Slackware
#####################################
:date: 2012-11-27 01:07
:author: Deny Dias
:category: Slackware
:tags: java, libGL.so, Switch.pm, Android, Slackware, JDK5, patch, perl, AOSP, JDK6, build, JDK7, compile
:slug: compiling-android-aosp-in-slackware

So you just got a fresh new `AOSP`_ (Android Open Source Project)
environment to your Slackware box and  get ready to do your droid's
compile party. Not that fast, my good friend. Not that fast. There are
two minor adjustments that you should do before hit ``make -j4``. Here
they are. Also check out the addendum at the end (if it applies to you,
of course).

AOSP requires Java 6 or 5 SDK
=============================

If you are running a fresh install of Slackware14, chances are that you
have installed Java SDK from Slackbuild's package, which is `JDK 7u9`_
at the time of this writing.

AOSP documentation isn't perfectly clear on what JDK version one should
have. It says only:

    The Sun JDK is no longer in Ubuntu's main package repository. In
    order to download it, you need to add the appropriate repository and
    indicate to the system which JDK should be used.
    
    Java 6: for Gingerbread and newer
    
    Java 5: for Froyo and older

    -- `AOSP, Download and Building chapter`_

This statement makes very clear that for Froyo and older (<2.2) you
must stick with JDK5. But, at least to my understanding, it's not clear
if I can or can not use JDK7 for Gingerbread and newer (>2.3). So, the
answer is no. I can't. I get this from compile time with JDK7:

.. code:: console

    Checking build tools versions...
    ************************************************************
    You are attempting to build with the incorrect versionof java.
    
    Your version is: java version "1.7.0_09".
    The correct version is: Java SE 1.6.
    
    Please follow the machine setup instructions at
        https://source.android.com/source/download.html
    ************************************************************

I should have JDK6 to compile anything Android after Gingerbread. So,
let's do it.

First, `download`_ the most recent JDK6 from Oracle's website. At the
time of this writing, it is JDK 6u37. Then:

.. code:: console

    $ cd [path_where_jdk6_is]
    $ ./jdk-6u37-linux-x64.bin
    $ sudo mv jdk1.6.0_37 /usr/lib64/jdk1.6.0_37
    $ sudo chown -R root:root /usr/lib64/jdk1.6.0_37
    $ sudo rm -f /usr/lib64/jdk1.7.0_09
    $ sudo mv /usr/lib64/java /usr/lib64/jdk1.7.0_09
    $ sudo ln -s /usr/lib64/java /usr/lib64/jdk1.6.0_37

Three words of advice:

#. Note that my system is 64bit. If you are on a 32bit system,
   `download`_ ``jdk-6u37-linux-i586.bin`` instead and change the paths to
   ``/usr/lib``, not ``/usr/lib64``.
#. The above commands completely disables JDK7 on your system. You can
   always re-enable it by reverting the symbolic link ``/usr/lib/java`` to
   ``/usr/lib64/jdk1.7.0\_09``. Just remember: to compile AOSP, JDK6 or JDK5
   are mandatory (depending on your AOSP target version).
#. So you can use JDK5, the steps are pretty much the same. In that
   case, you need to
   `download <http://www.oracle.com/technetwork/java/javasebusiness/downloads/java-archive-downloads-javase5-419410.html#jdk-1.5.0_22-oth-JPR>`__
   JDK5 from Oracle's website instead of JDK6.

Your JDK environment is done. Let's proceed with perl.

Can't locate Switch.pm
======================

Slackware14's perl version is 5.16.1. Many newer distributions out there
uses this perl version too. That should not be a problem at all, unless
you are trying to compile AOSP. It requires a perl library called
'Switch.pm' that is deprecated. The last perl version that came with
Script.pm was 5.14.x, as you can see on this `issue`_ from Android's
Google Code issue tracking. If you try to compile AOSP against your perl
>5.15, you are going to get this after a long waiting:

.. code:: console

    Can't locate Switch.pm in @INC (@INC contains: /usr/local/lib64/perl5 /usr/local/share/perl5 /usr/lib64/perl5/vendor_perl /usr/share/perl5/vendor_perl /usr/lib64/perl5 /usr/share/perl5 .) at external/webkit/Source/WebCore/make-hash-tools.pl line 23.

That's very frustrating, indeed.

So, downgrade perl, one might think. WRONG! BHHHEEEHHHNNN!!!! Downgrade
is difficult and poses some security issues you don't want to deal with.
The correct and elegant approach to this is to patch. To patch AOSP
source is easy, reliable and just works. So, let's do it.

Thanks to xoomdev, a user/dev at rootzwiki forum, we got a `patch`_ that
fix this issue in the elegant way. To make it easy for the reader, I'll
paste the patch here, but the kudos are all to xoomdev.

.. code:: diff

    diff --git a/Source/WebCore/make-hash-tools.pl b/Source/WebCore/make-hash-tools.pl
    index 37639eb..2968beb 100644
    --- a/Source/WebCore/make-hash-tools.pl
    +++ b/Source/WebCore/make-hash-tools.pl
    @@ -20,7 +20,8 @@
    #   Boston, MA 02110-1301, USA.

    use strict;
    -use Switch;
    +# use Switch;
    +use feature qw(switch);
    use File::Basename;

    my $outdir = $ARGV[0];
    @@ -28,9 +29,9 @@ shift;
    my $option = basename($ARGV[0],".gperf");


    -switch ($option) {
    +given ($option) {

    -case "DocTypeStrings" {
    +when ("DocTypeStrings") {

        my $docTypeStringsGenerated    = "$outdir/DocTypeStrings.cpp";
        my $docTypeStringsGperf        = $ARGV[0];
    @@ -40,7 +41,7 @@ case "DocTypeStrings" {

    } # case "DocTypeStrings"

    -case "ColorData" {
    +when ("ColorData") {

        my $colorDataGenerated         = "$outdir/ColorData.cpp";
        my $colorDataGperf             = $ARGV[0];

Copy the code above, paste it to
``[AOSP\_HOME]/external/webkit/Source/WebCore/make-hash-tools.pl.patch``,
then:

.. code:: console

    $ cd [AOSP_HOME]/external/webkit/Source/WebCore/$ cp -p make-hash-tools.pl make-hash-tools.pl.orig$ patch --verbose < make-hash-tools.pl.patch

And you're done. After that, you can go to you your ``[AOSP\_HOME]``, hit
``make -j4``, wait a lot for the compile tasks finishes and, at the end,
just run:

.. code:: console

    $ emulator

Addendum: Failed to load libGL.so
=================================

Well, in fact there is another issue with emulator runtime. It complains
about libGL.so not found. This one is an easy fix:

.. code:: console

    $ cd /usr/lib64
    $ sudo ln -s libGL.so.1 libGL.so

Comments? Doubts? Something seems wrong to you? Fill in the box bellow
and drop me a line.

[Nov 28 05:53:37 2012] Update: Shell preparation for AOSP
=========================================================

It just occurred to me that when I close the terminal where I've build
AOSP and ran emulator, all the environment variables needed to run it
again has gone. Set it up again is a matter of two or three commands,
but I don't want to type then anytime I need AOSP up and running. So I
just created a bash alias like this:

.. code:: bash

    alias droidprep='cd ~/Dev/adt-bundle-linux/aosp;. build/envsetup.sh;lunch full-eng;env|grep ANDROID'

From now on, when I want to run Android on my system or build something
on it, I just hit on any terminal:

.. code:: console

    $ droidprep
    $ emulator

This is a per terminal session setting. If you do this in one terminal
session, Android environment is going to run on that session only. If
you want this to be a user wide and make it work on any terminal
session, the best place to do it is from your ``~/.bashrc``
(for interactive, non login shells) or ``~/.bash_profile`` (for
interactive, login shells). See more details in ``man bash``, ``INVOCATION``
chapter.

**Bonus**: Radiohead - Paranoid Android
=======================================

.. youtube:: sPLEbAVjiLA
   :width: 500
   :height: 281
   :align: center

.. _AOSP: http://source.android.com/
.. _JDK 7u9: http://slackbuilds.org/repository/14.0/development/jdk/
.. _AOSP, Download and Building chapter: http://source.android.com/source/initializing.html#installing-the-jdk
.. _download: http://www.oracle.com/technetwork/java/javase/downloads/jdk6u37-downloads-1859587.html
.. _issue: http://code.google.com/p/android/issues/detail?id=22231
.. _patch: http://rootzwiki.com/topic/8037-compile-android-on-fedora-1516-by-xoomdev/page__st__10#entry738111
