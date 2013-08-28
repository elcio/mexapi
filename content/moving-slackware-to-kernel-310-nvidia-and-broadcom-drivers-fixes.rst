Moving Slackware to kernel 3.10: NVIDIA and Broadcom drivers fixes
##################################################################
:date: 2013-08-11 05:03
:author: Deny Dias
:category: Slackware
:tags: development, network, software, update, -current, broadcom, Slackware, nvidia, build, MacBook Pro, Linux, kernel, 3.10.5, slackbuild, driver
:slug: /moving-slackware-to-kernel-310-fixes-to

Last Tuesday, the 6th Aug, Pat (Patrick Volkerding, Slackware's
`BDFL`_) released Linux kernel 3.10.5 in the -current tree. Bellow you
can read Mr. Pat statement for this move:

    Looks like 3.10.x got LTS status, but more importantly fixes the
    power issue on resume with some Intel machines. So, we're bumping
    the kernel to 3.10.5, and will stick with that series for the
    release. A few more things to look at before calling this a beta,
    but it's pretty close. Enjoy!
    
    --Patrick Volkerding

Well done, Pat. But the move, at least for me, owner of a MacBook Pro
7,1, was far from what I can name an enjoyable task. Not your fault
tough. The one to blame is always those crappy proprietary hardware and
its drivers.

NVIDIA and Broadcom drivers, at least as they are distributed at
`SlackBuilds.org`_ just don't compile under the new 3.10 series kernel.
Both is going to miserably fail when you try to compile them either
using slackbuild's scripts or straight from the vendors tarballs.

So, let's troubleshoot it.

NVIDIA
======

NVIDIA was an easy fix. LinuxQuestion's user WhiteWolf1776 reported on
a `post`_ that "like it was planned, -current moves to 3.10 series and
nVidia releases a new driver 325.15." So you can build NVIDIA driver
successfully on your brand new 3.10.5 kernel, you can use the slackbuild
`provided`_ by WhiteWolf1776 or you can just copy (what I've done) your
SlackBuild.org's scripts (`nvidia-kernel`_ and `nvidia-driver`_), edit
.info to change version, download URL's and md5 checksum, edit
.SlackBuild to change versions and then build. They are going to build
and install with no errors.

Broadcom
========

Unlike NVIDIA drivers, Broadcom was a pain in the ass. Broadcom is
lazy enough to don't upgrade their proprietary Linux drivers since 2011.
So, after each major change on kernel's API or some core code used by
the WiFi card drivers, good developers out there must do their work and
fix that shit on Broadcom's side so it can compile and run on newer
Linuxes. Of course that somewhere in the future this trick will not work
anymore. But at least for now we, the poor Broadcom enabled hardware
owners, are in a safe place! Kudos to the Arch Linux `broadcom-wl
package`_ maintainer, Krejzi. He managed to patch the driver for that
distribution and I've put it together for Slackware.

So, to cut the crap talk out, all you have to do is to clone my GitHub
`repository`_ for that driver, download the Broadcom's driver tarball
from the vendor `website`_ in the same directory as the slackbuild lives
and run the slackbuild script. It should build with success and place a
package ready to install under your /temp. Install it and you should be
good to go with no cables.

Now, just as Pat said before, enjoy!

**Bonus**: Destroy Everything You Touch - Ladytron
==================================================

.. youtube:: JTTwlAT_AwU
   :width: 500
   :height: 281
   :align: center

.. _BDFL: https://en.wikipedia.org/wiki/Benevolent_Dictator_for_Life
.. _SlackBuilds.org: http://slackbuilds.org/
.. _post: http://www.linuxquestions.org/questions/slackware-14/new-nvidia-drivers-325-15-support-3-10-kernel-4175472319/#post5003987
.. _provided: https://github.com/WhiteWolf1776/Bumblebee-SlackBuilds
.. _nvidia-kernel: http://slackbuilds.org/repository/14.0/system/nvidia-kernel/
.. _nvidia-driver: http://slackbuilds.org/repository/14.0/system/nvidia-driver/
.. _broadcom-wl package: https://aur.archlinux.org/packages/broadcom-wl/
.. _repository: https://github.com/denydias/broadcom-sta-recent
.. _website: http://www.broadcom.com/support/802.11/linux_sta.php
