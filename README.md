# SyndProxy validated proxy pool

## Current pool

- Alive now: 607
- Gold now: 414
- HTTP: 106 alive / 64 gold
- HTTPS: 139 alive / 23 gold
- SOCKS4: 178 alive / 159 gold
- SOCKS5: 184 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41302
- Ever gold: 1324

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
