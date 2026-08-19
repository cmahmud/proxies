# SyndProxy private pool

## Current pool

- Alive now: 1147
- Gold now: 483
- HTTP: 454 alive / 190 gold
- HTTPS: 276 alive / 113 gold
- SOCKS4: 210 alive / 78 gold
- SOCKS5: 207 alive / 102 gold

## Historical pool

- Discovered: 124845
- Ever alive: 19386
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
