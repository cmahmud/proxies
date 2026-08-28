# SyndProxy validated proxy pool

## Current pool

- Alive now: 570
- Gold now: 423
- HTTP: 91 alive / 72 gold
- HTTPS: 114 alive / 21 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 188 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42522
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
