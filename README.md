# usenetfs

usage: sshfs [user@]host:[dir] mountpoint [options]
usage: usenetfs [options] [[proto://[user:pass@]host/]]index.nzb mountpoint

mount -t usenet -o \
    server=nntp.server.com, \
    user=username, \
    pass=password, \
    index=rw, \
    mode=rw \
index.nzb /mnt/usenet

[file;//]/path/to/index.nzb           - rw default
ftp://[user:pass@]host.com/index.nzb  - rw if creds, ro otherwise
ssh://[user:pass@]host.com/index.nzb  - rw if creds, ro otherwise