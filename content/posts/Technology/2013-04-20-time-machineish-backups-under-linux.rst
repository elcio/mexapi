Time Machine'ish backups under Linux
####################################
:date: 2013-04-20 01:11
:author: Deny Dias
:tags: rsnapshot, network, development, Linux, backup, software, rsync, Slackware
:slug: time-machineish-backups-under-linux

When I `switched`_ from Mac OS X to Slackware on my old MacBook Pro
7,1, I´ve `read`_ a lot about rsync snapshot backups. It works, indeed.
It just don't work so smooth and unattended as Time Machine did in Mac
OS X. There were two features I missed most under Linux/rsync setup:

#. The ability to backup to different mounts under different networks.
#. Make the system completely ignore backup tasks if I'm plugged to a
   network where I do not have a backup drive.

I work mainly at home. Here I do have a beautiful piece of appliance
from Synology, `DS211+`_, that provides me a full 2TB NAS with NFS,
mirrored RAID, backups itself to an external USB drive and many others
storage bells and whistles. This is my primary backup facility. When I'm
at home, I want my backups sent to my NFS mount at DS each four hours.

When I'm at the office tough, I count on an old Apple Time Capsule
which provides me 500GB over AFP or SMB. No frills and all the ugly
Apple closeness. But I'm still able to mount it using either AFP or SMB
on Linux.

When I hit the road, I still use an yet older 150GB external USB drive
as a backup storage.

Under OS X, deal with all this different storage destinations for Time
Machine backup was a piece of cake. But at Linux this shows to be
challenging. When I was updating my knowledge about rsync backups, it
became clear very quickly that rsync can't deal with multiple, dynamic
destinations. That's not rsync job. rsync's job is to move files way
around with confidence.

Then `rsnapshot`_ came to me. From it's website:

    rsnapshot is a filesystem snapshot utility for making backups of
    local and remote systems.

Just what I was looking for: local and remote backups. But there's a
catch: rsnapshot can't deal with dynamic mount points under different
networks too. It just expect that remote destination is already mounted
upon backup start.

I couldn't find any viable solution to make this happen so easily and
unattended as it was under Mac OS X's Time Machine.

So I decided to write my own piece of code to do it: `nsnapshot`_.

It relies on rsnapshot and takes tree arrays of parameters to decide
where a backup should sit: network address, mount point and a force
field.

The network parameter is the network address where the backup should
happen. For instance, let's say your IP is ``192.168.173.40``. Your network
address on this network is ``192.168.173.0``.

The mount point is the networked storage resource where your backup is
sent to. Of course this should be set under ``/etc/fstab`` first I'll leave
this as an exercise for the reader.

Finally, the force field says to ``nsnapshot`` that it should backup to
that mount point regardless your machine is on that network or not.
Great for locally mounted devices such as my old USB drive.

After set ``nsnapshot`` and ``rsnapshot.conf`` up, ``chmod +x`` on ``nsnapshot`` and
ran it through cron I've got completely unattended backups to either
local or remote storage, dynamically, just like I had on Time Machine.

One small and useful advice about cron setup if you are an Slackware
kind of person follows bellow (thanks to `Nick Coleman`_). Also, don't
forget to include ``ionice`` and ``nice`` commands so your system still gets
usable while rsnapshot/rsync is doing its thing.

.. code:: bash

    # Run snapshot backup levels
    0 */4 * * * ID=sshourly ionice -c 2 nice -n+19 /usr/local/bin/nsnapshot hourly >> /var/log/rsnapshot 2>&1
    50 21-23 * * * ID=ssdaily FREQ=2h/1h ionice -c 2 nice -n+19 /usr/local/bin/nsnapshot daily >> /var/log/rsnapshot 2>&1
    40 21-23 * * * ID=ssweekly FREQ=7d/1h ionice -c 2 nice -n+19 /usr/local/bin/nsnapshot weekly >> /var/log/rsnapshot 2>&1
    30 21-23 * * * ID=ssmonthly FREQ=30d/1h ionice -c 2 nice -n+19 /usr/local/bin/nsnapshot monthly >> /var/log/rsnapshot 2>&1

**Bonus**: Daft Punk Pharrell "Get Lucky" SNL Ad
================================================

.. youtube:: JMJwcOiBoZE
   :width: 500
   :height: 281
   :align: center

.. _switched: http://mexapi.macpress.com.br/2012/11/subversao-tecnologica-do-mac-os-x-para.html
.. _read: https://www.google.com.br/webhp?oq=linux+rsyc+snapshot#q=linux+rsync+snapshot
.. _DS211+: http://www.synology.com/us/products/DS211+/index.php
.. _rsnapshot: http://www.rsnapshot.org/
.. _nsnapshot: https://github.com/denydias/nsnapshot
.. _Nick Coleman: http://www.nickcoleman.org/blog/index.cgi/cronslackware!201112181115!unix
